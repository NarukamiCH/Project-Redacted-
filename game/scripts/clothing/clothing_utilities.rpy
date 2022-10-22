init python:

    def register_Clothes(Girl):
        if Girl.tag == "Rogue":
            Clothes = all_Rogue_Clothes(Girl)
        elif Girl.tag == "Laura":
            Clothes = all_Laura_Clothes(Girl)
        elif Girl.tag == "Jean":
            Clothes = all_Jean_Clothes(Girl)
        elif Girl.tag == "Daenerys":
            Clothes = all_Daenerys_Clothes(Girl)
        else:
            Clothes = []

        return Clothes

    def set_default_Outfits(Girl, change = True):
        casual = OutfitClass("casual", wear_in_public = True, wear_in_private = True)
        alternate = OutfitClass("alternate", wear_in_public = True, wear_in_private = True)
        hero = OutfitClass("hero", activewear = True)
        swimsuit = OutfitClass("swimsuit", swimwear = True)
        pajamas = OutfitClass("pajamas", sleepwear = True)
        shower = OutfitClass("shower")

        Outfits = [casual, alternate, hero, swimsuit, pajamas, shower]

        if Girl.tag == "Rogue":
            Outfits = set_default_Rogue_Outfits(Girl, Outfits)
        elif Girl.tag == "Laura":
            Outfits = set_default_Laura_Outfits(Girl, Outfits)
        elif Girl.tag == "Jean":
            Outfits = set_default_Jean_Outfits(Girl, Outfits)
        elif Girl.tag == "Daenerys":
            Outfits = set_default_Daenerys_Outfits(Girl, Outfits)

        for Outfit in Outfits:
            Girl.Wardrobe.Outfits.update({Outfit.name: Outfit})

        for Outfit in Girl.Wardrobe.Outfits.values():
            for Clothing in Outfit.Clothes.values():
                if Clothing.name:
                    Girl.give(Clothing)

        if change:
            Girl.choose_Outfits()
            Girl.change_Outfit(Girl.Wardrobe.public_Outfit.name, instant = True)

        return