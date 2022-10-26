init -1 python:

    def blueyellow_Wolverine_boots(Owner):
        name = "blue-and-yellow Wolverine boots"
        string = "blueyellow_Wolverine_boots"
        
        type = "boots"
        
        dialogue_lines = {}

        if Owner.tag == "Laura":
            dialogue_lines.update({
                "shopping": "Oh, cool, retro.",
                "purchased": f"Heh, thanks, {Owner.player_petname}.",
                "gift": "These are pretty nice.",
                "change": "Sure, no prob."})

        price = 75

        shame = 0

        hides = []
        covers = []

        number_of_states = 1
        
        poses = ["standing"]
        
        incompatibilities = []
        
        return ClothingClass(Owner, name, string, type, dialogue_lines, price = price, shame = shame, hides = hides, covers = covers, number_of_states = number_of_states, poses = poses, incompatibilities = incompatibilities)
