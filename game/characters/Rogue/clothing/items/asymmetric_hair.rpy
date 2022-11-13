init -1 python:

    def Rogue_asymmetric_hair():
        name = "asymmetric hair"
        string = "asymmetric"
        
        type = "hair"
        
        dialogue_lines = {}
        
        price = 0
        
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
