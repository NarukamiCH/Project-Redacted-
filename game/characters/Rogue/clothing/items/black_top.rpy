init -1 python:

    def Rogue_black_top():
        name = "black top"
        string = "black_top"
        
        type = "top"
        
        dialogue_lines = {}
        
        price = 75
        
        shame = 1
        
        hides = ["breasts"]
        covers = ["breasts"]
        
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
