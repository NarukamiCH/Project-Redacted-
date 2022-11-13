init -1 python:

    def Rogue_black_gloves():
        name = "black gloves"
        string = "black_gloves"
        
        type = "gloves"
        
        dialogue_lines = {}
        
        price = 35
        
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
