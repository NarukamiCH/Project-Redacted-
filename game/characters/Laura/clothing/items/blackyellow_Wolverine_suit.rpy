init -1 python:

    def Laura_blackyellow_Wolverine_suit():
        name = "black-and-yellow Wolverine suit"
        string = "blackyellow_Wolverine_suit"

        type = "bodysuit"

        dialogue_lines = {
            "shopping": "Yeah, this is awesome.",
            "purchased": f"Heh, thanks, {Laura.player_petname}.",
            "gift": f"Heh, thanks, {Laura.player_petname}.",
            "change": "It does kick ass, huh?"}

        price = 250

        shame = 0

        hides = ["breasts", "pussy"]
        covers = ["breasts", "pussy", "thighs"]

        number_of_states = 2

        poses = ["standing"]

        incompatibilities = []

        return ClothingClass(
            Laura, 
            name, string, type, 
            dialogue_lines, 
            price = price, shame = shame, 
            hides = hides, covers = covers, 
            number_of_states = number_of_states, poses = poses, 
            incompatibilities = incompatibilities)
