from ...Scripts.Blocks.SceneSc import Scene
from .Russian0 import russiantimes0content
from .Russian1 import russiantimes1content
from .Russian2 import russiantimes2content
from .Russian3 import russiantimes3content
from .Russian4 import russiantimes4content
from .Russian5 import russiantimes5content


def assemble_russian_scenes():
    times0 = Scene("Times0", russiantimes0content)
    times1 = Scene("Times1", russiantimes1content)
    times2 = Scene("Times2", russiantimes2content)
    times3 = Scene("Times3", russiantimes3content)
    times4 = Scene("Times4", russiantimes4content)
    times5 = Scene("Times4", russiantimes5content)

    return {
        "Times0": times0,
        "Times1": times1,
        "Times2": times2,
        "Times3": times3,
        "Times4": times4,
        "Times5": times5,
    }


russianscenes = assemble_russian_scenes()
