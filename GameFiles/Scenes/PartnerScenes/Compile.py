from ...Scripts.Blocks.SceneSc import Scene
from .PartnerTanktop0 import partnertanktoptimes0content
from .Partner0 import partnertimes0content
from .Partner1 import partnertimes1content
from .Partner2 import partnertimes2content
from .PartnerBank import partnerbankcontent
from .PartnerGather0 import partnergather0content
from .PartnerGather1 import partnergather1content


def assemble_partner_scenes():
    # times0 = Scene("Times0", russiantimes0content)

    times0 = Scene("Times0", partnertimes0content)
    times1 = Scene("Times1", partnertimes1content)
    times2 = Scene("Times2", partnertimes2content)
    gather0 = Scene("Gather0", partnergather0content)
    gather1 = Scene("Gather1", partnergather1content)
    partnerbank = Scene("PartnerBank", partnerbankcontent)

    partnertanktop0 = Scene("PartnerTanktop0", partnertanktoptimes0content)

    return {
        "Times0": times0,
        "Times1": times1,
        "Times2": times2,
        "Gather0": gather0,
        "Gather1": gather1,
        "PartnerBank": partnerbank,
        "PartnerTanktop0": partnertanktop0,
    }


partnerscenes = assemble_partner_scenes()
