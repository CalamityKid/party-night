class Item:
    def __init__(self, name, identifiers, duration, use_text, active_item_text, effects_while_active, loading_item = False, loading_counter = None, loading_text = None):
        self.name = name
        self.identifiers = identifiers
        self.duration = duration
        self.use_text = use_text
        self.active_item_text = active_item_text
        self.loading_item = loading_item
        self.loading_text = loading_text
        self.effects_while_active = effects_while_active
    
    def __repr__(self):
        return self.name
    

def setupitems():
    lollipop = Item ("lollipop", ["lol"], 50, "You put the lollipop in your mouth", "You're sucking on the lollipop.", {mouth: 40, coolness: 10})
    soundcloud = Item ("Soundcloud", ["sound", "pill", "mdma"], 70, "You pop the pill",  "You can't help your body moving to the music. Soundcloud's coming up.", {high: 20, lit: 20, mouth: -20}, True, 20, "Soundcloud's still loading it seems.")




    "G": 40,             item_to_identify == "g"
            or "ghb" in item_to_identify
            or "chorr" in item_to_identify
G_text1 = "G still hasn't kicked in..."
G_text2 = "G's making you horny af."
        if "G" in player.active_items:  # For G
            if player.G_turn > 0:
                print(G_text1)
            if player.G_turn == 0:
                print(G_text2)
                player.high += 10
                player.mouth -= 10
                player.lit += 20




    "blunt": 40,             "blunt" in item_to_identify
            or "weed" in item_to_identify
            or "hash" in item_to_identify
blunt_text = "The blunt's buzzing in the background"
        if "blunt" in player.active_items:  # For blunt
            print(blunt_text)
            player.coolness += 10
            player.high += 10
            player.mouth -= 10
            player.lit += 10


    "cigarette": 20,   elif "cig" in item_to_identify:
cigarette_text = "You feel the nicotine."
        if "cigarette" in player.active_items:  # For cigarette
            print(cigarette_text)
            player.coolness += 20
            player.lit += 10
            player.high -= 20
            player.mouth -= 10


    "poppers": 20,  "popp"
poppers_text = "Hot damn, that rush huff was intense."
        if "poppers" in player.active_items:  # For poppers
            print(poppers_text)
            player.high += 10
            player.lit += 100



    "chewing gum": 40, "chew"
chewing_gum_text = "Gum's still minty fresh"
        if "chewing gum" in player.active_items:  # For chewing gum
            print(chewing_gum_text)
            player.mouth += 30




            