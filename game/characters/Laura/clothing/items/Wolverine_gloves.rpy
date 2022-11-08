init -1 python:

    def Laura_Wolverine_gloves():
        name = "Wolverine gloves"
        string = "Wolverine_gloves"
        
        type = "gloves"
        
        dialogue_lines = {
            "shopping": "These look good.",
            "purchased": "Cool.",
            "gift": f"Thanks, {Laura.player_petname}.",
            "change": "What's the mission?"}
        
        price = 70
        
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
