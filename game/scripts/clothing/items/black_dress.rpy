init -1 python:

    def black_dress(Owner):
        name = "black dress"
        string = "black_dress"
        
        type = "dress"
        
        dialogue_lines = {}
        
        if Owner.tag == "Laura":
            dialogue_lines.update({
                "shopping": "This is. . . nice.",
                "purchased": f"Aw, thanks, {Owner.player_petname}.",
                "gift": f"Huh, that's really nice of you, {Owner.player_petname}.",
                "change": "Feeling fancy, are we?"})
        
        price = 175
        
        shame = 0
        
        hides = ["breasts", "pussy"]
        covers = ["breasts", "pussy"]
        
        number_of_states = 2
        
        poses = ["standing"]
        
        incompatibilities = []
        
        return ClothingClass(Owner, name, string, type, dialogue_lines, price = price, shame = shame, hides = hides, covers = covers, number_of_states = number_of_states, poses = poses, incompatibilities = incompatibilities)
