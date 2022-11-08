init python:

    def all_Kitty_Clothes():
        return []

    def default_Kitty_Outfits(Outfits):
        for Outfit in Outfits:
            update = {}

            if Outfit.name == "shower":
                update = {
                    "top": Kitty_towel()}

            Outfit.update_Clothes(update)

        return Outfits