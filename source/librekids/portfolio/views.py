from django.http.response import HttpResponse
from django.shortcuts import render


def index(request):
    '''
    TODO: Dummy view
    '''
    
    return HttpResponse("portfolio app")

