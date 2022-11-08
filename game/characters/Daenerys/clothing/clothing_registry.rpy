init python:

    def all_Daenerys_Clothes():
        Clothes = [
            Daenerys_arm_band(),
            Daenerys_braided_hair(),
            Daenerys_cloth_bra(),
            Daenerys_cloth_dress(),
            Daenerys_cloth_panties(),
            Daenerys_loose_hair(),
            Daenerys_towel(),
            Daenerys_war_dress(),
            Daenerys_wet_hair()]

        return Clothes

    def default_Daenerys_Outfits(Outfits):
        for Outfit in Outfits:
            update = {}

            if Outfit.name == "casual":
                update = {
                    "hair": Daenerys_loose_hair(),
                    "underwear": Daenerys_cloth_panties(),
                    "dress": Daenerys_cloth_dress(),
                    "sleeves": Daenerys_arm_band()}
            elif Outfit.name == "alternate":
                update = {
                    "hair": Daenerys_braided_hair(),
                    "underwear": Daenerys_cloth_panties(),
                    "dress": Daenerys_war_dress()}
            elif Outfit.name == "hero":
                update = {
                    "hair": Daenerys_braided_hair(),
                    "underwear": Daenerys_cloth_panties(),
                    "dress": Daenerys_war_dress()}
            elif Outfit.name == "swimsuit":
                update = {
                    "hair": Daenerys_braided_hair(),
                    "underwear": Daenerys_cloth_panties(),
                    "bra": Daenerys_cloth_bra()}
            elif Outfit.name == "pajamas":
                update = {
                    "hair": Daenerys_loose_hair(),
                    "underwear": Daenerys_cloth_panties(),
                    "bra": Daenerys_cloth_bra()}
            elif Outfit.name == "shower":
                update = {
                    "hair": Daenerys_loose_hair(),
                    "top": Daenerys_towel()}

            Outfit.update_Clothes(update)
            
        return Outfits