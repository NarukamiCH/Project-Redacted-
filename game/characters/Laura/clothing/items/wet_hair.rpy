init -1 python:

    def Laura_wet_hair():
        name = "wet hair"
        string = "wet"
        
        type = "hair"
        
        dialogue_lines = {
            "shopping": None,
            "purchased": None,
            "gift": None,
            "change": "Wet, huh?"}
        
        price = 0
        
        shame = 0
        
        hides = []
        covers = []
        
        number_of_states = 1
        
        poses = ["standing"]
        
        incompatibilities = []
        
        return ClothingClass(
            Laura, 
            name, string, type, 
            dialogue_lines, 
            price = price, shame = shame, 
            hides = hides, covers = covers, 
            number_of_states = number_of_states, poses = poses, 
            incompatibilities = incompatibilities)
