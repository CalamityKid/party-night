from ...Scripts.Blocks.ItemsSc import items

bad_no_item_string = "you might need some chemical help because"

bad_bark_item_string_dict = {
    items["lollipop"]: "you do a lollipop thing but end up looking silly and ",
    items["Soundcloud"]: "you start rambling and",
    items["G"]: "your tongue goes slower than your brain,",
    items["blunt"]: "you space out and",
    items["cigarette"]: "maybe it's bad breath but",
    items["poppers"]: "you're still a bit lightheaded so",
    items["chewing gum"]: "you kinda fumble with the gum and",
    items["special K"]: "you're a bit absent minded,",
    items["coke"]: "you're a bit too alert, twitchy even,",
}

bad_bark_room_string_dict = {
    "the smoking room": "you're not feeling the vibe in here and",
    "the bathroom": "it might be the being in a bathroom thing but",
    "the dance floor": "the music gets in the way of your delivery and",
}
bad_bark_stats_string_dict = {
    0: "you feel a bit self conscious and",
    1: "you try but you don't really feel it and",
    2: "your brain isn't doing its best work atm so",
}

bad_ending_string_dict = {
    0: " it doesn't go well, it's a bit embarrasing.",
    1: " you're really off the mark this time, it's pretty bad.",
    2: " it doesn't land very well. Oof.",
    3: " you make a fool of yourself.",
    4: " you sound really dumb. Not good.",
}
