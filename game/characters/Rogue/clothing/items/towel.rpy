init -1 python:

    def Rogue_towel():
        name = "towel"
        string = "towel"

        type = "dress"

        dialogue_lines = {}

        price = 50

        shame = 2

        hides = ["breasts", "pussy"]
        covers = ["breasts", "pussy"]

        number_of_states = 2

        poses = ["standing"]

        incompatibilities = ["top", "belt"]

        return ClothingClass(
            Rogue, 
            name, string, type, 
            dialogue_lines, 
            price = price, shame = shame, 
            hides = hides, covers = covers, 
            number_of_states = number_of_states, poses = poses, 
            incompatibilities = incompatibilities)
