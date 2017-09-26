from django.conf.urls import url

from librekids.messaging.apps import MessagingConfig as AppConfig

from . import views


app_name = AppConfig.name

urlpatterns = [
    url(r'^$', views.index, name='index'),
]
