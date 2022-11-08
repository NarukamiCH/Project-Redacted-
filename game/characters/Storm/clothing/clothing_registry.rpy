init python:

    def all_Storm_Clothes():
        return []

    def default_Storm_Outfits(Outfits):
        for Outfit in Outfits:
            update = {}

            if Outfit.name == "shower":
                update = {
                    "top": Storm_towel()}

            Outfit.update_Clothes(update)

        return Outfits