init -1 python:

    def Rogue_green_mesh_top():
        name = "green mesh top"
        string = "green_mesh_top"
        
        type = "top"
        
        dialogue_lines = {}
        
        price = 50
        
        shame = 1
        
        hides = []
        covers = ["breasts"]
        
        number_of_states = 1
        
        poses = ["standing"]
        
        incompatibilities = ["jacket"]
        
        return ClothingClass(
            Rogue, 
            name, string, type, 
            dialogue_lines, 
            price = price, shame = shame, 
            hides = hides, covers = covers, 
            number_of_states = number_of_states, poses = poses, 
            incompatibilities = incompatibilities)
