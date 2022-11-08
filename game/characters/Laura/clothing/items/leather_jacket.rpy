init -1 python:

    def Laura_leather_jacket():
        name = "leather jacket"
        string = "leather_jacket"

        type = "jacket"

        dialogue_lines = {
            "shopping": "Think I'd look good in this?",
            "purchased": f"That's nice of you, {Laura.player_petname}.",
            "gift": "Oh, I like it.",
            "change": "Sure."}

        price = 150

        shame = 0

        hides = []
        covers = ["breasts"]

        number_of_states = 1

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
