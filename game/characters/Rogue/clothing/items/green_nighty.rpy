init -1 python:

    def Rogue_green_nighty():
        name = "green nighty"
        string = "green_nighty"
        
        type = "dress"
        
        dialogue_lines = {}
        
        price = 150
        
        shame = 2
        
        hides = ["breasts"]
        covers = ["breasts", "pussy"]
        
        number_of_states = 2
        
        poses = ["standing"]
        
        incompatibilities = ["belt", "jacket"]
        
        return ClothingClass(
            Rogue, 
            name, string, type, 
            dialogue_lines, 
            price = price, shame = shame, 
            hides = hides, covers = covers, 
            number_of_states = number_of_states, poses = poses, 
            incompatibilities = incompatibilities)
