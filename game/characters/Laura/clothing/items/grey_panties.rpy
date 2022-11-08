init -1 python:

    def Laura_grey_panties():
        name = "grey panties"
        string = "grey_panties"
        
        type = "underwear"
        
        dialogue_lines = {
            "shopping": "I guess I like these.",
            "purchased": f"Heh, thanks, {Laura.player_petname}.",
            "gift": "Oh? Thanks.",
            "change": "Hmm, they are comfortable."}
        
        price = 40
        
        shame = 0
        
        hides = ["pussy"]
        covers = ["pussy"]
        
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
