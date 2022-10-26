init -1 python:

    def blackred_corset(Owner):
        name = "black-and-red corset"
        string = "blackred_corset"
        
        type = "bra"
        
        dialogue_lines = {}
        
        if Owner.tag == "Laura":
            dialogue_lines.update({
                "shopping": "This looks familiar.",
                "purchased": f"Not too subtle, {Owner.player_petname}.",
                "gift": "Hmm, you want me to wear this?",
                "change": "I like it too."})
        
        price = 125
        
        shame = 2
        
        hides = ["breasts"]
        covers = ["breasts"]
        
        number_of_states = 2
        
        poses = ["standing"]
        
        incompatibilities = []
        
        return ClothingClass(Owner, name, string, type, dialogue_lines, price = price, shame = shame, hides = hides, covers = covers, number_of_states = number_of_states, poses = poses, incompatibilities = incompatibilities)
