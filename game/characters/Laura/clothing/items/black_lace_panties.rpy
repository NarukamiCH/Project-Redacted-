init -1 python:

    def Laura_black_lace_panties():
        name = "black lace panties"
        string = "black_lace_panties"
        
        type = "underwear"
        
        dialogue_lines = {
            "shopping": "A little revealing.",
            "purchased": f"Figures you'd like these, {Laura.player_petname}.",
            "gift": "You want me to wear these, huh?",
            "change": "I guess they are pretty sexy."}
        
        price = 60
        
        shame = 2
        
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
