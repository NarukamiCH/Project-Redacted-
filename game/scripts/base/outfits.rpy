init -2 python:

    import pickle

    class ClothingClass(object):
        def __init__(self, Laura, name, string, type, dialogue_lines, **properties):
            self.Laura = Laura

            self.name = name
            self.string = string

            self.type = type

            self.dialogue_lines = dialogue_lines

            self.price = properties.get("price", 0)

            self.shame = properties.get("shame", 0)

            self.hides = properties.get("hides", [])
            self.covers = properties.get("covers", [])

            self.number_of_states = properties.get("number_of_states", 1)

            self.poses = properties.get("poses", [])

            self.incompatibilities = properties.get("incompatibilities", [])

            self.state = 0

            if self.number_of_states > 1:
                self.undressed_state = 1
            else:
                self.undressed_state = 0

            self.set_Clothing_flags()

        def put_on(self, instant = False):
            while self.state > 0:
                self.state -= 1

                if not instant:
                    renpy.pause(0.15)

            self.set_Clothing_flags()

            return

        def take_off(self, instant = False):
            while self.state < self.undressed_state:
                self.state += 1

                if not instant:
                    renpy.pause(0.15)

            self.set_Clothing_flags()

            return

        def set_Clothing_flags(self):
            self.hides_breasts = False
            self.covers_breasts = False

            self.hides_pussy = False
            self.covers_pussy = False

            self.covers_thighs = False
            self.covers_feet = False

            if "breasts" in self.hides:
                if self.type in ["bodysuit", "dress"] and self.state < 1:
                    self.hides_breasts = True
                elif self.type in ["top", "jacket"] and self.state < 1:
                    self.hides_breasts = True
                else:
                    self.hides_breasts = True

            if "breasts" in self.covers:
                if self.type in ["bodysuit", "dress"] and self.state < 1:
                    self.covers_breasts = True
                elif self.type in ["top", "jacket"] and self.state < 1:
                    self.covers_breasts = True
                else:
                    self.covers_breasts = True

            if "pussy" in self.hides:
                if self.state != 1:
                    self.hides_pussy = True

            if "pussy" in self.covers:
                if self.state != 1:
                    self.covers_pussy = True

            if "thighs" in self.covers:
                if self.state != 1:
                    self.covers_thighs = True

            if "feet" in self.covers:
                self.covers_feet = True

            return

    class OutfitClass(object):
        def __init__(self, name, **properties):
            self.name = name

            self.wear_in_public = properties.get("wear_in_public", False)
            self.wear_in_private = properties.get("wear_in_private", False)
            self.activewear = properties.get("activewear", False)
            self.sleepwear = properties.get("sleepwear", False)
            self.swimwear = properties.get("swimwear", False)

            self.Clothes = {}

            for type in all_Clothing_types:
                self.Clothes[type] = ClothingClass(Laura = None, name = None, string = None, type = None, dialogue_lines = None)

            self.set_Outfit_flags()

        def add_Clothing(self, Clothing):
            self.Clothes[Clothing.type] = Clothing

            return

        def remove_Clothing(self, types):
            if types in all_Clothing_types:
                types = [types]

            for type in types:
                self.Clothes[type] = ClothingClass(Laura = None, name = None, string = None, type = None, dialogue_lines = None)

            return

        def change_into(self, Clothing, instant = False):                
            if self.Clothes[Clothing.type].string:
                if Clothing.name == self.Clothes[Clothing.type].name:
                    return

            temp_Clothes = pickle.loads(pickle.dumps(self.Clothes, -1))

            covering_Clothes = Clothing_coverage[Clothing.type]

            for c in reversed(range(len(covering_Clothes))):
                if self.Clothes[covering_Clothes[c]].name:
                    self.Clothes[covering_Clothes[c]].take_off(instant = instant)
                    self.remove_Clothing(covering_Clothes[c])

                    if not instant:
                        renpy.pause(0.15)

            for current_Clothing in self.Clothes.values():
                if Clothing.type in current_Clothing.incompatibilities:
                    self.Clothes[current_Clothing.type].take_off(instant = instant)
                    self.remove_Clothing(current_Clothing.type)

                    if not instant:
                        renpy.pause(0.15)

            # if Clothing.type in ["underwear", "hose"]:
            #     if self.Clothes["skirt"].string and "skirt" not in covering_Clothes:
            #         self.Clothes["skirt"].take_off(instant = instant)

            #     if self.Clothes["dress"].string and "dress" not in covering_Clothes:
            #         self.Clothes["dress"].take_off(instant = instant)

            if self.Clothes[Clothing.type].name and Clothing.type in removable_Clothing_types:
                self.Clothes[Clothing.type].take_off(instant = instant)
                self.remove_Clothing(Clothing.type)

                if not instant:
                    renpy.pause(0.15)

            for incompatibility in Clothing.incompatibilities:
                if self.Clothes[incompatibility].string:
                    self.Clothes[incompatibility].take_off(instant = instant)
                    self.remove_Clothing(incompatibility)

                    if not instant:
                        renpy.pause(0.15)

            Clothing.state = Clothing.undressed_state
            self.add_Clothing(Clothing)

            if not instant:
                renpy.pause(0.15)

            self.Clothes[Clothing.type].put_on(instant = instant)

            # if Clothing.type in ["underwear", "hose"]:
            #     if self.Clothes["skirt"].string and "skirt" not in covering_Clothes:
            #         self.Clothes["skirt"].put_on(instant = instant)

            #     if self.Clothes["dress"].string and "dress" not in covering_Clothes:
            #         self.Clothes["dress"].put_on(instant = instant)

            for old_Clothing in temp_Clothes.values():
                if old_Clothing.type and not self.Clothes[old_Clothing.type].string:
                    if old_Clothing.type not in Clothing.incompatibilities and Clothing.type not in old_Clothing.incompatibilities:
                        temp_Clothes[covering_Clothes[c]].state = temp_Clothes[covering_Clothes[c]].undressed_state
                        self.add_Clothing(temp_Clothes[covering_Clothes[c]])

                        if not instant:
                            renpy.pause(0.15)

                        self.Clothes[covering_Clothes[c]].put_on(instant = instant)

            del temp_Clothes

            self.set_Outfit_flags()

            return

        def change_out_of(self, type, instant = False):
            if not self.Clothes[type].string:
                return
            elif type == "hair":
                return

            temp_Clothes = pickle.loads(pickle.dumps(self.Clothes, -1))

            covering_Clothes = Clothing_coverage[type]

            for c in reversed(range(len(covering_Clothes))):
                if self.Clothes[covering_Clothes[c]].name:
                    self.Clothes[covering_Clothes[c]].take_off(instant = instant)
                    self.remove_Clothing(covering_Clothes[c])

                    if not instant:
                        renpy.pause(0.15)

            # if type in ["underwear", "hose"]:
            #     if self.Clothes["skirt"].string and "skirt" not in covering_Clothes:
            #         self.Clothes["skirt"].take_off(instant = instant)

            #     if self.Clothes["dress"].string and "dress" not in covering_Clothes:
            #         self.Clothes["dress"].take_off(instant = instant)

            self.Clothes[type].take_off(instant = instant)
            self.remove_Clothing(type)

            if not instant:
                renpy.pause(0.15)

            # if type in ["underwear", "hose"]:
            #     if self.Clothes["skirt"].string and "skirt" not in covering_Clothes:
            #         self.Clothes["skirt"].put_on(instant = instant)

            #     if self.Clothes["dress"].string and "dress" not in covering_Clothes:
            #         self.Clothes["dress"].put_on(instant = instant)

            for c in range(len(covering_Clothes)):
                if temp_Clothes[covering_Clothes[c]].name:
                    temp_Clothes[covering_Clothes[c]].state = temp_Clothes[covering_Clothes[c]].undressed_state
                    self.add_Clothing(temp_Clothes[covering_Clothes[c]])

                    if not instant:
                        renpy.pause(0.15)

                    self.Clothes[covering_Clothes[c]].put_on(instant = instant)

            del temp_Clothes

            self.set_Outfit_flags()

            return

        def undress(self, instant = False):
            for type in reversed(removable_Clothing_types):
                if self.Clothes[type].name:
                    if not instant:
                        self.Clothes[type].take_off(instant = instant)

                    self.remove_Clothing(type)

                    if not instant:
                        renpy.pause(0.15)

            return

        def update_Clothes(self, new_Clothes):
            self.Clothes.update(new_Clothes)

            self.set_Outfit_flags()

            return

        def set_Outfit_flags(self):
            self.breasts_hidden = False
            self.breasts_covered = False

            self.underwear_hidden = False
            self.underwear_covered = False

            self.pussy_hidden = False
            self.pussy_covered = False

            self.thighs_covered = False
            self.feet_covered = False

            self.fully_nude = True

            for type in breast_hiding_Clothing_types:
                Clothing = self.Clothes[type]

                if Clothing.hides_breasts:
                    self.breasts_hidden = True
                    self.breasts_covered = True

                    break
                elif Clothing.covers_breasts:
                    self.breasts_covered = True

            for type in underwear_hiding_Clothing_types:
                Clothing = self.Clothes[type]

                if Clothing.hides_pussy:
                    self.underwear_hidden = True
                    self.underwear_covered = True

                    break
                elif Clothing.covers_pussy:
                    self.underwear_covered = True

            for type in pussy_hiding_Clothing_types:
                Clothing = self.Clothes[type]

                if Clothing.hides_pussy:
                    self.pussy_hidden = True
                    self.pussy_covered = True

                    break
                elif Clothing.covers_pussy:
                    self.pussy_covered = True

            for type in thigh_covering_Clothing_types:
                Clothing = self.Clothes[type]

                if Clothing.covers_thighs:
                    self.thighs_covered = True

                    break

            for type in feet_covering_Clothing_types:
                Clothing = self.Clothes[type]

                if Clothing.covers_feet:
                    self.feet_covered = True

                    break

            for type in removable_Clothing_types:
                Clothing = self.Clothes[type]

                self.fully_nude = False

                break

            self.shame = 0

            for type in all_Clothing_types:
                if self.Clothes[type].string:
                    self.shame += self.Clothes[type].shame
                elif type == "bra":
                    self.shame += 2
                elif type == "underwear":
                    self.shame += 5

            if not self.breasts_covered:
                self.shame += 10
            elif not self.breasts_hidden:
                self.shame += 5

            if not self.pussy_covered:
                self.shame += 20
            elif not self.pussy_hidden:
                self.shame += 15
            elif not self.underwear_covered:
                self.shame += 5
            elif not self.underwear_hidden:
                self.shame += 2

            if not self.thighs_covered:
                self.shame += 2

            if self.shame < 0:
                self.shame = 0

            return

    class WardrobeClass(object):
        def __init__(self):
            self.Clothes = {}

            self.Outfits = {}

            self.public_Outfit = OutfitClass("null")
            self.private_Outfit = OutfitClass("null")
            self.gym_Outfit = OutfitClass("null")
            self.sleeping_Outfit = OutfitClass("null")
            self.swimming_Outfit = OutfitClass("null")

            self.current_Outfit = pickle.loads(pickle.dumps(self.public_Outfit, -1))
            self.last_Outfit = pickle.loads(pickle.dumps(self.public_Outfit, -1))

        def add_Clothing(self, Clothing):
            if Clothing.name not in self.Clothes.keys():
                self.Clothes[Clothing.name] = Clothing

            return

        def add_Outfit(self, Outfit):
            if Outfit not in self.Outfits:
                self.Outfits[Outfit.name] = Outfit

            return

        def remove_Outfit(self, name):
            for Outfit in self.Outfits:
                if Outfit.name == name:
                    self.Outfits.remove(Outfit)

                    break

            return

        def change_Outfit(self, Outfit, instant = False):
            if self.current_Outfit.name == Outfit.name:
                instant = True

            self.last_Outfit = pickle.loads(pickle.dumps(self.current_Outfit, -1))

            if not instant:
                self.current_Outfit.undress(instant = instant)

                for type in removable_Clothing_types:
                    if Outfit.Clothes[type].name:
                        Outfit.Clothes[type].state = Outfit.Clothes[type].undressed_state

                        self.current_Outfit.add_Clothing(Outfit.Clothes[type])

                        renpy.pause(0.15)

                        self.current_Outfit.Clothes[type].put_on(instant = instant)

                if Outfit.Clothes["hair"]:
                    self.current_Outfit.add_Clothing(Outfit.Clothes["hair"])

            self.current_Outfit = pickle.loads(pickle.dumps(Outfit, -1))

            return

        def choose_Outfits(self):
            public_Outfits = []
            private_Outfits = []
            gym_Outfits = []
            sleeping_Outfits = []
            swimming_Outfits = []

            for Outfit in self.Outfits.values():
                if Outfit.wear_in_public:
                    public_Outfits.append(Outfit)

                if Outfit.wear_in_private:
                    private_Outfits.append(Outfit)

                if Outfit.activewear:
                    gym_Outfits.append(Outfit)

                if Outfit.sleepwear:
                    sleeping_Outfits.append(Outfit)

                if Outfit.swimwear:
                    swimming_Outfits.append(Outfit)

            self.public_Outfit = renpy.random.choice(public_Outfits) if public_Outfits else OutfitClass("null")
            self.private_Outfit = renpy.random.choice(private_Outfits) if private_Outfits else OutfitClass("null")
            self.gym_Outfit = renpy.random.choice(gym_Outfits) if gym_Outfits else OutfitClass("null")
            self.sleeping_Outfit = renpy.random.choice(sleeping_Outfits) if sleeping_Outfits else OutfitClass("null")
            self.swimming_Outfit = renpy.random.choice(swimming_Outfits) if swimming_Outfits else OutfitClass("null")

            return
