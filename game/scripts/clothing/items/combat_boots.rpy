init -1 python:

    def combat_boots(Owner):
        name = "combat boots"
        string = "combat_boots"
        
        type = "boots"
        
        dialogue_lines = {}
        
        if Owner.tag == "Laura":
            dialogue_lines.update({
                "shopping": "Sick.",
                "purchased": f"Thanks, {Owner.player_petname}.",
                "gift": "Oh, thanks!",
                "change": "No problem."})
        
        price = 60
        
        shame = 0
        
        hides = []
        covers = []
        
        number_of_states = 1
        
        poses = ["standing"]
        
        incompatibilities = []
        
        return ClothingClass(Owner, name, string, type, dialogue_lines, price = price, shame = shame, hides = hides, covers = covers, number_of_states = number_of_states, poses = poses, incompatibilities = incompatibilities)
