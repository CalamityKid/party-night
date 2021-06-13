from .Scripts.Blocks.TimeSc import time
from .Scripts.Blocks.PartySc import party


def update_schedule ():
################ CROWDS #############
    if time.hour < 1 or time.hour > 5:
        party.change_crowd_empty()
    elif time.hour == 1 or time.hour == 4:
        party.change_crowd_half()
    elif time.hour == 2 or time.hour == 3:
        party.change_crowd_full()
################## Music ############# Must get the exception of the cutscne thingy
    if time.hour < 1 or time.hour == 2:
        party.change_music_ok()
    elif time.hour == 1 or (time.hour == 3 and time.minutes < 30):
        #if variable for music changed is FALSE:
        party.change_music_terrible()
        #otherwise make music amazing
    elif time.hour > 5:
        party.change_music_great()

