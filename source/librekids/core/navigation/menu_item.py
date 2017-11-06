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
        self._isRedirect = False
        self._onNewTab = False
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
    
    
    def setTarget(self, target, isRedirect=False, onNewTab=False):
        '''
        Set the target
        @param target: menu-item target        
        '''
        
        self._target = target
        
        return self
    
    def isRedirect(self, isRedirect=True):
        '''
        Indicates whether the target is a redirect
        @param isRedirect: The browser redirects to the target. Otherwise, the response will be 
        displayed within the content section.
        '''
    
        self._isRedirect = isRedirect
        
        return self
        
        
    def onNewTab(self, onNewTab=True):
        '''
        Indicates whether the target shall be displayed on a new tab.
        It works with redirection targets only. Otherwise it will be ignored.
        @param onNewTab: The redirected page will be displayed on new tab. This works on 
        redirections only.
        '''
        
        self._onNewTab = onNewTab
        
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
    
    
    def getMap(self, parentPath=""):
        '''
        Returns the object data as a map object
        '''
        
        itemPath = "{0}.{1}".format(parentPath,self._name) if parentPath != "" else self._name
        
        mapObject = {
            "label": self._label, 
            "name": itemPath,
            "target": self._target,
            "is_redirect": self._isRedirect,
            "on_new_tab": self._onNewTab,
            "menu": [menuItem.getMap(itemPath) for menuItem in self._subMenu]
        }
        
        return mapObject
                  
    
        