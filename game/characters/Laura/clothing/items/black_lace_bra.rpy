init -1 python:

    def Laura_black_lace_bra():
        name = "black lace bra"
        string = "black_lace_bra"
        
        type = "bra"
        
        dialogue_lines = {
            "shopping": "Straps, huh?",
            "purchased": f"I see what you're into, {Laura.player_petname}.",
            "gift": "Oh, you want me to wear this?",
            "change": "If you insist."}
        
        price = 75
        
        shame = 1
        
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
