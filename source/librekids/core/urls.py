from django.conf.urls import url

from librekids.core.apps import CoreConfig as AppConfig
from . import views


app_name = AppConfig.name

urlpatterns = [
    url(r'^$', views.IndexView.as_view(), name='index'),
    url(r'^kindergarten/$', views.KindergartenView.as_view(), name='kindergarten'),
]
