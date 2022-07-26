from ...Scripts.Blocks.SceneSc import Scene
from .Pusher0 import pushertimes0content
from .Pusher1 import pushertimes1content


def assemble_pusher_scenes():
    times0 = Scene("Times0", pushertimes0content)
    times1 = Scene("Times1", pushertimes1content)

    return {
        "Times0": times0,
        "Times1": times1,
    }


pusherscenes = assemble_pusher_scenes()
