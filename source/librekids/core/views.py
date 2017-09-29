from django.http.response import HttpResponse
from django.shortcuts import render
from django.views.generic.base import TemplateView


class IndexView(TemplateView):

    template_name = "core/index.html"

    def get_context_data(self, **kwargs):
        context = super(IndexView, self).get_context_data(**kwargs)
        context["main_menu"] = [           
            {"label": "Home"},
            {"label": "Kids"},
            {"label": "Kindergarten"},
            {"label": "Portfolios"},
            {"label": "Messages"},
            {"label": "Projects"},
            {"label": "Equipment"}, 
        ]
                
        context["user_menu"] = [
            {"label": "Profile"},
            {"label": "My kids"},
            {"label": "My portfolios"},
            {"label": "My classrrom"},
            {"label": "About"},
            {"label": "Logout"},
        ]
        
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
            "label": "User name",
        }
                    
        return context


def login(request):
    '''
    Login view
    '''
    
    return HttpResponse("login")
    
    