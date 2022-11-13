init -1 python:

    def Rogue_yellow_boots():
        name = "yellow boots"
        string = "yellow_boots"
        
        type = "boots"
        
        dialogue_lines = {}

        price = 75

        shame = 0

        hides = []
        covers = []

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
