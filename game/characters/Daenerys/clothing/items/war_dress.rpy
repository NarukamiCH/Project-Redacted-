init -1 python:

    def Daenerys_war_dress():
        name = "war dress"
        string = "war_dress"
        
        type = "dress"
        
        dialogue_lines = {}
        
        price = 250
        
        shame = 0
        
        hides = ["breasts", "pussy"]
        covers = ["breasts", "pussy"]
        
        number_of_states = 2
        
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
