init python:

    def set_default_Outfits(Girl, change = True):
        casual = OutfitClass("casual", wear_in_public = True, wear_in_private = True)
        alternate = OutfitClass("alternate", wear_in_public = True, wear_in_private = True)
        hero = OutfitClass("hero", activewear = True)
        swimsuit = OutfitClass("swimsuit", swimwear = True)
        pajamas = OutfitClass("pajamas", sleepwear = True)
        shower = OutfitClass("shower")

        Outfits = eval(f"default_{Girl.tag}_Outfits")([casual, alternate, hero, swimsuit, pajamas, shower])

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