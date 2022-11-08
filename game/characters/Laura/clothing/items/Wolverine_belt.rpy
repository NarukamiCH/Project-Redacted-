init -1 python:

    def Laura_Wolverine_belt():
        name = "Wolverine belt"
        string = "Wolverine_belt"
        
        type = "belt"
        
        dialogue_lines = {
            "shopping": "Oh, I like this one.",
            "purchased": "Cool, thanks.",
            "gift": "Oh, thanks.",
            "change": "Okay."}
        
        price = 75
        
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
