init python:

    def all_Rogue_Clothes():
        Clothes = [
            Rogue_asymmetric_hair(),
            Rogue_black_garterbelt(),
            Rogue_black_gloves(),
            Rogue_black_jeans(),
            Rogue_black_lace_bra(),
            Rogue_black_lace_panties(),
            Rogue_black_stockings(),
            Rogue_black_tanktop(),
            Rogue_black_tights(),
            Rogue_black_top(),
            Rogue_brown_jacket(),
            Rogue_green_bikini_bottoms(),
            Rogue_green_bikini_top(),
            Rogue_green_dress(),
            Rogue_green_mesh_top(),
            Rogue_green_nighty(),
            Rogue_leather_skirt(),
            Rogue_Rogue_belt(),
            Rogue_Rogue_suit(),
            Rogue_spiked_bracelets(),
            Rogue_spiked_collar(),
            Rogue_symmetric_hair(),
            Rogue_towel(),
            Rogue_wet_hair(),
            Rogue_yellow_boots(),
            Rogue_yellow_gloves()]

        return Clothes

    def default_Rogue_Outfits(Outfits):
        asymmetric_hair = Rogue_asymmetric_hair()
        black_gloves = Rogue_black_gloves()
        black_tanktop = Rogue_black_tanktop()
        green_bikini_bottoms = Rogue_green_bikini_bottoms()
        spiked_bracelets = Rogue_spiked_bracelets()
        spiked_collar = Rogue_spiked_collar()

        for Outfit in Outfits:
            update = {}

            if Outfit.name == "casual":
                update = {
                    "hair": asymmetric_hair,
                    "underwear": green_bikini_bottoms, "hose": Rogue_black_tights(),
                    "skirt": Rogue_leather_skirt(),
                    "bra": black_tanktop, "top": Rogue_green_mesh_top(),
                    "neck": spiked_collar, "gloves": black_gloves, "sleeves": spiked_bracelets}
            elif Outfit.name == "alternate":
                update = {
                    "hair": asymmetric_hair,
                    "underwear": green_bikini_bottoms,
                    "pants": Rogue_black_jeans(),
                    "bra": black_tanktop, "top": Rogue_black_top(),
                    "neck": spiked_collar, "gloves": black_gloves, "sleeves": spiked_bracelets}
            elif Outfit.name == "hero":
                update = {
                    "hair": asymmetric_hair,
                    "underwear": green_bikini_bottoms,
                    "bodysuit": Rogue_Rogue_suit(),
                    "belt": Rogue_Rogue_belt(),
                    "gloves": Rogue_yellow_gloves(),
                    "jacket": Rogue_brown_jacket()}
            elif Outfit.name == "swimsuit":
                update = {
                    "hair": asymmetric_hair,
                    "underwear": green_bikini_bottoms,
                    "bra": Rogue_green_bikini_top(),
                    "neck": spiked_collar, "gloves": black_gloves, "sleeves": spiked_bracelets}
            elif Outfit.name == "pajamas":
                update = {
                    "hair": asymmetric_hair,
                    "underwear": green_bikini_bottoms,
                    "bra": black_tanktop,
                    "neck": spiked_collar, "gloves": black_gloves, "sleeves": spiked_bracelets}
            elif Outfit.name == "shower":
                update = {
                    "hair": asymmetric_hair,
                    "dress": Rogue_towel()}

            Outfit.update_Clothes(update)
                
        return Outfits