from random import randint


def body_check_bark():  ##Random opening statement before body check
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
