init python:

    def all_Rogue_Clothes():
        return []

    def default_Rogue_Outfits(Outfits):
        for Outfit in Outfits:
            update = {}

            if Outfit.name == "shower":
                update = {
                    "top": Rogue_towel()}

            Outfit.update_Clothes(update)

        return Outfits