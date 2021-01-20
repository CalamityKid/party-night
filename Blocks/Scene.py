class Scene:
    def __init__(self, sceneName, actor, content=None, actor2=None, has_run=False):
        self.sceneName = sceneName
        self.content = content
        self.has_run = has_run
        self.actor = actor
        self.actor2 = actor2

    def __repr__(self):
        return "Scene: " + str(self.sceneName)

    def run_scene(self):
        self.content(self.actor)
        self.has_run = True


class SceneVariables:
    def __init__(self, stalltimewarning=False, movementtimewarning=False):
        self.stalltimewarning = stalltimewarning
        self.movementtimewarning = movementtimewarning

    def __repr__(self):
        return "Scene Variables"