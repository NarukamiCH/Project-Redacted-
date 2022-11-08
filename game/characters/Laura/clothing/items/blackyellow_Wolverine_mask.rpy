init -1 python:

    def Laura_blackyellow_Wolverine_mask():
        name = "black-and-yellow Wolverine mask"
        string = "blackyellow_Wolverine_mask"

        type = "face_inner_accessory"

        dialogue_lines = {
            "shopping": "I could get used to wearing this.",
            "purchased": f"Thanks, {Laura.player_petname}.",
            "gift": "Ha, cool.",
            "change": f"Feeling adventurous, {Laura.player_petname}?"}

        price = 100

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
