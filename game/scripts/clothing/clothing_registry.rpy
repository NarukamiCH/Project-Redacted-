init python:

    def all_Rogue_Clothes(Girl):
        return []

    def set_default_Rogue_Outfits(Girl, Outfits):
        for Outfit in Outfits:
            update = {}

            if Outfit.name == "shower":
                update = {
                    "top": towel(Girl)}

            Outfit.update_Clothes(update)

        return Outfits

    def all_Kitty_Clothes(Girl):
        return []

    def set_default_Kitty_Outfits(Girl, Outfits):
        for Outfit in Outfits:
            update = {}

            if Outfit.name == "shower":
                update = {
                    "top": towel(Girl)}

            Outfit.update_Clothes(update)

        return Outfits

    def all_Laura_Clothes(Girl):
        Clothes = [
            black_lace_bra(Girl),
            black_lace_panties(Girl),
            black_swimsuit(Girl),
            blackyellow_Wolverine_mask(Girl),
            blackyellow_Wolverine_suit(Girl),
            blueyellow_Wolverine_mask(Girl),
            blueyellow_Wolverine_suit(Girl),
            grey_panties(Girl),
            leather_jacket(Girl),
            leather_pants(Girl),
            long_hair(Girl),
            messy_hair(Girl),
            towel(Girl),
            white_tanktop(Girl),
            Wolverine_belt(Girl)]

        return Clothes

    def set_default_Laura_Outfits(Girl, Outfits):
        for Outfit in Outfits:
            update = {}

            if Outfit.name == "default":
                update = {
                    "hair": long_hair(Girl),
                    "underwear": grey_panties(Girl),
                    "pants": leather_pants(Girl),
                    "bra": white_tanktop(Girl),
                    "jacket": leather_jacket(Girl)}
            elif Outfit.name == "casual":
                update = {
                    "hair": long_hair(Girl),
                    "underwear": grey_panties(Girl),
                    "pants": leather_pants(Girl),
                    "bra": white_tanktop(Girl)}
            elif Outfit.name == "costume":
                update = {
                    "hair": long_hair(Girl),
                    "underwear": grey_panties(Girl),
                    "bodysuit": blackyellow_Wolverine_suit(Girl),
                    "belt": Wolverine_belt(Girl)}
            elif Outfit.name == "swimsuit":
                update = {
                    "hair": long_hair(Girl),
                    "bodysuit": black_swimsuit(Girl)}
            elif Outfit.name == "pajamas":
                update = {
                    "hair": long_hair(Girl),
                    "underwear": grey_panties(Girl),
                    "bra": white_tanktop(Girl)}
            elif Outfit.name == "shower":
                update = {
                    "hair": long_hair(Girl),
                    "top": towel(Girl)}

            Outfit.update_Clothes(update)
            
        return Outfits

    def all_Storm_Clothes(Girl):
        return []

    def set_default_Storm_Outfits(Girl, Outfits):
        for Outfit in Outfits:
            update = {}

            if Outfit.name == "shower":
                update = {
                    "top": towel(Girl)}

            Outfit.update_Clothes(update)

        return Outfits

    def all_Jean_Clothes(Girl):
        return []

    def set_default_Jean_Outfits(Girl, Outfits):
        for Outfit in Outfits:
            update = {}
            
            if Outfit.name == "shower":
                update = {
                    "top": towel(Girl)}

            Outfit.update_Clothes(update)

        return Outfits
