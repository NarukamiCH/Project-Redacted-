init -1 python:

    def Rogue_spiked_collar():
        name = "spiked collar"
        string = "spiked_collar"
        
        type = "neck"
        
        dialogue_lines = {}
        
        price = 45
        
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
