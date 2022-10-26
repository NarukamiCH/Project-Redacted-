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
            black_dress(Girl),
            black_lace_bra(Girl),
            black_lace_panties(Girl),
            black_long_gloves(Girl),
            black_swimsuit(Girl),
            blackred_corset(Girl),
            blackred_garterbelt(Girl),
            blackred_ripped_stockings(Girl),
            blackyellow_Wolverine_boots(Girl),
            blackyellow_Wolverine_mask(Girl),
            blackyellow_Wolverine_suit(Girl),
            blueyellow_Wolverine_boots(Girl),
            blueyellow_Wolverine_mask(Girl),
            blueyellow_Wolverine_suit(Girl),
            combat_boots(Girl),
            cross_choker(Girl),
            cross_necklace(Girl),
            grey_panties(Girl),
            leather_jacket(Girl),
            leather_pants(Girl),
            messy_hair(Girl),
            red_skirt(Girl),
            straight_hair(Girl),
            thighhigh_boots(Girl),
            towel(Girl),
            wet_hair(Girl),
            white_tanktop(Girl),
            Wolverine_belt(Girl),
            Wolverine_gloves(Girl)]

        return Clothes

    def set_default_Laura_Outfits(Girl, Outfits):
        for Outfit in Outfits:
            update = {}

            if Outfit.name == "casual":
                update = {
                    "hair": straight_hair(Girl),
                    "underwear": grey_panties(Girl),
                    "pants": leather_pants(Girl),
                    "bra": white_tanktop(Girl),
                    "neck": cross_choker(Girl), "belt": Wolverine_belt(Girl),
                    "jacket": leather_jacket(Girl)}
            elif Outfit.name == "alternate":
                update = {
                    "hair": straight_hair(Girl),
                    "underwear": grey_panties(Girl),
                    "skirt": red_skirt(Girl), "boots": thighhigh_boots(Girl),
                    "bra": blackred_corset(Girl),
                    "neck": cross_necklace(Girl)}
            elif Outfit.name == "hero":
                update = {
                    "face_inner_accessory": blackyellow_Wolverine_mask(Girl), "hair": straight_hair(Girl),
                    "underwear": grey_panties(Girl),
                    "bodysuit": blackyellow_Wolverine_suit(Girl),
                    "belt": Wolverine_belt(Girl)}
            elif Outfit.name == "swimsuit":
                update = {
                    "hair": straight_hair(Girl),
                    "bodysuit": black_swimsuit(Girl)}
            elif Outfit.name == "pajamas":
                update = {
                    "hair": straight_hair(Girl),
                    "underwear": grey_panties(Girl),
                    "bra": white_tanktop(Girl)}
            elif Outfit.name == "shower":
                update = {
                    "hair": straight_hair(Girl),
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

    def all_Daenerys_Clothes(Girl):
        Clothes = [
            arm_band(Girl),
            braided_hair(Girl),
            cloth_bra(Girl),
            cloth_dress(Girl),
            cloth_panties(Girl),
            loose_hair(Girl),
            towel(Girl),
            war_dress(Girl),
            wet_hair(Girl)]

        return Clothes

    def set_default_Daenerys_Outfits(Girl, Outfits):
        for Outfit in Outfits:
            update = {}

            if Outfit.name == "casual":
                update = {
                    "hair": loose_hair(Girl),
                    "underwear": cloth_panties(Girl),
                    "dress": cloth_dress(Girl),
                    "sleeves": arm_band(Girl)}
            elif Outfit.name == "alternate":
                update = {
                    "hair": braided_hair(Girl),
                    "underwear": cloth_panties(Girl),
                    "dress": war_dress(Girl)}
            elif Outfit.name == "hero":
                update = {
                    "hair": braided_hair(Girl),
                    "underwear": cloth_panties(Girl),
                    "dress": war_dress(Girl)}
            elif Outfit.name == "swimsuit":
                update = {
                    "hair": braided_hair(Girl),
                    "underwear": cloth_panties(Girl),
                    "bra": cloth_bra(Girl)}
            elif Outfit.name == "pajamas":
                update = {
                    "hair": loose_hair(Girl),
                    "underwear": cloth_panties(Girl),
                    "bra": cloth_bra(Girl)}
            elif Outfit.name == "shower":
                update = {
                    "hair": loose_hair(Girl),
                    "top": towel(Girl)}

            Outfit.update_Clothes(update)
            
        return Outfits
