init -1 python:

    def Item():
        name = "lace panties"
        string = "lace_panties"

        type = "underwear"

        dialogue_lines = {
            "shopping": "Ooh, these are cute!",
            "purchased": f"Aw, that's sweet of you, {Girl.player_petname}.",
            "gift": f"Thank you, {Girl.player_petname}!",
            "change": "I do look good in those, don't I?"}

        price = 50

        shame = 1

        hides = ["pussy"]
        covers = ["pussy"]

        number_of_states = 1

        poses = ["standing", "blowjob", "sex", "doggy"]

        incompatibilities = []

        return ClothingClass(
            Girl, 
            name, string, type, 
            dialogue_lines, 
            price = price, shame = shame, 
            hides = hides, covers = covers, 
            number_of_states = number_of_states, poses = poses, 
            incompatibilities = incompatibilities)
