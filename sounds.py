import pygame
import os

# Initialize pygame mixer
pygame.mixer.init()

# Path to the folder containing your sound files
SOUNDS_DIR = os.path.join(os.path.dirname(__file__), "sounds")

def play_sound(sound_file):
    """
    Play a sound from the 'sounds' folder.

    sound_file: filename with extension (e.g. "archivo.mp3", "sound.mp3")
    """
    try:
        full_path = os.path.join(SOUNDS_DIR, sound_file)
        if not os.path.isfile(full_path):
            print(f"Sound file not found: {full_path}")
            return

        sound = pygame.mixer.Sound(full_path)
        sound.play()
    except Exception as e:
        print(f"Error playing sound '{sound_file}': {e}")
