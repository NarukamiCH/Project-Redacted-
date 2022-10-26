init -1 python:

    def cloth_dress(Owner):
        name = "cloth dress"
        string = "cloth_dress"
        
        type = "dress"
        
        dialogue_lines = {}
        
        price = 250
        
        shame = 1
        
        hides = ["breasts", "pussy"]
        covers = ["breasts", "pussy", "thighs"]
        
        number_of_states = 2
        
        poses = ["standing"]
        
        incompatibilities = []
        
        return ClothingClass(Owner, name, string, type, dialogue_lines, price = price, shame = shame, hides = hides, covers = covers, number_of_states = number_of_states, poses = poses, incompatibilities = incompatibilities)
