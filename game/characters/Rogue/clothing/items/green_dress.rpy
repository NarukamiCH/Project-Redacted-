init -1 python:

    def Rogue_green_dress():
        name = "green dress"
        string = "green_dress"
        
        type = "dress"
        
        dialogue_lines = {}
        
        price = 125
        
        shame = 1
        
        hides = ["breasts", "pussy"]
        covers = ["breasts", "pussy"]
        
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
