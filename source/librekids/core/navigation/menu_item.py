'''
Created on 13 oct. 2017

@author: david
'''

class MenuItem(object):
    '''
    Menu-item class
    '''


    def __init__(self, name=""):
        '''
        Constructor
        @param name: menu-item name 
        '''
        
        self._name = name
        self._label = None
        self._target = None
        self._subMenu = []
        
    
    def setName(self, name):
        '''
        Set the name
        @param name: menu-item name
        '''
        
        self._name = name
        
        return self
    
    
    def setLabel(self, label):
        '''
        Set the label
        @param label: menu-item label
        '''
        
        self._label = label
        
        return self
    
    
    def setTarget(self, target):
        '''
        Set the target
        @param target: menu-item target
        '''
        
        self._target = target
        
        return self
    
    
    def setSubmenu(self, subMenu):
        '''
        Set the submenu
        @param subMenu: menu-item submenu 
        '''
        
        self._subMenu = subMenu
        
        return self
    
    
    def getName(self):
        '''
        Get the name        
        '''
        
        return self._name        
    
    
    def getLabel(self):
        '''
        Get the label        
        '''
        
        return self._label
    
    
    def getTarget(self):
        '''
        Set the target
        '''
        
        return self._target
            
    
    def getSubmenu(self):
        '''
        Set the submenu         
        '''
        
        return self._subMenu
    
    
    def getMap(self):
        '''
        Returns the object data as a map object
        '''
        
        mapObject = {
            "label": self._label, 
            "name": self._name,
            "target": self._target,
            "menu": [menuItem.getMap() for menuItem in self._subMenu]
        }
        
        return mapObject
                  
    
        