import pygame

def load_sounds():
    hit_sound = pygame.mixer.Sound("assets/mixkit-game-ball-tap-2073.wav")
    score_sound = pygame.mixer.Sound("assets/mixkit-arcade-score-interface-217.wav")
    bg_music = pygame.mixer.Sound("assets/music.mp3")

    hit_sound.set_volume(0.5)
    score_sound.set_volume(0.5)
    bg_music.set_volume(0.3)

    return hit_sound, score_sound, bg_music

def play_background_music(bg_music):
    bg_music.play(-1)  # Loop forever
