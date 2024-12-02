import pygame as pg

class Settings:
    def __init__(self):
        screen_info = pg.display.Info()
        self.screen_width = 1400  # Set the screen width to 800 pixels
        self.screen_height = 800  # Set the screen height to 600 pixels
        self.bg_color = (230, 230, 230)
        self.flag = pg.RESIZABLE

        # Initialize static settings
        self.apples_allowed = 3
        self.apple_limit = 3
        self.game_over = False

        # Scoring
        self.apple_points = 2

        # Levelup Scale
        self.levelup_scale = 1.1

        self.initialize_dynamic_settings()

    def initialize_dynamic_settings(self):
        self.basket_speed = 7
        self.apple_drop_speed = 2

    def increase_speed(self):
        self.basket_speed *= self.levelup_scale
        self.apple_drop_speed *= self.levelup_scale