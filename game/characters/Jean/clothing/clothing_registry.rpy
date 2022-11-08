init python:

    def all_Jean_Clothes():
        return []

    def default_Jean_Outfits(Outfits):
        for Outfit in Outfits:
            update = {}
            
            if Outfit.name == "shower":
                update = {
                    "top": Jean_towel()}

            Outfit.update_Clothes(update)

        return Outfits