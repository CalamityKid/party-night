from random import randint

intro_text = """
You're not super excited to play this game.
Because it doesn't have any visuals.
But mostly because Joel is making you play.
Probably you'd rather be doing something else.
But here we are so.
Yeah.
What's your name?
"""

intro_text2 = """
Okay {name}. I don't wanna be here either.
But humor him for a bit.
"""

intro_text3 = """
Because this is text, I can write anything 
and you, {name}, have to pretend like it's real. 
Like, it's just words. Letters.
No visuals, no sound. 
I mean, no budget too, you know.
Life's hard.
He's doing his best though.
Well, not his BEST, but you now what I mean"""

intro_text4 = """
So, yeah, the plot is...
....You, {name}, are like dancing and being cool af
in a club full of super hot people. 
This is pre COVID 19, of course.
Or post COVID, whatever, point is, everybody's
having  blast,
dancing together, sweaty. 
Like the Slave 4 U video.

And you see them walk in. 
Your Archnemesis. 
That bitch.
Trying to outshine you every single time.
What was their name again?"""

tutorial_text = """

TUTORIAL -- THIS IS HOW YOU PLAY THE GAME

Whenever you want to do an action
you'll see some [ACTION] words in brackets,
you type that down, just that word
watch your spelling, NO NEED TO USE CAPS THO

For example if you wanna talk to someone a room and 
you see that it says [TALK]
you can write "talk", or TALK or TaLK 

And you'll talk.

With ITEMS and PEOPLE just write the item or the person
doesn't have to be the whole thing

For example if it says "your partner", or "Valentina, Queen of Hearts"
you can just write partner or valentina

You can write "Tutorial" as an action to read this again.

"""
line = """

"""

space = """








"""

Soundcloud_text1 = "Soundcloud's still loading it seems."

Soundcloud_text2 = (
    "You can't help your body moving to the music. Soundcloud's coming up."
)

lollipop_text = "You're sucking on the lollipop."
blunt_text = "The blunt's buzzing in the background"
cigarette_text = "You feel the nicotine."
poppers_text = "Hot damn, that rush huff was intense."
G_text1 = "G still hasn't kicked in..."
G_text2 = "G's making you horny af."
chewing_gum_text = "Gum's still minty fresh"


def body_check_opener():  ##Random opening statement before body check
    print(" ")
    op = randint(0, 9)
    if op == 0:
        print("This is what's up now:")
    elif op == 1:
        print("This is what's popping:")
    elif op == 2:
        print("The lay of the land:")
    elif op == 3:
        print("Latest updates:")
    elif op == 4:
        print("Current party situation:")
    elif op == 5:
        print("STATUS:")
    elif op == 6:
        print("You connect to your inner being:")
    elif op == 7:
        print("You listen to your body:")
    elif op == 8:
        print("SITUATION REPORT:")
    elif op == 9:
        print("What had happened was:")


#####TO DO. "ask dj to change music", add TIME, program actions and interactions.
