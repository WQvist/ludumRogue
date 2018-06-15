"""Gloval Gamesettings"""
class Settings():
    """A class to store our settings"""

    def __init__(self):
        # Screen settings
        self.screen_width = 640
        self.screen_height = 480

        # Character settings
        self.speed_factor = 4
        self.jump_factor = -13.37

        # Universal settings
        self.gravity = 0.3
