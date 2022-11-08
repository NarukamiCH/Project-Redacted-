init -1 python:

    def Laura_combat_boots():
        name = "combat boots"
        string = "combat_boots"
        
        type = "boots"
        
        dialogue_lines = {
            "shopping": "Sick.",
            "purchased": f"Thanks, {Laura.player_petname}.",
            "gift": "Oh, thanks!",
            "change": "No problem."}
        
        price = 60
        
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
