from ursina import *

# Main Menu Example, or it can be any kind of menu, like Inventory, Quest journal, etc.
# Created by Doctor
# 09 Feb 21

# Class of game menu
# MainMenu
class MainMenu(Entity):
    def __init__(self, **kwargs):
        super().__init__(parent=camera.ui, ignore_paused=True)

        self.main_menu = Entity(parent=self, enabled=True)
        self.options_menu = Entity(parent=self, enabled=False)
        self.help_menu = Entity(parent=self, enabled=False)

        Text("MAIN MENU", parent=self.main_menu, y=0.4, x=0, origin=(0,0))

        def quit_game():
            application.quit()

        def options_menu_btn():
            self.options_menu.enable()
            self.main_menu.disable()

        def help_menu_btn():
            self.help_menu.enable()
            self.main_menu.disable()

        ButtonList(button_dict={
            "Start": Func(print_on_screen,"You clicked on the Start button!", position=(0,.1), origin=(0,0)),
            "Options": Func(options_menu_btn),
            "Help": Func(help_menu_btn),
            "Exit": Func(quit_game)
        },y=0,parent=self.main_menu)

        Text ("OPTIONS MENU", parent=self.options_menu, y=0.4, x=0, origin=(0, 0))

        def options_back_btn_action():
            self.main_menu.enable()
            self.options_menu.disable()

        Button("Back",parent=self.options_menu,y=-0.3,scale=(0.1,0.05),color=rgb(50,50,50),
               on_click=options_back_btn_action)

        Text ("HELP MENU", parent=self.help_menu, y=0.4, x=0, origin=(0, 0))

        def help_back_btn_action():
            self.main_menu.enable()
            self.help_menu.disable()

        ButtonList (button_dict={
            "Gameplay": Func(print_on_screen,"You clicked on Gameplay help button!", position=(0,.1), origin=(0,0)),
            "Battle": Func(print_on_screen,"You clicked on Battle help button!", position=(0,.1), origin=(0,0)),
            "Control": Func(print_on_screen,"You clicked on Control help button!", position=(0,.1), origin=(0,0)),
            "Back": Func (help_back_btn_action)
        }, y=0, parent=self.help_menu)
        
        for key, value in kwargs.items ():
            setattr (self, key, value)

    def input(self, key):
        if self.main_menu.enabled:
            if key == "escape":
                # Close app
                application.quit()

        if self.options_menu.enabled:
            if key == "escape":
                self.main_menu.enable()
                self.options_menu.disable()

        if self.help_menu.enabled:
            if key == "escape":
                self.main_menu.enable()
                self.help_menu.disable()

    def update(self):
        pass
