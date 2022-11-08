init -1 python:

    def Laura_blueyellow_Wolverine_boots():
        name = "blue-and-yellow Wolverine boots"
        string = "blueyellow_Wolverine_boots"
        
        type = "boots"
        
        dialogue_lines = {
            "shopping": "Oh, cool, retro.",
            "purchased": f"Heh, thanks, {Laura.player_petname}.",
            "gift": "These are pretty nice.",
            "change": "Sure, no prob."}

        price = 75

        shame = 0

        hides = []
        covers = []

        number_of_states = 1
        
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
