from librekids.core.apps import ModuleConfig
from librekids.core.navigation.context_menu import ContextMenuSet
from librekids.core.navigation.menu_item import MenuItem


class PortfolioConfig(ModuleConfig):
    name = 'portfolio'

    @staticmethod
    def getMainMenu():
        '''
        @return: the main menu for this module
        '''
        
        mainMenu = [
            MenuItem("portfolios").setLabel("Portfolios"),            
        ]
        
        return mainMenu

    @staticmethod
    def getContextMenuSets():
        '''
        @return: menu item sets
        '''
        
        newPortfolio = MenuItem("new-portfolio").setLabel("New portfolio")
        viewPortFolios = MenuItem("view-portfolios").setLabel("View portfolios")  
        
        
        contextMenuSets = [
            ContextMenuSet("portfolio").addMenuItems([                
                MenuItem("new-portfolio").setLabel("New portfolio"),
                MenuItem("view-personal").setLabel("Personal portfolios"),
                MenuItem("view-kindergarten").setLabel("Kindergarten portfolios"),
                MenuItem("view-classroom").setLabel("Classroom portfolios"),
                MenuItem("view-child").setLabel("Child portfolios"),
                MenuItem("view-employee").setLabel("Employee portfolios"),
            ]),
            ContextMenuSet("kindergarten").addMenuItems([                
                newPortfolio,
                viewPortFolios,
            ]),
            ContextMenuSet("classroom").addMenuItems([
                newPortfolio,
                viewPortFolios,
            ]),
            ContextMenuSet("children").addMenuItems([
                newPortfolio,
                viewPortFolios,
            ]),
            ContextMenuSet("employee").addMenuItems([
                newPortfolio,
                viewPortFolios,
            ]),

        ]        
                
        return contextMenuSets
    