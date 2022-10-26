init -1 python:

    def thighhigh_boots(Owner):
        name = "thigh-high boots"
        string = "thighhigh_boots"
        
        type = "boots"
        
        dialogue_lines = {}
        
        if Owner.tag == "Laura":
            dialogue_lines.update({
                "shopping": "Hmm, these aren't bad.",
                "purchased": f"Thanks, {Owner.player_petname}.",
                "gift": f"Thanks, {Owner.player_petname}.",
                "change": "I can throw them on if you want."})
        
        price = 75
        
        shame = 0
        
        hides = []
        covers = []
        
        number_of_states = 1
        
        poses = ["standing"]
        
        incompatibilities = []
        
        return ClothingClass(Owner, name, string, type, dialogue_lines, price = price, shame = shame, hides = hides, covers = covers, number_of_states = number_of_states, poses = poses, incompatibilities = incompatibilities)
