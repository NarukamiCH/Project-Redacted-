init -1 python:

    def cross_necklace(Owner):
        name = "cross necklace"
        string = "cross_necklace"
        
        type = "neck"
        
        dialogue_lines = {}
        
        if Owner.tag == "Laura":
            dialogue_lines.update({
                "shopping": "This looks cool.",
                "purchased": "Mmm, thanks.",
                "gift": f"Thanks for thinking of me, {Owner.player_petname}.",
                "change": "Yeah, I like that one."})
        
        price = 80
        
        shame = 0
        
        hides = []
        covers = []
        
        number_of_states = 1

        poses = ["standing"]
        
        incompatibilities = []
        
        return ClothingClass(Owner, name, string, type, dialogue_lines, price = price, shame = shame, hides = hides, covers = covers, number_of_states = number_of_states, poses = poses, incompatibilities = incompatibilities)
