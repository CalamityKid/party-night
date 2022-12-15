from playsound import playsound
import os

toop = "pat.wav"
tap = "cursor.wav"
end = "battleTurn.wav"


def play_sound(sound):
    absolute_path = os.path.dirname(__file__)
    sounddir = sound
    full_path = os.path.join(absolute_path, sounddir)
    playsound(full_path)


def play_toop():
    play_sound(toop)


def play_tap():
    play_sound(tap)


def play_end():
    play_sound(end)
