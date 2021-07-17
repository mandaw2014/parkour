from ursina import *

class PauseMenu(Entity):
    def __init__(self):
        super().__init__(parent = camera.ui, ignore_paused = True)

        self.pause_menu = Entity(parent = self, enabled = True)
        self.player = None
        self.main_menu = None

        self.level01 = None
        self.level02 = None
        self.level03 = None
        self.level04 = None
        self.level05 = None
        self.level06 = None
        self.level07 = None
        self.level08 = None
        self.level09 = None

        def reset():
            self.pause_menu.disable()
            self.player.enable()
            mouse.locked = True
            self.player.time.enable()
            self.player.time_running = True

            if self.level01.is_enabled == True:
                self.player.position = (888, 12, 18)
                self.player.rotation = (0, -142, 0)
            if self.level02.is_enabled == True:
                self.player.position = (811, 14, 108)
                self.player.rotation = (0, -267, 0)
            if self.level03.is_enabled == True:
                self.player.position = (809, 4, 106)
                self.player.rotation = (0, 181, 0)
            if self.level04.is_enabled == True:
                self.player.position = (5, 10, -150)
                self.player.rotation = (0, -90, 0)
            if self.level05.is_enabled == True:
                self.player.position = (-1, -5, 34)
                self.player.rotation = (0, -180, 0)
            if self.level06.is_enabled == True:
                self.player.position = (130, -120, 0)
                self.player.rotation = (0, -90, 0)
            if self.level07.is_enabled == True:
                self.player.position = (0, 10, 0)
                self.player.rotation = (0, 0, 0)
            if self.level09.is_enabled == True:
                self.player.position = (0, 10, 0)
                self.player.rotation = (0, 0, 0)
            if self.level09.is_enabled == True:
                self.player.position = (0, 10, 0)
                self.player.rotation = (0, 0, 0)

        def resume():
            self.player.enable()
            mouse.locked = True
            self.pause_menu.disable()
            self.player.time.enable()
            self.player.time_running = True

        resume_button = Button(text = "R e s u m e", color = color.black, scale_y = 0.1, scale_x = 0.3, y = 0.12, parent = self.pause_menu)
        reset_button = Button(text = "R e s e t", color = color.black, scale_y = 0.1, scale_x = 0.3, y = 0, parent = self.pause_menu)
        quit_button = Button(text = "Q u i t", color = color.black, scale_y = 0.1, scale_x = 0.3, y = -0.12, parent = self.pause_menu)
        quit_button.on_click = application.quit
        reset_button.on_click = Func(reset)
        resume_button.on_click = Func(resume)
