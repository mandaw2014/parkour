from ursina import *

class MainMenu(Entity):
    def __init__(self):
        super().__init__(
            parent = camera.ui
        )

        self.main_menu = Entity(parent = self, enabled = True)
        self.levels_menu = Entity(parent = self, enabled = False)
        self.player = None

        self.level01 = None
        self.level02 = None
        self.level03 = None
        self.level04 = None
        self.level05 = None
        self.level06 = None
        self.level07 = None
        self.level08 = None
        self.level09 = None

        def start():
            self.player.enable()
            mouse.locked = True
            self.main_menu.disable()
            self.player.time_running = True

        def levels():
            self.main_menu.disable()
            self.levels_menu.enable()

        def level01_menu():
            self.main_menu.disable()
            self.levels_menu.disable()
            self.player.enable()
            self.player.time_running = True
            mouse.locked = True
        
        def level02_menu():
            self.main_menu.disable()
            self.levels_menu.disable()
            self.player.enable()
            self.player.time_running = True
            self.player.position = (811, 14, 108)
            self.player.rotation = (0, -267, 0)
            mouse.locked = True

            self.level01.disable()
            self.level02.enable()

        def level03_menu():
            self.main_menu.disable()
            self.levels_menu.disable()
            self.player.enable()
            self.player.time_running = True
            self.player.position = (809, 4, 106)
            self.player.rotation = (0, 181, 0)
            mouse.locked = True

            self.level01.disable()
            self.level03.enable()

        def level04_menu():
            self.main_menu.disable()
            self.levels_menu.disable()
            self.player.enable()
            self.player.time_running = True
            self.player.position = (5, 10, -150)
            self.player.rotation = (0, 0, 0)
            mouse.locked = True

            self.level01.disable()
            self.level04.enable()

        def level05_menu():
            self.main_menu.disable()
            self.levels_menu.disable()
            self.player.enable()
            self.player.time_running = True
            self.player.position = (-1, -5, 34)
            self.player.rotation = (0, -180, 0)
            mouse.locked = True

            self.level01.disable()
            self.level05.enable()

        def level06_menu():
            self.main_menu.disable()
            self.levels_menu.disable()
            self.player.enable()
            self.player.time_running = True
            self.player.position = (130, -120, 0)
            self.player.rotation = (0, -90, 0)
            mouse.locked = True

            self.level01.disable()
            self.level06.enable()

        def level07_menu():
            self.main_menu.disable()
            self.levels_menu.disable()
            self.player.enable()
            self.player.time_running = True
            self.player.position = (0, 10, 0)
            self.player.rotation = (0, 0, 0)
            mouse.locked = True

            self.level01.disable()
            self.level07.enable()

        def level08_menu():
            self.main_menu.disable()
            self.levels_menu.disable()
            self.player.enable()
            self.player.time_running = True
            self.player.position = (0, 10, 0)
            self.player.rotation = (0, 0, 0)
            mouse.locked = True

            self.level01.disable()
            self.level08.enable()

        def level09_menu():
            self.main_menu.disable()
            self.levels_menu.disable()
            self.player.enable()
            self.player.time_running = True
            self.player.position = (0, 10, 0)
            self.player.rotation = (0, 0, 0)
            mouse.locked = True

            self.level01.disable()
            self.level09.enable()

        def back():
            self.main_menu.enable()
            self.levels_menu.disable()

        title = Entity(model = "quad", scale = (0.8, 0.2, 0.2), texture = "parkour_logo_4", parent = self.main_menu, y = 0.3)

        start_button = Button(text = "S t a r t - G a m e", color = color.black, scale_y = 0.1, scale_x = 0.3, y = 0.02, parent = self.main_menu)
        levels_button = Button(text = "L e v e l s", color = color.black, scale_y = 0.1, scale_x = 0.3, y = -0.1, parent = self.main_menu)
        quit_button = Button(text = "Q u i t", color = color.black, scale_y = 0.1, scale_x = 0.3, y = -0.22, parent = self.main_menu)
        quit_button.on_click = application.quit
        start_button.on_click = Func(start)
        levels_button.on_click = Func(levels)

        level01 = Button(text = "L e v e l 0 1", color = color.black, scale_y = 0.1, scale_x = 0.3, y = 0.3, x = -0.5, parent = self.levels_menu)
        level02 = Button(text = "L e v e l 0 2", color = color.black, scale_y = 0.1, scale_x = 0.3, y = 0.3, x = 0, parent = self.levels_menu)
        level03 = Button(text = "L e v e l 0 3", color = color.black, scale_y = 0.1, scale_x = 0.3, y = 0.3, x = 0.5, parent = self.levels_menu)

        level04 = Button(text = "L e v e l 0 4", color = color.black, scale_y = 0.1, scale_x = 0.3, y = 0, x = -0.5, parent = self.levels_menu)
        level05 = Button(text = "L e v e l 0 5", color = color.black, scale_y = 0.1, scale_x = 0.3, y = 0, x = 0, parent = self.levels_menu)
        level06 = Button(text = "L e v e l 0 6", color = color.black, scale_y = 0.1, scale_x = 0.3, y = 0, x = 0.5, parent = self.levels_menu)

        level07 = Button(text = "L e v e l 0 7", color = color.black, scale_y = 0.1, scale_x = 0.3, y = -0.3, x = -0.5, parent = self.levels_menu)
        level08 = Button(text = "L e v e l 0 8", color = color.black, scale_y = 0.1, scale_x = 0.3, y = -0.3, x = 0, parent = self.levels_menu)
        level09 = Button(text = "L e v e l 0 9", color = color.black, scale_y = 0.1, scale_x = 0.3, y = -0.3, x = 0.5, parent = self.levels_menu)

        back_button = Button(text = "< - B a c k", color = color.gray, scale_y = 0.05, scale_x = 0.2, y = 0.45, x = -0.65, parent = self.levels_menu)

        level01.on_click = Func(level01_menu)
        level02.on_click = Func(level02_menu)
        level03.on_click = Func(level03_menu)
        level04.on_click = Func(level04_menu)
        level05.on_click = Func(level05_menu)
        level06.on_click = Func(level06_menu)
        level07.on_click = Func(level07_menu)
        level08.on_click = Func(level08_menu)
        level09.on_click = Func(level09_menu)

        back_button.on_click = Func(back)
