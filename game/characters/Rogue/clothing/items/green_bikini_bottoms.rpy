init -1 python:

    def Rogue_green_bikini_bottoms():
        name = "green bikini bottoms"
        string = "green_bikini_bottoms"
        
        type = "underwear"
        
        dialogue_lines = {}
        
        price = 60
        
        shame = 0
        
        hides = ["pussy"]
        covers = ["pussy"]
        
        number_of_states = 2
        
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
