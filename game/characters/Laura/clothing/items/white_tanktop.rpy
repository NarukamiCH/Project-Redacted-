init -1 python:

    def Laura_white_tanktop():
        name = "white tanktop"
        string = "white_tanktop"
        
        type = "bra"
        
        dialogue_lines = {
            "shopping": "I go through a ton of these.",
            "purchased": f"Thanks, {Laura.player_petname}.",
            "gift": "Thanks.",
            "change": "Sure."}
        
        price = 50
        
        shame = 0
        
        hides = ["breasts"]
        covers = ["breasts"]
        
        number_of_states = 2
        
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
