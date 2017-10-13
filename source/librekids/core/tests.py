from django.test import TestCase
from django.urls.base import reverse

from librekids.core.navigation.menu_item import MenuItem
from librekids.core.navigation.module_config import ModuleConfig
from librekids.core.navigation.module_manager import ModuleManager


class ModuleTestConfig(ModuleConfig):
    name = 'tests'
    
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


class NavigationTests(TestCase):    
        
    
    def test_mainMenuGeneration(self):
        
        appList = ["librekids.core"]
        configLocation = "tests"
        
        manager = ModuleManager(appList, configLocation)
        menu = manager.getMainMenuItems()
        
        self.assertEqual(menu[0].getName(), "home", "Main menu generation failed!")
        self.assertEqual(menu[1].getName(), "kindergarten", "Main menu generation failed!")
        
        submenu = menu[1].getSubmenu()
        
        self.assertEqual(submenu[0].getName(), "classroom", "Main menu generation failed!")
        self.assertEqual(submenu[1].getName(), "children", "Main menu generation failed!")
        self.assertEqual(submenu[2].getName(), "employees", "Main menu generation failed!")
        
    
    def test_menuItemAsMap(self):
        
        menuItem = MenuItem("name").setLabel("label");
        menuItemMap = menuItem.getMap()
        
        target = {
            "name": "name",
            "label": "label",
            "target": None,
            "menu": []
        }
        
        self.assertDictEqual(menuItemMap, target, "Menu item mapped incorrectly.")
    
    
    def test_mainMenuHashmap(self):
        
        appList = ["librekids.core"]
        configLocation = "tests"
        
        manager = ModuleManager(appList, configLocation)
        menuMap = manager.getMainMenuAsMap()
        
        self.assertIsNotNone(menuMap, "Main menu not generated.")
        
        target = [        
            {"label": "Home", "name": "home", "target": None, "menu": []},
            {"label": "Kindergarten", "name": "kindergarten",
                    "target": reverse("core:kindergarten"),
                    "menu": [
                        {"label": "Classrooms", "name": "classroom", "target": None, "menu": []},
                        {"label": "Children", "name": "children", "target": None, "menu": []},
                        {"label": "Employees", "name": "employees", "target": None, "menu": []},
                    ]             
                }
        ]
        
        self.assertEqual(len(menuMap), len(target), "Unexpected menu length.")
        
        for menuIndex in range(len(menuMap)):  
            self.assertDictEqual(menuMap[menuIndex], target[menuIndex], "Menu mapped incorrectly!")
        
        