init -1 python:

    def Rogue_black_tanktop():
        name = "black tanktop"
        string = "black_tanktop"
        
        type = "bra"
        
        dialogue_lines = {}
        
        price = 50
        
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
