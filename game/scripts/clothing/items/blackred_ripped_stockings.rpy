init -1 python:

    def blackred_ripped_stockings(Owner):
        name = "black-and-red ripped stockings"
        string = "blackred_ripped_stockings"
        
        type = "socks"
        
        dialogue_lines = {}
        
        if Owner.tag == "Laura":
            dialogue_lines.update({
                "shopping": "Is someone selling my clothes again?",
                "purchased": "Thanks, I guess.",
                "gift": "Interesting. . .",
                "change": "Tryna' start something?"})
        
        price = 25
        
        shame = 2
        
        hides = []
        covers = []
        
        number_of_states = 1

        poses = ["standing"]
        
        incompatibilities = []
        
        return ClothingClass(Owner, name, string, type, dialogue_lines, price = price, shame = shame, hides = hides, covers = covers, number_of_states = number_of_states, poses = poses, incompatibilities = incompatibilities)
