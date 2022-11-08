init -1 python:

    def Laura_blackred_corset():
        name = "black-and-red corset"
        string = "blackred_corset"
        
        type = "bra"
        
        dialogue_lines = {
            "shopping": "This looks familiar.",
            "purchased": f"Not too subtle, {Laura.player_petname}.",
            "gift": "Hmm, you want me to wear this?",
            "change": "I like it too."}
        
        price = 125
        
        shame = 2
        
        hides = ["breasts"]
        covers = ["breasts"]
        
        number_of_states = 2
        
        poses = ["standing"]
        
        incompatibilities = []
        
        return ClothingClass(
            Laura, 
            name, string, type, 
            dialogue_lines, 
            price = price, shame = shame, 
            hides = hides, covers = covers, 
            number_of_states = number_of_states, poses = poses, 
            incompatibilities = incompatibilities)
