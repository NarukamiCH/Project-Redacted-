init -1 python:

    def Rogue_black_garterbelt():
        name = "black garterbelt"
        string = "black_garterbelt"
        
        type = "hose"
        
        dialogue_lines = {}
        
        price = 80
        
        shame = 1
        
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
