init -1 python:

    def Daenerys_wet_hair():
        name = "wet hair"
        string = "wet"
        
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
            Daenerys, 
            name, string, type, 
            dialogue_lines, 
            price = price, shame = shame, 
            hides = hides, covers = covers, 
            number_of_states = number_of_states, poses = poses, 
            incompatibilities = incompatibilities)
