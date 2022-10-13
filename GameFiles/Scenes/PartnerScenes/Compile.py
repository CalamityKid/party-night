from ...Scripts.Blocks.SceneSc import Scene
from .PartnerTanktop0 import partnertanktoptimes0content
from .Partner0 import partnertimes0content
from .Partner1 import partnertimes1content
from .Partner2 import partnertimes2content
from .Partner3 import partnertimes3content
from .Partner4 import partnertimes4content
from .PartnerBank import partnerbankcontent
from .PartnerTanktop0 import partnertanktoptimes0content
from .PartnerTanktop5 import partnertanktop5content
from .PartnerGather0 import partnergather0content
from .PartnerGather1 import partnergather1content
from .PartnerWater import partnerwatercontent
from .PartnerAnxiety import partneranxietycontent
from .PartnerCrowd import partnercrowdcontent
from .PartnerMusic import partnermusiccontent
from .PartnerTanktop5 import partnertanktop5content
from .baltri import baltricontent


def assemble_partner_scenes():
    # times0 = Scene("Times0", russiantimes0content)

    times0 = Scene("Times0", partnertimes0content)
    times1 = Scene("Times1", partnertimes1content)
    times2 = Scene("Times2", partnertimes2content)
    times3 = Scene("Times3", partnertimes3content)
    times4 = Scene("Times4", partnertimes4content)
    gather0 = Scene("Gather0", partnergather0content)
    gather1 = Scene("Gather1", partnergather1content)
    partnertanktop0 = Scene("PartnerTanktop0", partnertanktoptimes0content)
    partnertanktop5 = Scene("PartnerTanktop5", partnertanktop5content)
    partnerbank = Scene("PartnerBank", partnerbankcontent)
    partnerwater = Scene("PartnerWater", partnerwatercontent)
    partneranxiety = Scene("PartnerAnxiety", partneranxietycontent)
    partnermusic = Scene("PartnerMusic", partnermusiccontent)
    partnercrowd = Scene("PartnerCrowd", partnercrowdcontent)

    partnertanktop0 = Scene("PartnerTanktop0", partnertanktoptimes0content)
    partnertanktop5 = Scene("PartnerTantop5", partnertanktop5content)
    baltri = Scene("Baltri", baltricontent)

    return {
        "Times0": times0,
        "Times1": times1,
        "Times2": times2,
        "Times3": times3,
        "Times4": times4,
        "Gather0": gather0,
        "Gather1": gather1,
        "PartnerBank": partnerbank,
        "PartnerTanktop0": partnertanktop0,
        "PartnerTanktop5": partnertanktop5,
        "PartnerWater": partnerwater,
        "PartnerAnxiety": partneranxiety,
        "PartnerMusic": partnermusic,
        "PartnerCrowd": partnercrowd,
        "Baltri": baltri,
    }


partnerscenes = assemble_partner_scenes()
