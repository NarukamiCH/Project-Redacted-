init -1 python:

    def Rogue_brown_jacket():
        name = "brown jacket"
        string = "brown_jacket"

        type = "jacket"

        dialogue_lines = {}

        price = 150

        shame = 0

        hides = ["breasts"]
        covers = ["breasts"]

        number_of_states = 2

        poses = ["standing"]

        incompatibilities = []

        return ClothingClass(
            Rogue, 
            name, string, type, 
            dialogue_lines, 
            price = price, shame = shame, 
            hides = hides, covers = covers, 
            number_of_states = number_of_states, poses = poses, 
            incompatibilities = incompatibilities)
