from django.http.response import HttpResponse
from django.shortcuts import render
from django.views.generic.base import TemplateView


class IndexView(TemplateView):

    template_name = "core/index.html"

    def get_context_data(self, **kwargs):
        context = super(IndexView, self).get_context_data(**kwargs)
        #context['latest_articles'] = Article.objects.all()[:5]
        return context


def login(request):
    '''
    Login view
    '''
    
    return HttpResponse("login")
    
    