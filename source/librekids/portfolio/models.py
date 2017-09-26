from django.db import models

from librekids.core.models import Employee, Child, Classroom, Kindergarten


class Folder(models.Model):
    '''
    Generic folder
    '''
    
    owner = models.ForeignKey(Employee, null=True, on_delete=models.SET_NULL)

    
class Report(models.Model):
    '''
    Report
    '''
    
    folder = models.ForeignKey(Folder, on_delete=models.CASCADE)
    content_text = models.TextField(blank=True)
    is_draft = models.BooleanField(default=True)
    

class ReportEdition(models.Model):
    '''
    Edition of a report
    '''
    
    report = models.ForeignKey(Report, on_delete=models.CASCADE)
    edited_by = models.ForeignKey(Employee, null=True, on_delete=models.SET_NULL)
    edition_time = models.DateTimeField(null=False)
    

class ChildFolder(Folder):
    '''
    Folder related to a child
    '''
    
    child = models.ForeignKey(Child, on_delete=models.CASCADE) 


class ClassroomFolder(Folder):
    '''
    Folder related to a classroom
    '''
    
    classroom = models.ForeignKey(Classroom, on_delete=models.CASCADE)
    
    
class KindergartenFolder(Folder):
    '''
    Folder related to a kindergarten
    '''
    
    kindergarten = models.ForeignKey(Kindergarten, on_delete=models.CASCADE)
