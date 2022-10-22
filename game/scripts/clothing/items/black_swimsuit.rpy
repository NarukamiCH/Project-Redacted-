init -1 python:

    def black_swimsuit(Owner):
        name = "black swimsuit"
        string = "black_swimsuit"

        type = "bodysuit"

        dialogue_lines = {}

        if Owner.tag == "Laura":
            dialogue_lines.update({
                "shopping": "Like this one?",
                "purchased": f"That's. . . actually pretty nice, {Owner.player_petname}.",
                "gift": f"That's. . . actually pretty nice, {Owner.player_petname}.",
                "change": "You think it's cute?"})

        price = 100

        shame = 0

        hides = ["breasts", "pussy"]
        covers = ["breasts", "pussy"]

        number_of_states = 2

        poses = ["standing"]

        incompatibilities = []

        return ClothingClass(Owner, name, string, type, dialogue_lines, price = price, shame = shame, hides = hides, covers = covers, number_of_states = number_of_states, poses = poses, incompatibilities = incompatibilities)
