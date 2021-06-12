from ursina import *

class PauseMenu(Entity):
    def __init__(self):
        super().__init__(parent = camera.ui, ignore_paused = True)

        self.pause_menu = Entity(parent = self, enabled = True)

        def reset():
            self.pause_menu.disable()
            player.position = (0, 5, 0)
            player.enable()
            mouse.locked = True

        def resume():
            player.enable()
            mouse.locked = True
            self.pause_menu.disable()

        resume_button = Button(text = "R e s u m e", color = color.black, scale_y = 0.1, scale_x = 0.3, y = -0.08, parent = self.pause_menu)
        reset_button = Button(text = "R e s e t", color = color.black, scale_y = 0.1, scale_x = 0.3, y = -0.2, parent = self.pause_menu)
        quit_button = Button(text = "Q u i t", color = color.black, scale_y = 0.1, scale_x = 0.3, y = -0.32, parent = self.pause_menu)
        quit_button.on_click = application.quit
        reset_button.on_click = Func(reset)
        resume_button.on_click = Func(resume)
