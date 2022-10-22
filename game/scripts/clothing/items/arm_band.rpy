init -1 python:

    def arm_band(Owner):
        name = "arm band"
        string = "arm_band"

        type = "sleeves"

        dialogue_lines = {}

        price = 35

        shame = 0

        hides = []
        covers = []

        number_of_states = 1

        poses = ["standing"]

        incompatibilities = []

        return ClothingClass(Owner, name, string, type, dialogue_lines, price = price, shame = shame, hides = hides, covers = covers, number_of_states = number_of_states, poses = poses, incompatibilities = incompatibilities)
