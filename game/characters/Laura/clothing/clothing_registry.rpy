init python:

    def all_Laura_Clothes():
        Clothes = [
            Laura_black_dress(),
            Laura_black_lace_bra(),
            Laura_black_lace_panties(),
            Laura_black_long_gloves(),
            Laura_black_swimsuit(),
            Laura_blackred_corset(),
            Laura_blackred_garterbelt(),
            Laura_blackred_ripped_stockings(),
            Laura_blackyellow_Wolverine_boots(),
            Laura_blackyellow_Wolverine_mask(),
            Laura_blackyellow_Wolverine_suit(),
            Laura_blueyellow_Wolverine_boots(),
            Laura_blueyellow_Wolverine_mask(),
            Laura_blueyellow_Wolverine_suit(),
            # Laura_combat_boots(),
            Laura_cross_choker(),
            Laura_cross_necklace(),
            Laura_grey_panties(),
            Laura_leather_jacket(),
            Laura_leather_pants(),
            Laura_messy_hair(),
            Laura_red_skirt(),
            Laura_straight_hair(),
            Laura_thighhigh_boots(),
            Laura_towel(),
            Laura_wet_hair(),
            Laura_white_tanktop(),
            Laura_Wolverine_belt(),
            Laura_Wolverine_gloves()]

        return Clothes

    def default_Laura_Outfits(Outfits):
        for Outfit in Outfits:
            update = {}

            if Outfit.name == "casual":
                update = {
                    "hair": Laura_straight_hair(),
                    "underwear": Laura_grey_panties(),
                    "pants": Laura_leather_pants(),
                    "bra": Laura_white_tanktop(),
                    "neck": Laura_cross_choker(),
                    "jacket": Laura_leather_jacket()}
            elif Outfit.name == "alternate":
                update = {
                    "hair": Laura_straight_hair(),
                    "underwear": Laura_grey_panties(),
                    "skirt": Laura_red_skirt(), "boots": Laura_thighhigh_boots(),
                    "bra": Laura_blackred_corset(),
                    "neck": Laura_cross_necklace()}
            elif Outfit.name == "hero":
                update = {
                    "hair": Laura_straight_hair(), "face_outer_accessory": Laura_blackyellow_Wolverine_mask(), 
                    "underwear": Laura_grey_panties(),
                    "bodysuit": Laura_blackyellow_Wolverine_suit(),
                    "belt": Laura_Wolverine_belt()}
            elif Outfit.name == "swimsuit":
                update = {
                    "hair": Laura_straight_hair(),
                    "bodysuit": Laura_black_swimsuit()}
            elif Outfit.name == "pajamas":
                update = {
                    "hair": Laura_straight_hair(),
                    "underwear": Laura_grey_panties(),
                    "bra": Laura_white_tanktop()}
            elif Outfit.name == "shower":
                update = {
                    "hair": Laura_straight_hair(),
                    "dress": Laura_towel()}

            Outfit.update_Clothes(update)
                
        return Outfits