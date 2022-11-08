init -1 python:

    def Laura_cross_necklace():
        name = "cross necklace"
        string = "cross_necklace"
        
        type = "neck"
        
        dialogue_lines = {
            "shopping": "This looks cool.",
            "purchased": "Mmm, thanks.",
            "gift": f"Thanks for thinking of me, {Laura.player_petname}.",
            "change": "Yeah, I like that one."}
        
        price = 80
        
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
