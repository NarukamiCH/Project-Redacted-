init -1 python:

    def Laura_towel():
        name = "towel"
        string = "towel"

        type = "dress"

        dialogue_lines = {
            "shopping": "I do need one.",
            "purchased": f"Thanks, {Laura.player_petname}.",
            "gift": "Thanks?",
            "change": "Okay. . ."}

        price = 50

        shame = 2

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
