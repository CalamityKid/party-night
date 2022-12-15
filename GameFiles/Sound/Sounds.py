from playsound import playsound
import os

toop = "pat.wav"
tap = "cursor.wav"
end = "battleTurn.wav"
b_in = "breathein.wav"
b_out = "breatheout.wav"


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


def play_in():
    play_sound(b_in)


def play_out():
    play_sound(b_out)


def play_in_or_out(zero_or_one):
    """takes a 0 or 1, plays in if 0, plays out if 1"""
    if zero_or_one == 0:
        play_in()
    elif zero_or_one == 1:
        play_out()
