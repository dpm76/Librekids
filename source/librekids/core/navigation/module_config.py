'''
Created on 13 oct. 2017

@author: david
'''
from django.apps.config import AppConfig


class ModuleConfig(AppConfig):
    '''
    Configuration class for modules
    '''
    
    @staticmethod
    def getMainMenu():
        return []
    
    @staticmethod
    def getContextMenu():
        return []
    
    @staticmethod
    def getNotifiers():
        return []
    
    @staticmethod
    def getDashlets():
        return []