init -1 python:

    def Rogue_green_bikini_top():
        name = "green bikini top"
        string = "green_bikini_top"
        
        type = "bra"
        
        dialogue_lines = {}
        
        price = 70
        
        shame = 0
        
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
