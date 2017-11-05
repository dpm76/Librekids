from django.contrib.auth.mixins import LoginRequiredMixin
from django.http.response import HttpResponse
from django.shortcuts import render
from django.views.generic.base import TemplateView
from django.views.generic.list import ListView

from librekids.core.models import Kindergarten
from librekids.core.navigation.menu_item import MenuItem
from librekids.core.navigation.module_manager import ModuleManager


class IndexView(LoginRequiredMixin, TemplateView):

    template_name = "core/index.html"
    login_url = "/login/"
    
    def get_context_data(self, **kwargs):
        context = super(IndexView, self).get_context_data(**kwargs)
#         context["main_menu"] = [           
#             {"label": "Home", "name": "home", "is_selected": True},            
#             {"label": "Kindergarten", "name": "kindergarten",
#                 "target": reverse("core:kindergarten"),
#                 "menu": [
#                     {"label": "Classrooms", "name": "classroom"},
#                     {"label": "Children", "name": "children"},
#                     {"label": "Employees", "name": "employees"},
#                 ]             
#             },
#             {"label": "Portfolios", "name": "portfolios"},
#             {"label": "Messages", "name": "messages"},
#             {"label": "Projects", "name": "projects"},
#             {"label": "Equipment", "name": "equipment"}, 
#         ]
                
        context["main_menu"] = ModuleManager.getInstance().getMainMenuAsMap()
        context["main_menu"][0]["is_selected"] = True 
        
        context["user_menu"] = MenuItem("user")\
                .setLabel(self.request.user.username)\
                .setTarget("")\
                .setSubmenu([
                    MenuItem("profile").setLabel("Profile"),
                    MenuItem("children").setLabel("My kids"),
                    MenuItem("portfolios").setLabel("My portfolios"),
                    MenuItem("classroom").setLabel("My classroom"),
                    MenuItem("about").setLabel("About"),
                    MenuItem("logout").setLabel("Logout"),
                ]).getMap()
        
#         context["user_menu"] = [
#             {"label": "Profile"},
#             {"label": "My kids"},
#             {"label": "My portfolios"},
#             {"label": "My classroom"},
#             {"label": "About"},
#             {"label": "Logout"},
#         ]
#         
        context["context_panel"] = {
            "label": "Portfolio",
            "context_menu": [
                {"label": "see portfolio"},
                {"label": "new report"},
                {"label": "send message to fathers"},
                {"label": "see authorized persons"},
                {"label": "new authorized person"},
            ]
        }
        
        context["breadcrumbs"] = [
            {"label" : "home"},
            {"label" : "Pepito Pérez"},
            {"label" : "portfolio"},            
        ]
        
        context["user_notifications"] = [
            {
                "label": "Messages",
                "name": "messages",
                "status_type": "integer",
                "status_value": "2"
            },
            {
                "label": "Activity",
                "name": "activity-stream",
                "status_type": "boolean",
                "status_value": "true"
            },
            {
                "label": "Custom",
                "name": "custom",
                "status_type": "boolean",
                "status_value": "false"
            },
        ]
        
        context["user_data"] = {
            "label": self.request.user.username,
        }
                    
        return context


class HomeView(LoginRequiredMixin, TemplateView):
    '''
    Home view
    '''

    template_name = "core/home.html"
    raise_exception = True

    def get_context_data(self, **kwargs):
        context = super(HomeView, self).get_context_data(**kwargs)
        
        return context

    
class KindergartenView(LoginRequiredMixin, ListView):
    '''
    Kindergarten view
    '''
        
    model = Kindergarten
    context_object_name = "kindergartens"
    template_name = "core/kindergarten_list.html"
    raise_exception = True 
    
#     def get_context_data(self, **kwargs):
#         context = super(KindergartenView, self).get_context_data(**kwargs)
#         #context['now'] = timezone.now()
#         return context
    
    
    