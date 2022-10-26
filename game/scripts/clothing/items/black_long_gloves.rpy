init -1 python:

    def black_long_gloves(Owner):
        name = "black long gloves"
        string = "black_long_gloves"
        
        type = "gloves"
        
        dialogue_lines = {}
        
        if Owner.tag == "Laura":
            dialogue_lines.update({
                "shopping": "Hmm, familiar.",
                "purchased": f"Appreciate it, {Owner.player_petname}.",
                "gift": "Oh, thanks.",
                "change": "Okay."})
        
        price = 50
        
        shame = 0
        
        hides = []
        covers = []
        
        number_of_states = 1
        
        poses = ["standing"]
        
        incompatibilities = []
        
        return ClothingClass(Owner, name, string, type, dialogue_lines, price = price, shame = shame, hides = hides, covers = covers, number_of_states = number_of_states, poses = poses, incompatibilities = incompatibilities)
