init -1 python:

    def blackred_garterbelt(Owner):
        name = "black-and-red garterbelt"
        string = "blackred_garterbelt"
        
        type = "hose"
        
        dialogue_lines = {}
        
        if Owner.tag == "Laura":
            dialogue_lines.update({
                "shopping": "Spicy.",
                "purchased": "Well, okay then.",
                "gift": "Oh? Thanks.",
                "change": "We're dressing up, huh?"})
        
        price = 70
        
        shame = 1
        
        hides = []
        covers = []
        
        number_of_states = 1

        poses = ["standing"]
        
        incompatibilities = []
        
        return ClothingClass(Owner, name, string, type, dialogue_lines, price = price, shame = shame, hides = hides, covers = covers, number_of_states = number_of_states, poses = poses, incompatibilities = incompatibilities)
