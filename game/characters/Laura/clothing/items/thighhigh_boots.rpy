init -1 python:

    def Laura_thighhigh_boots():
        name = "thigh-high boots"
        string = "thighhigh_boots"
        
        type = "boots"
        
        dialogue_lines = {
            "shopping": "Hmm, these aren't bad.",
            "purchased": f"Thanks, {Laura.player_petname}.",
            "gift": f"Thanks, {Laura.player_petname}.",
            "change": "I can throw them on if you want."}
        
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
