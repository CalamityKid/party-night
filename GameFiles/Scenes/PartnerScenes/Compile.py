from ...Scripts.Blocks.SceneSc import Scene
from .PartnerTanktop0 import partnertantoptimes0content


def assemble_partner_scenes():
    # times0 = Scene("Times0", russiantimes0content)

    partnertanktop0 = Scene("PartnerTanktop0", partnertantoptimes0content)

    return {
        "PartnerTanktop0": partnertanktop0,
    }


partnerscenes = assemble_partner_scenes()
