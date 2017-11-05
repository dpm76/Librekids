'''
Created on 26 oct. 2017

@author: david
'''

class ContextMenuSet(object):
    '''
    Set of menu items displayed within a view's context menu
    '''

    def __init__(self, targetView):
        '''
        Constructor
        
        @param targetview: Name of the view where this set will be displayed. 
        '''
        self._targetView = targetView
        self._menuItems = []
    
    
    def addMenuItems(self, menuItems):
        '''
        Adds a list of menu items
        
        @param menuItems: List of MenuItem-objects.
        @return: This instance itself.
        '''
        
        self._menuItems += menuItems
        
        return self
    
    
    def addMenuItem(self, menuItem):
        '''
        Adds a menu item
        
        @param menuItem: A MenuItem-object.
        @return: This instance itself.
        '''
        
        self._menuItems.append(menuItem)
        
        return self 
    
    
    def getTargetView(self):
        '''
        @return: Name of the related view
        '''        
        
        return self._targetView
    
    
    def getMenuItems(self):
        '''
        @return: List of menu items
        '''
        
        return self._menuItems
    