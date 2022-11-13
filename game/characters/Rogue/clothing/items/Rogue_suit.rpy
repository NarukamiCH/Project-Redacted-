init -1 python:

    def Rogue_Rogue_suit():
        name = "Rogue suit"
        string = "Rogue_suit"

        type = "bodysuit"

        dialogue_lines = {}

        price = 225

        shame = 0

        hides = ["breasts", "pussy"]
        covers = ["breasts", "pussy", "thighs"]

        number_of_states = 1

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
