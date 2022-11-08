init -1 python:

    def Laura_red_skirt():
        name = "red skirt"
        string = "red_skirt"
        
        type = "skirt"
        
        dialogue_lines = {
            "shopping": "Where have I seen this before?",
            "purchased": "Doesn't leave much to the imagination.",
            "gift": "I guess I can wear this.",
            "change": "I understand why you like this one."}
        
        price = 75
        
        shame = 2
        
        hides = ["pussy"]
        covers = ["pussy"]
        
        number_of_states = 2
        
        poses = ["standing"]
        
        incompatibilities = ["belt"]
        
        return ClothingClass(
            Laura, 
            name, string, type, 
            dialogue_lines, 
            price = price, shame = shame, 
            hides = hides, covers = covers, 
            number_of_states = number_of_states, poses = poses, 
            incompatibilities = incompatibilities)
