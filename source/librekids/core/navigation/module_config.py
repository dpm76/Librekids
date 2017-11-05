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
        '''
        @return: the main menu for this module
        '''
        
        return []
    
    @staticmethod
    def getContextMenuSets():
        '''
        @return: menu item sets
        '''
        
        return []
    
    @staticmethod
    def getNotifiers():
        return []
    
    @staticmethod
    def getDashlets():
        return []