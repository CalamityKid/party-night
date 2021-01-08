class Scene:
    def __init__(self, sceneName, content=None, has_run=False):
        self.sceneName = sceneName
        self.content = content
        self.has_run = has_run

    
    def __repr__(self):
        return "Scene: " + str(self.sceneName)

    def run_scene(self):
        self.content()
        self.has_run = True
        Battle.update_room()
        if player.gameover == False:
            Battle.choose_action()

def SmileTimes0code ():
    print ("We haven't partied in so long, it's about time we had some real, like, with people fun.")
    print ("And I am ready. to. party.")
    print("They open up this huge fan. Like a hand fan. Makes a loud ass noise.")
    print("It's the signature smile ambassador party fan.")
    smile.times_talked = 1

SmileTimes0 = Scene ("SmileTimes0", SmileTimes0code)