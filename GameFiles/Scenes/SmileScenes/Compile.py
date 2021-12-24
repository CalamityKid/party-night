from ...Scripts.Blocks.SceneSc import Scene
from .Smile0 import smiletimes0content
from .Smile1 import smiletimes1content
from .Smile2 import smiletimes2content
from .Smile3 import smiletimes3content
from .Smile4 import smiletimes4content
from .Smile5 import smiletimes5content


def assemble_smile_scenes():
    times0 = Scene("Times0", smiletimes0content)
    times1 = Scene("Times1", smiletimes1content)
    times2 = Scene("Times2", smiletimes2content)
    times3 = Scene("Times3", smiletimes3content)
    times4 = Scene("Times4", smiletimes4content)
    times5 = Scene("Times4", smiletimes5content)

    return {
        "Times0": times0,
        "Times1": times1,
        "Times2": times2,
        "Times3": times3,
        "Times4": times4,
        "Times5": times5,
    }


smilescenes = assemble_smile_scenes()
