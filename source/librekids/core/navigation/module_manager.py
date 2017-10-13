'''
Created on 13 oct. 2017

@author: david
'''
import importlib
import inspect

import librekids
from librekids.core.navigation.module_config import ModuleConfig


class ModuleManager(object):
    '''
    Manages the installed modules
    '''

    DEFAULT_CONFIG_LOCATION = "apps"
    
    _instance = None
    
    @staticmethod
    def getInstance():
        '''
        Returns the single instance
        '''
        
        if ModuleManager._instance == None:
            ModuleManager._instance = ModuleManager()
            
        return ModuleManager._instance
        

    def __init__(self, appList = librekids.settings.INSTALLED_APPS, configLocation = DEFAULT_CONFIG_LOCATION):
        '''
        Constructor
        '''
        
        self._mainMenu = []
        
        for appName in appList:
            
            appModule = importlib.import_module(appName)            
            if hasattr(appModule, configLocation):                
                
                moduleConfigLocation = importlib.import_module("{0}.{1}".format(appName, configLocation))
                
                classes = inspect.getmembers(moduleConfigLocation, inspect.isclass)
                for moduleClass in classes:
                    classObject = moduleClass[1]  
                    if issubclass(classObject, ModuleConfig) and classObject != ModuleConfig:
                        
                        self._mainMenu += classObject.getMainMenu()                         
                        
        
    def getMainMenuItems(self):
        '''
        Get the main menu items
        '''
        
        return self._mainMenu
    
    
    def getMainMenuAsMap(self):
        '''
        Get the main menu as an array of map object
        '''
        
        return [menuItem.getMap() for menuItem in self._mainMenu]
        
    
    def getContextMenu(self, name):
        '''
        Get a context menu
        '''
        
        pass
    