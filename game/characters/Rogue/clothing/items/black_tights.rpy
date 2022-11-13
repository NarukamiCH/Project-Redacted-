init -1 python:

    def Rogue_black_tights():
        name = "black tights"
        string = "black_tights"
        
        type = "hose"
        
        dialogue_lines = {}
        
        price = 65
        
        shame = 1
        
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
