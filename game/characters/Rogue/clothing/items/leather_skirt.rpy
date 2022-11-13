init -1 python:

    def Rogue_leather_skirt():
        name = "leather skirt"
        string = "leather_skirt"
        
        type = "skirt"
        
        dialogue_lines = {}
        
        price = 85
        
        shame = 0
        
        hides = ["pussy"]
        covers = ["pussy", "thighs"]
        
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
