init -1 python:

    def Rogue_black_lace_panties():
        name = "black lace panties"
        string = "black_lace_panties"
        
        type = "underwear"
        
        dialogue_lines = {}
        
        price = 70
        
        shame = 2
        
        hides = ["pussy"]
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
