# config.py
class SoundConfig:
    def __init__(self):
        self.current_volume_music = 1.0
        self.current_volume_effect = 1.0
        self.volume_levels = {'mute': 0.0, 'low': 0.3, 'medium': 0.6, 'high': 1.0}

    def set_current_volume_effect(self, level):
        self.current_volume_effect = self.volume_levels[level]

    def set_current_volume_music(self, level):
        self.current_volume_music = self.volume_levels[level]

sound_config = SoundConfig()
