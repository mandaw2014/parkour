from ursina import *

app = Ursina()

class MainMenu(Entity):
    def __init__(self):
        super().__init__(
            parent = camera.ui
        )

        self.main_menu = Entity(parent = self, enabled = True)

        def start():
            player.enable()
            mouse.locked = True
            self.main_menu.disable()

        title = Entity(model = "quad", scale = (0.65, 0.2, 0.2), texture = "assets/parkour_logo_4", parent = self.main_menu, y = 0.3)

        start_button = Button(text = "S t a r t - G a m e", color = color.black, scale_y = 0.1, scale_x = 0.3, y = -0.1, parent = self.main_menu)
        quit_button = Button(text = "Q u i t", color = color.black, scale_y = 0.1, scale_x = 0.3, y = -0.22, parent = self.main_menu)
        quit_button.on_click = application.quit
        start_button.on_click = Func(start)


m = MainMenu()

app.run()
