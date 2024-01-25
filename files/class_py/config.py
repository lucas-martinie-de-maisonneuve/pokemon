# config.py
import pygame

# Variables globales pour les effets sonores
confirmation_sound = pygame.mixer.Sound('files/song/confirm_button.mp3')
confirmation_enabled = True
volume_levels = {
    'mute': 0.0,
    'low': 0.2,
    'medium': 0.5,
    'high': 1.0
}
current_volume = 'high'

# Variables globales pour la musique
background_music = pygame.mixer.music.load('files/song/opening.mp3')
music_enabled = True
music_volume = 0.5

def play_confirmation_sound():
    if confirmation_enabled and confirmation_sound:
        volume = volume_levels[current_volume]
        confirmation_sound.set_volume(volume)
        confirmation_sound.play()

def set_volume_level(volume_option):
    if volume_option in volume_levels:
        global current_volume
        current_volume = volume_option

def toggle_confirmation():
    global confirmation_enabled
    confirmation_enabled = not confirmation_enabled

def play_background_music():
    if music_enabled:
        pygame.mixer.music.set_volume(music_volume)
        pygame.mixer.music.play(-1)  # -1 pour la répétition infinie

def set_music_volume(volume):
    global music_volume
    music_volume = volume
    pygame.mixer.music.set_volume(volume)

def toggle_music():
    global music_enabled
    music_enabled = not music_enabled
    if music_enabled:
        play_background_music()
    else:
        pygame.mixer.music.stop()
