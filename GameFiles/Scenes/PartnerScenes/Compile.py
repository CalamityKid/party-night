from ...Scripts.Blocks.SceneSc import Scene
from .PartnerTanktop0 import partnertanktoptimes0content
from .Partner0 import partnertimes0content


def assemble_partner_scenes():
    # times0 = Scene("Times0", russiantimes0content)

    times0 = Scene("Times0", partnertimes0content)
    partnertanktop0 = Scene("PartnerTanktop0", partnertanktoptimes0content)

    return {
        "Times0": times0,
        "PartnerTanktop0": partnertanktop0,
    }


partnerscenes = assemble_partner_scenes()
