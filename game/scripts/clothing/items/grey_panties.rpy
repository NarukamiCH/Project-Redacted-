init -1 python:

    def grey_panties(Owner):
        name = "grey panties"
        string = "grey_panties"
        
        type = "underwear"
        
        dialogue_lines = {}
        
        if Owner.tag == "Laura":
            dialogue_lines.update({
                "shopping": "I guess I like these.",
                "purchased": f"Heh, thanks, {Owner.player_petname}.",
                "gift": "Oh? Thanks.",
                "change": "Hmm, they are comfortable."})
        
        price = 40
        
        shame = 0
        
        hides = ["pussy"]
        covers = ["pussy"]
        
        number_of_states = 2
        
        poses = ["standing"]
        
        incompatibilities = []
        
        return ClothingClass(Owner, name, string, type, dialogue_lines, price = price, shame = shame, hides = hides, covers = covers, number_of_states = number_of_states, poses = poses, incompatibilities = incompatibilities)
