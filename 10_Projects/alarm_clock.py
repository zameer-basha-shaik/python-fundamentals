# Alaram Clock Using Python (24 hours time)
import time
import datetime
from pathlib import Path
import pygame


def set_alaram(set_time):
    print(f"Alarm is set for {set_time}")

    sound_file = Path(__file__).resolve().parent.parent / "resources" / "audio.mpeg"

    is_running = True
    while is_running:

        current_time = datetime.datetime.now().strftime("%H:%M:%S")
        if current_time == set_time:
            print("Wake Up!!!!!!")
            pygame.mixer.init()
            pygame.mixer.music.load(str(sound_file))
            pygame.mixer.music.play()
            while pygame.mixer.music.get_busy():
                time.sleep(1)

            is_running = False
        print(current_time)
        time.sleep(1)


if __name__ == "__main__":
    set_time = input("Enter the time to set alaram(HH:MM:SS): ")
    set_alaram(set_time)