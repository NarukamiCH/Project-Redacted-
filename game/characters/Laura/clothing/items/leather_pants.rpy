init -1 python:

    def Laura_leather_pants():
        name = "leather pants"
        string = "leather_pants"

        type = "pants"

        dialogue_lines = {
            "shopping": "Huh, these look cool.",
            "purchased": f"Thanks, {Laura.player_petname}, these are nice.",
            "gift": "Oh, thanks.",
            "change": "Cool."}

        price = 150

        shame = 0

        hides = ["pussy"]
        covers = ["pussy", "thighs"]

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
