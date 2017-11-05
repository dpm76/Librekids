from django.urls.base import reverse

from librekids.core.navigation.context_menu import ContextMenuSet
from librekids.core.navigation.menu_item import MenuItem
from librekids.core.navigation.module_config import ModuleConfig


class CoreConfig(ModuleConfig):
    name = 'core'
    
    @staticmethod
    def getMainMenu():
        '''
        @return: the main menu for this module
        '''
        
        mainMenu = [
            MenuItem("home")
                .setLabel("Home")
                .setTarget(reverse("core:home")),
            MenuItem("kindergarten")
                .setLabel("Kindergarten")
                .setTarget(reverse("core:kindergarten"))
                .setSubmenu([
                    MenuItem("classroom").setLabel("Classrooms"),
                    MenuItem("children").setLabel("Children"),
                    MenuItem("employees").setLabel("Employees"),
                ]),
        ]
        
        return mainMenu
    

    @staticmethod
    def getContextMenuSets():
        '''
        @return: menu item sets
        '''
        
        contextMenuSets = [
            ContextMenuSet("kindergarten").addMenuItems([
                MenuItem("new-kindergarten").setLabel("New kindergarten"),
                MenuItem("view-kindergartens").setLabel("View kindergartens"),  
                MenuItem("view-children").setLabel("View children"),              
            ]),
            ContextMenuSet("classroom").addMenuItems([
                MenuItem("new-classroom").setLabel("New classroom"),
                MenuItem("view-classrooms").setLabel("View classrooms"),                
                MenuItem("view-children").setLabel("View children"),
            ]),
            ContextMenuSet("children").addMenuItems([
                MenuItem("new-child").setLabel("New child"),
                MenuItem("view-classroom").setLabel("View classroom"),                
                MenuItem("view-parents").setLabel("View parents"),
                MenuItem("view-authorised").setLabel("View authorised"),
            ]),
        ]        
                
        return contextMenuSets
    