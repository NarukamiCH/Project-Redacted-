init -1 python:

    def towel(Owner):
        name = "towel"
        string = "towel"

        type = "top"

        dialogue_lines = {}

        if Owner.tag == "Laura":
            dialogue_lines.update({
                "shopping": "I do need one.",
                "purchased": f"Thanks, {Owner.player_petname}.",
                "gift": "Thanks?",
                "change": "Okay. . ."})

        price = 50

        shame = 2

        hides = ["breasts", "pussy"]
        covers = ["breasts", "pussy"]

        number_of_states = 2

        poses = ["standing"]

        incompatibilities = ["bodysuit", "pants", "jacket"]

        return ClothingClass(Owner, name, string, type, dialogue_lines, price = price, shame = shame, hides = hides, covers = covers, number_of_states = number_of_states, poses = poses, incompatibilities = incompatibilities)
