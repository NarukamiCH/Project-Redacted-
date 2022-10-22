init -1 python:

    def cloth_bra(Owner):
        name = "cloth bra"
        string = "cloth_bra"
        
        type = "bra"
        
        dialogue_lines = {}
        
        price = 60
        
        shame = 1
        
        hides = ["breasts"]
        covers = ["breasts"]
        
        number_of_states = 2
        
        poses = ["standing"]
        
        incompatibilities = []
        
        return ClothingClass(Owner, name, string, type, dialogue_lines, price = price, shame = shame, hides = hides, covers = covers, number_of_states = number_of_states, poses = poses, incompatibilities = incompatibilities)
