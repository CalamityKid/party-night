from ...Scripts.Blocks.SceneSc import Scene
from .Tanktop0 import tanktoptimes0content
from .Tanktop1 import tanktoptimes1content
from .Tanktop2 import tanktoptimes2content
from .Tanktop3 import tanktoptimes3content
from .Tanktop4 import tanktoptimes4content
from .Tanktop5 import tanktoptimes5content
from .TanktopFlirt import tanktopflirtcontent


def assemble_tanktop_scenes():
    times0 = Scene("Times0", tanktoptimes0content)
    times1 = Scene("Times1", tanktoptimes1content)
    times2 = Scene("Times2", tanktoptimes2content)
    times3 = Scene("Times3", tanktoptimes3content)
    times4 = Scene("Times4", tanktoptimes4content)
    times5 = Scene("Times4", tanktoptimes5content)
    tanktopflirt = Scene("TanktopFlirt", tanktopflirtcontent)

    return {
        "Times0": times0,
        "Times1": times1,
        "Times2": times2,
        "Times3": times3,
        "Times4": times4,
        "Times5": times5,
        "TanktopFlirt": tanktopflirt,
    }


tanktopscenes = assemble_tanktop_scenes()
