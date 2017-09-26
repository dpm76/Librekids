from django.apps import apps as django_apps
from django.contrib import admin
from django.contrib.admin.sites import AlreadyRegistered

app_models = django_apps.get_app_config('core').get_models()
for model in app_models:
    try:
        admin.site.register(model)
    except AlreadyRegistered:
        pass
    
'''
admin.site.register(models.AuthorisedPerson)
admin.site.register(models.Child)
admin.site.register(models.Classroom)
admin.site.register(models.Company)
admin.site.register(models.Educator)
admin.site.register(models.Employee)
admin.site.register(models.Kindergarten)
admin.site.register(models.Parent)
admin.site.register(models.ActivityStreamEntry)
admin.site.register(models.ChildAuthorisation)
admin.site.register(models.Role)
'''