init -1 python:

    def Laura_black_swimsuit():
        name = "black swimsuit"
        string = "black_swimsuit"

        type = "bodysuit"

        dialogue_lines = {
            "shopping": "Like this one?",
            "purchased": f"That's. . . actually pretty nice, {Laura.player_petname}.",
            "gift": f"That's. . . actually pretty nice, {Laura.player_petname}.",
            "change": "You think it's cute?"}

        price = 100

        shame = 0

        hides = ["breasts", "pussy"]
        covers = ["breasts", "pussy"]

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
