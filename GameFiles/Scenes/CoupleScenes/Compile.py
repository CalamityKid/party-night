from ...Scripts.Blocks.SceneSc import Scene
from .Couple0 import coupletimes0content
from .Couple1 import coupletimes1content
from .Couple2 import coupletimes2content
from .Couple3 import coupletimes3content
from .Couple4 import coupletimes4content
from .Couple5 import coupletimes5content
from .CoupleGum import coupleGumcontent
from .CoupleLeave import coupleleavescontent


def assemble_couple_scenes():
    times0 = Scene("Times0", coupletimes0content)
    times1 = Scene("Times1", coupletimes1content)
    times2 = Scene("Times2", coupletimes2content)
    times3 = Scene("Times3", coupletimes3content)
    times4 = Scene("Times4", coupletimes4content)
    times5 = Scene("Times4", coupletimes5content)
    couplegum = Scene("CoupleGum", coupleGumcontent)
    coupleleaves = Scene("CoupleLeaves", coupleleavescontent)

    return {
        "Times0": times0,
        "Times1": times1,
        "Times2": times2,
        "Times3": times3,
        "Times4": times4,
        "Times5": times5,
        "CoupleGum": couplegum,
        "CoupleLeaves": coupleleaves,
    }


couplescenes = assemble_couple_scenes()
