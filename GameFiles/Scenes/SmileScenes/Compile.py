from ...Scripts.Blocks.SceneSc import Scene
from .Smile0 import smiletimes0content

__all__ = ["Smile0", "Smile1", "Smile2", "SmileG"]


def assemble_smile_scenes():
    times0 = Scene("Times0", smiletimes0content)

    return {
        "Times0": times0,
    }


smilescenes = assemble_smile_scenes()
