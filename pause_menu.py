from ursina import *

class PauseMenu(Entity):
    def __init__(self, **kwargs):
        super().__init__(parent = camera.ui, ignore_paused = True)

        self.pause_menu = Entity(parent = self, enabled = True)

        def resume():
            self.pause_menu.disable()
            player.enable()
            mouse.locked = True
        def reset():
            player.position = (0, 2, 0)
            self.pause_menu.disable()
            player.enable()
            mouse.locked = True

        ButtonList(button_dict = {
            "Resume": Func(resume),
            "Reset": Func(reset),
            "Quit": Func(quit)
        }, y = 0, parent = self.pause_menu)