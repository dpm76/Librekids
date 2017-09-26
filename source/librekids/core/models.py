from django.contrib.auth.models import User, Group
from django.contrib.contenttypes.fields import GenericForeignKey
from django.contrib.contenttypes.models import ContentType
from django.core.validators import RegexValidator
from django.db import models


class PhoneValidator(RegexValidator):
    '''
    Ensures a phone number input was correctly inserted
    '''
    
    instance = None    
    
    @staticmethod
    def getInstance():
        '''
        Returns single instance
        '''
        
        if PhoneValidator.instance == None:            
            PhoneValidator.instance = PhoneValidator()
            
        return PhoneValidator.instance
    
    
    def __init__(self):
        '''
        Constructor
        '''
        RegexValidator.__init__(self, regex=r"^(\+|00)?(\d|-|\.|\s){9,15}$", 
                                 message="Phone number must be entered in the format: '+999999999'. Up to 15 digits allowed.")

    

class AuthorisedPerson(models.Model):
    '''
    Any other people authorized to pick any child up
    '''
    
    name=models.CharField(max_length=50, blank=False)    
    address_primary = models.TextField(blank=True)
    address_secondary = models.TextField(blank=True)
    phone_number = models.CharField(validators=[PhoneValidator.getInstance()], 
                                    max_length=15, blank=True)
    work_number = models.CharField(validators=[PhoneValidator.getInstance()], 
                                    max_length=15, blank=True)
    mobile_number = models.CharField(validators=[PhoneValidator.getInstance()], 
                                     max_length=15, blank=True)
    email = models.EmailField(blank=True)



class Parent(AuthorisedPerson):
    '''
    Mother or father or any relative of children  
    '''
    
    pass


class Employee(models.Model):
    '''
    Company's employee
    '''
    
    name=models.CharField(max_length=50)
    position = models.CharField(max_length=50, blank=True)
    supervisor = models.ForeignKey('self', null=True, related_name="supervisor_of")
    phone_number = models.CharField(validators=[PhoneValidator.getInstance()], 
                                    max_length=15, blank=True)
    mobile_number = models.CharField(validators=[PhoneValidator.getInstance()], 
                                     max_length=15, blank=True)
    email = models.EmailField(blank=True)


class Company(models.Model):
    '''
    Company with one more kindergartens 
    '''
    
    name = models.CharField(max_length=50, blank=False)
    address = models.TextField()
    owner = models.ForeignKey(Employee)
    

class Kindergarten(models.Model):
    '''
    Kindergarten
    '''
    
    address = models.TextField()
    phone_number = models.CharField(validators=[PhoneValidator.getInstance()], 
                                    max_length=15, blank=True)
    name = models.CharField(max_length=50, blank=False)
    company = models.ForeignKey(Company, on_delete=models.CASCADE)
    director = models.ForeignKey(Employee)    
    
    
class Classroom(models.Model):
    '''
    Class room or group of children, leaded by an educator
    '''
    
    name = models.CharField(max_length=50, blank=False)
    kindergarten = models.ForeignKey(Kindergarten, on_delete=models.CASCADE)


class Educator(Employee):
    '''
    Educator
    '''
    
    main_classroom = models.ForeignKey(Classroom)


class Child(models.Model):
    '''
    Every single child
    '''
    
    name=models.CharField(max_length=50, blank=False)
    educator = models.ForeignKey(Educator, null=True, on_delete=models.SET_NULL)
    parents = models.ManyToManyField(Parent)
    
    
class ChildAuthorisation(models.Model):
    '''
    Authorisation of someone on any child
    '''
    
    authorised_person = models.ForeignKey(AuthorisedPerson, on_delete=models.CASCADE)
    on_children = models.ManyToManyField(Child)
    is_active = models.BooleanField()
    #Depending this field the authorisation will be time enclosed or not.
    is_enclosed = models.BooleanField()    
    date_start = models.DateField(null=True)
    date_end = models.DateField(null=True)


class ActivityStreamEntry(models.Model):
    '''
    Stream notification
    '''
    
    actor = models.ForeignKey(User)
    object_type = models.ForeignKey(ContentType, null=False, on_delete=models.CASCADE, 
                                    related_name="activity_stream_entry_as_object_type")
    object_id = models.PositiveIntegerField()
    object = GenericForeignKey('object_type', 'object_id')
    target_type = models.ForeignKey(ContentType, null=True, on_delete=models.SET_NULL,
                                    related_name="activity_stream_entry_as_target_type")
    target_id = models.PositiveIntegerField()
    target = GenericForeignKey('target_type', 'target_id')
    verb = models.CharField(max_length=50, blank=False)
    time_stamp = models.DateTimeField(blank=False)
    
    
class Role(Group):
    '''
    Employee's role. Determines the permissions on models that a user has. 
    '''
    
    description = models.TextField(blank=True)
    

class DataArea(models.Model):
    '''
    User group. Determines the access-grant on a concrete data that a user has.
    '''
    
    name = models.CharField(max_length=50, blank=False)
    description = models.TextField(blank=True)
    users = models.ManyToManyField(User)
    

class DataIntoAreaRelation(models.Model):
    '''
    Relation between data-area and data 
    '''
    
    data_area = models.ForeignKey(DataArea, on_delete=models.CASCADE)
    data_type = models.ForeignKey(ContentType, null=True, on_delete=models.CASCADE)
    data_id = models.PositiveIntegerField()
    data = GenericForeignKey('data_type', 'data_id')

