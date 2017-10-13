from django.urls.base import reverse

from librekids.core.navigation.menu_item import MenuItem
from librekids.core.navigation.module_config import ModuleConfig


class CoreConfig(ModuleConfig):
    name = 'core'
    
    @staticmethod
    def getMainMenu():
        
        mainMenu = [
            MenuItem("home").setLabel("Home"),
            MenuItem("kindergarten")\
                .setLabel("Kindergarten")\
                .setTarget(reverse("core:kindergarten"))\
                .setSubmenu([
                    MenuItem("classroom").setLabel("Classrooms"),
                    MenuItem("children").setLabel("Children"),
                    MenuItem("employees").setLabel("Employees"),
                ]),
        ]
        
        return mainMenu
