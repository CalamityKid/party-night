class Scene:
    def __init__(self, sceneName, content=None, has_run=False):
        self.sceneName = sceneName
        self.content = content
        self.has_run = has_run

    def __repr__(self):
        return "Scene: " + str(self.sceneName)

    def run_scene(self, actor):
        self.has_run = True
        return self.content(actor)


class SceneVariables:
    def __init__(
        self,
        stalltimewarning=False,
        movementtimewarning=False,
        popper_counter=0,
        capeohour=00,
        capeominute=00,
    ):
        self.stalltimewarning = stalltimewarning
        self.movementtimewarning = movementtimewarning
        self.popper_counter = popper_counter
        self.capeohour = capeohour
        self.capeominute = capeominute

    def __repr__(self):
        return "Scene Variables"


scenevariables = SceneVariables()
