init -1 python:

    def Rogue_green_panties():
        name = "green panties"
        string = "green_panties"
        
        type = "underwear"
        
        dialogue_lines = {}
        
        price = 50
        
        shame = 0
        
        hides = []
        covers = ["pussy"]
        
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
