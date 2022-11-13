init -1 python:

    def Rogue_Rogue_belt():
        name = "Rogue belt"
        string = "Rogue_belt"
        
        type = "belt"
        
        dialogue_lines = {}
        
        price = 80
        
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
