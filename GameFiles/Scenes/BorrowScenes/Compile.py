from ...Scripts.Blocks.SceneSc import Scene
from .RussianPoppers import russianpopperscontent
from .SmileG import smileGcontent


def assemble_borrow_scenes():
    # times0 = Scene("Times0", russiantimes0content)

    russianpoppers = Scene("RussianPoppers", russianpopperscontent)
    smileG = Scene("SmileG", smileGcontent)

    return {
        "your russian friend": russianpoppers,
        "the smile ambassador": smileG,
    }


item_redirect = {
    "a bottle of poppers": "your russian friend",
    "G": "the smile ambassador",
}
borrow_scenes = assemble_borrow_scenes()
