init -1 python:

    def Rogue_black_stockings():
        name = "black stockings"
        string = "black_stockings"
        
        type = "socks"
        
        dialogue_lines = {}
        
        price = 35
        
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
