init -1 python:

    def cloth_panties(Owner):
        name = "cloth panties"
        string = "cloth_panties"
        
        type = "underwear"
        
        dialogue_lines = {}
        
        price = 30
        
        shame = 0
        
        hides = ["pussy"]
        covers = ["pussy"]
        
        number_of_states = 2
        
        poses = ["standing"]
        
        incompatibilities = []
        
        return ClothingClass(Owner, name, string, type, dialogue_lines, price = price, shame = shame, hides = hides, covers = covers, number_of_states = number_of_states, poses = poses, incompatibilities = incompatibilities)
