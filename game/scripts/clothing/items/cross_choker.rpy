init -1 python:

    def cross_choker(Owner):
        name = "cross choker"
        string = "cross_choker"
        
        type = "neck"
        
        dialogue_lines = {}
        
        if Owner.tag == "Laura":
            dialogue_lines.update({
                "shopping": "I like this.",
                "purchased": "Thanks.",
                "gift": "Cool, thanks.",
                "change": "Sure, I can put it on."})
        
        price = 60
        
        shame = 0
        
        hides = []
        covers = []
        
        number_of_states = 1

        poses = ["standing"]
        
        incompatibilities = []
        
        return ClothingClass(Owner, name, string, type, dialogue_lines, price = price, shame = shame, hides = hides, covers = covers, number_of_states = number_of_states, poses = poses, incompatibilities = incompatibilities)
