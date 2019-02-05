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
    
    
    def __str__(self):
        '''
        Simple serialization
        '''
        
        return self.name


class Profile(models.Model):
    '''
    Generic profile for users
    '''

    user = models.OneToOneField(User, on_delete=models.CASCADE)
    phone_number = models.CharField(validators=[PhoneValidator.getInstance()], 
                                    max_length=15, blank=True)
    mobile_number = models.CharField(validators=[PhoneValidator.getInstance()], 
                                     max_length=15, blank=True)
    email = models.EmailField(blank=True)
    
    def save(self, force_insert=False, force_update=False, using=None, 
        update_fields=None):
        '''
        Overrides save method creating and saving the related user
        '''

        if not self.user:
            user = User.objects.create()
            self.user = user
            
        self.user.save() 
        
        return models.Model.save(self, force_insert=force_insert, force_update=force_update, using=using, update_fields=update_fields)
    
    def __str__(self):
        '''
        Simple serialization
        '''
        
        return self.user.username


class Parent(Profile):
    '''
    Mother or father or any relative of children  
    '''    
        
    address_primary = models.TextField(blank=True)
    address_secondary = models.TextField(blank=True)    
    work_number = models.CharField(validators=[PhoneValidator.getInstance()], 
                                    max_length=15, blank=True)
        

class Employee(Profile):
    '''
    Company's employee
    '''
    
    position = models.CharField(max_length=50, blank=True)
    supervisor = models.ForeignKey('self', null=True, blank=True, related_name="supervisor_of", on_delete=models.SET_NULL)
    join_date = models.DateField(null=True, blank=True)
    leave_date = models.DateField(null=True, blank=True)    
    

class Company(models.Model):
    '''
    Company with one more kindergartens 
    '''
    
    name = models.CharField(max_length=50, blank=False)
    address = models.TextField(blank=True)
    owner = models.ForeignKey(Employee, null=True, blank=True, on_delete=models.SET_NULL)
    

    def __str__(self):
        '''
        Simple serialization
        '''
        
        return self.name
    

class Kindergarten(models.Model):
    '''
    Kindergarten
    '''
    
    address = models.TextField(blank=True)
    phone_number = models.CharField(validators=[PhoneValidator.getInstance()], 
                                    max_length=15, blank=True)
    name = models.CharField(max_length=50, blank=False)
    company = models.ForeignKey(Company, null=True, blank=True, on_delete=models.CASCADE)
    director = models.ForeignKey(Employee, null=True, blank=True, on_delete=models.SET_NULL)
    
    def getEmployees(self):
        
        classrooms = Classroom.objects.filter(kindergarten__pk = self.pk)
        employees = Employee.objects.filter(classrooms__in = classrooms).distinct()
        
        return employees


    def __str__(self):
        '''
        Simple serialization
        '''
        
        return self.name

    
    
class Classroom(models.Model):
    '''
    Class room or group of children, leaded by an educator
    '''
    
    name = models.CharField(max_length=50, blank=False)
    kindergarten = models.ForeignKey(Kindergarten, on_delete=models.CASCADE, related_name="classrooms")
    educators = models.ManyToManyField(Employee, related_name="classrooms")
    
    
    def __str__(self):
        '''
        Simple serialization
        '''
        
        return self.name


class Child(models.Model):
    '''
    Every single child
    '''
    
    name=models.CharField(max_length=50, blank=False)
    classroom = models.ForeignKey(Classroom, null=True, blank=True, on_delete = models.SET_NULL,\
                                   related_name="children")
    educator = models.ForeignKey(Employee, null=True, blank=True, on_delete=models.SET_NULL)
    parents = models.ManyToManyField(Parent, related_name="children")
    join_date = models.DateField(null=True, blank=True)
    leave_date = models.DateField(null=True, blank=True) 
    
    
    def __str__(self):
        '''
        Simple serialization
        '''
        
        return self.name

    
    
class ChildAuthorisation(models.Model):
    '''
    Authorisation of someone on any child
    '''
    
    authorised_person = models.ForeignKey(AuthorisedPerson, on_delete=models.CASCADE)
    on_children = models.ManyToManyField(Child)
    is_active = models.BooleanField()
    #Depending this field the authorisation will be time enclosed or not.
    is_enclosed = models.BooleanField()    
    date_start = models.DateField(null=True, blank=False)
    date_end = models.DateField(null=True, blank=False)


class ActivityStreamEntry(models.Model):
    '''
    Stream notification
    '''
    
    actor = models.ForeignKey(User, null=True, on_delete=models.SET_NULL)
    object_type = models.ForeignKey(ContentType, null=False, blank=False, on_delete=models.CASCADE, 
                                    related_name="activity_stream_entry_as_object_type")
    object_id = models.PositiveIntegerField()
    object = GenericForeignKey('object_type', 'object_id')
    target_type = models.ForeignKey(ContentType, null=True, blank=True, on_delete=models.SET_NULL,
                                    related_name="activity_stream_entry_as_target_type")
    target_id = models.PositiveIntegerField(null=True, blank=False)
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
    

    def __str__(self):
        '''
        Simple serialization
        '''
        
        return self.name

    

class DataIntoAreaRelation(models.Model):
    '''
    Relation between data-area and data 
    '''
    
    data_area = models.ForeignKey(DataArea, on_delete=models.CASCADE)
    data_type = models.ForeignKey(ContentType, null=False, blank=False, on_delete=models.CASCADE)
    data_id = models.PositiveIntegerField()
    data = GenericForeignKey('data_type', 'data_id')

