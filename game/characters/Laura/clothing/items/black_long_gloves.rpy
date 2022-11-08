init -1 python:

    def Laura_black_long_gloves():
        name = "black long gloves"
        string = "black_long_gloves"
        
        type = "gloves"
        
        dialogue_lines = {
            "shopping": "Hmm, familiar.",
            "purchased": f"Appreciate it, {Laura.player_petname}.",
            "gift": "Oh, thanks.",
            "change": "Okay."}
        
        price = 50
        
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
