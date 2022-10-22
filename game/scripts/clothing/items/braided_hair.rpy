init -1 python:

    def braided_hair(Owner):
        name = "braided hair"
        string = "braided"

        type = "hair"

        dialogue_lines = {}

        price = 0

        shame = 0

        hides = []
        covers = []

        number_of_states = 1

        poses = ["standing"]

        incompatibilities = []

        return ClothingClass(Owner, name, string, type, dialogue_lines, price = price, shame = shame, hides = hides, covers = covers, number_of_states = number_of_states, poses = poses, incompatibilities = incompatibilities)
