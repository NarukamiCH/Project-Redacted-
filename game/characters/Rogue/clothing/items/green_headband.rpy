init -1 python:

    def Rogue_green_headband():
        name = "green headband"
        string = "green_headband"
        
        type = "face_inner_accessory"
        
        dialogue_lines = {}
        
        price = 15
        
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
