init -1 python:

    def long_hair(Owner):
        name = "long hair"
        string = "long_hair"

        type = "hair"

        dialogue_lines = {}

        if Owner.tag == "Laura":
            dialogue_lines.update({
                "shopping": None,
                "purchased": None,
                "gift": None,
                "change": "Okay."})

        price = 0

        shame = 0

        hides = []
        covers = []

        number_of_states = 1

        poses = ["standing"]

        incompatibilities = []

        return ClothingClass(Owner, name, string, type, dialogue_lines, price = price, shame = shame, hides = hides, covers = covers, number_of_states = number_of_states, poses = poses, incompatibilities = incompatibilities)
