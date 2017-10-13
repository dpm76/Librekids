from librekids.core.apps import ModuleConfig
from librekids.core.navigation.menu_item import MenuItem


class MessagingConfig(ModuleConfig):
    name = 'messaging'

    @staticmethod
    def getMainMenu():
        
        mainMenu = [
            MenuItem("messages").setLabel("Messages"),
        ]
        
        return mainMenu
