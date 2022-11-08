init -1 python:

    def Jean_towel():
        name = "towel"
        string = "towel"

        type = "top"

        dialogue_lines = {}

        price = 50

        shame = 2

        hides = ["breasts", "pussy"]
        covers = ["breasts", "pussy"]

        number_of_states = 2

        poses = ["standing"]

        incompatibilities = []

        return ClothingClass(
            Jean, 
            name, string, type, 
            dialogue_lines, 
            price = price, shame = shame, 
            hides = hides, covers = covers, 
            number_of_states = number_of_states, poses = poses, 
            incompatibilities = incompatibilities)
