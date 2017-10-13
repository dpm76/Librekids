from librekids.core.apps import ModuleConfig
from librekids.core.navigation.menu_item import MenuItem


class PortfolioConfig(ModuleConfig):
    name = 'portfolio'

    @staticmethod
    def getMainMenu():
        
        mainMenu = [
            MenuItem("portfolios").setLabel("Portfolios"),            
        ]
        
        return mainMenu
