def yesorno():
    yesornoresult = None
    while yesornoresult == None:
        yesornoresult = input()
        if len(yesornoresult) > 0:
            yesornoresult = yesornoresult.lower()
            if "y" in yesornoresult[0]:
                return True
            if "n" in yesornoresult[0]:    
                return False
            else:
                print ("(yes or no):", end = " ")
                yesornoresult = None

input()
var = yesorno()
print (var)

var = yesorno()
print (var)