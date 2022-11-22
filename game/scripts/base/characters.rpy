init python:

    class PlayerClass(object):
        def __init__(self, name, **properties):
            self.name = name

            self.voice = properties.get("voice", None)
            self.text = properties.get("text", None)

            self.skin_color = properties.get("skin_color", "green")

            self.level = 1
            self.XP = 0
            self.XP_goal = 100
            self.stat_points = 0

            self.naked = False
            self.cock_out = False

            self.destination = "bg_entrance"
            self.location = "bg_entrance"

            self.focused_Girl = None
            self.Phonebook = []
            self.Party = []
            self.Keys = []
            self.Harem = []

            self.income = 12
            self.cash = 20

            self.inventory = []

            self.desire = 0
            self.semen = 3
            self.max_semen = 5

            self.mouth_Action = ActionClass([], None)
            self.hand_Action = ActionClass([], None)
            self.cock_Action = ActionClass([], None)

            self.all_Organs = [
                "mouth",
                "hand",
                "cock"]

            self.History = HistoryClass(default = False)
            self.recent_History = self.History.recent
            self.daily_History = self.History.daily
            self.permanent_History = self.History.permanent

    class GirlClass(object):
        def __init__(self, name, **properties):
            self.name = name
            self.tag = name
            self.names = [name]

            self.voice = properties.get("voice", None)
            self.text = properties.get("text", None)

            self.level = 1
            self.XP = 0
            self.XP_goal = 100
            self.stat_points = 0

            self.love = properties.get("love", 0)
            self.trust = properties.get("trust", 0)
            self.desire = properties.get("desire", 0)

            # 0: happy, 9: furious
            self.mood = 0

            self.craving = 0
            self.craving_rate = 0

            self.brows = "neutral"
            self.eyes = "neutral"
            self.mouth = "neutral"
            self.blush = 0

            self.arm_pose = 1

            self.wet = False
            self.tan_lines = {
                "top": False, "bottom": False}
            self.piercings = {
                "face": False, "nipple": False, "belly": False, "labia": False}
            self.grool = 0
            self.cumshot = {
                "hair": False, "face": False, "mouth": False, "chin": False,
                "breasts": False, "back": False, "belly": False, "hand": False}
            self.creampie = {
                "pussy": False, "anus": False}

            self.sprite_location = stage_center

            # sprite_layer = [background_characters (eg. teachers), midground (eg. steam), midground_characters (eg. teachers), foreground (eg. podium), foreground_characters (eg. Present), Player.focused_Girl, cover (eg. steam)]
            self.sprite_layer = 6

            self.destination = "hold"
            self.location = "hold"
            self.home = f"bg_{self.tag.lower()}"

            self.History = HistoryClass()
            self.recent_History = self.History.recent
            self.daily_History = self.History.daily
            self.permanent_History = self.History.permanent

            self.Wardrobe = WardrobeClass()
            self.Outfit = self.Wardrobe.current_Outfit
            self.Clothes = self.Outfit.Clothes

            self.mouth_Action = ActionClass([], None)
            self.hand_Action = ActionClass([], None)
            self.breast_Action = ActionClass([], None)
            self.pussy_Action = ActionClass([], None)
            self.ass_Action = ActionClass([], None)

            self.all_Organs = [
                "mouth",
                "hand",
                "breast",
                "pussy",
                "ass"]

            self.petname = self.name
            self.petnames = [self.name]

            all_Girls.append(self)
            all_Characters.append(self)

            bedrooms.append(self.home)

        def change_face(self, face = None, **kwargs):
            face = self.default_face() if not face else face

            brows = kwargs.get("brows", None)
            eyes = kwargs.get("eyes", None)
            mouth = kwargs.get("mouth", None)
            blush = kwargs.get("blush", 0)

            if self.mood > 4 and face in ["neutral", "bemused", "sexy", "sly", "smile", "startled"]:
                face = "angry"

            if face == "neutral":
                self.mouth = "neutral"
                self.brows = "neutral"
                self.eyes = "neutral"
            elif face == "angry":
                self.brows = "furrowed"
                self.eyes = "squint"
                self.mouth = "frown"
            elif face == "confused":
                self.brows = "cocked"
                self.eyes = "squint"

                if self.tag == "Rogue":
                    self.mouth = "neutral"
                else:
                    self.mouth = "kiss"
            elif face == "kiss":
                self.brows = "worried"
                self.eyes = "closed"
                self.mouth = "kiss"
            elif face == "manic":
                self.brows = "worried"
                self.eyes = "wide"

                if self.tag == "Rogue":
                    self.mouth = "open"
                else:
                    self.mouth = "smile"
                
                if not blush:
                    blush = 1
            elif face == "perplexed":
                self.brows = "cocked"
                self.eyes = "neutral"

                if self.tag == "Laura":
                    self.mouth = "neutral"
                else:
                    self.mouth = "open"
            elif face == "sad":
                self.brows = "worried"
                self.eyes = "neutral"
                self.mouth = "frown"
            elif face == "sexy":
                self.brows = "neutral"
                self.eyes = "sexy"
                self.mouth = "lipbite"
            elif face == "sly":
                self.brows = "neutral"
                self.eyes = "squint"
                self.mouth = "smirk"
            elif face == "smile":
                self.brows = "neutral"
                self.eyes = "neutral"

                if self.tag == "Rogue":
                    self.mouth = "smirk"
                else:
                    self.mouth = "smile"
            elif face == "surprised":
                if self.tag == "Laura":
                    self.mouth = "neutral"
                else:
                    self.mouth = "open"

                self.brows = "raised"
                self.eyes = "wide"

            self.blush = blush

            if brows:
                self.brows = brows

            if eyes:
                self.eyes = eyes

            if mouth:
                self.mouth = mouth

            return

        def default_face(self):
            if self.desire > 50 and approval_check(self, "love", 60):
                face = "sexy"
            elif self.craving > 75:
                face = "manic"
            elif not approval_check(self, threshold = 10):
                face = "angry"
            else:
                face = "neutral"

            return face

        def travel(self):
            if self.location in ["bg_danger", "bg_pool"]:
                self.destination = "bg_shower"
            elif self.location != "hold":
                possible_locations = []

                if self in Player.Harem or approval_check(self, threshold = 100):
                    possible_locations.append("bg_player")

                possible_locations.append(self.home)

                if time_index < 3:
                    possible_locations.append("bg_campus")

                if time_index < 2 and weekday < 5:
                    possible_locations.append("bg_classroom")

                if time_index < 3:
                    possible_locations.append("bg_danger")

                if time_index > 2:
                    pass
                elif time_index == 2 and weekday > 4:
                    possible_locations.append("bg_pool")
                    possible_locations.append("bg_mall")
                else:
                    possible_locations.append("bg_pool")
                    possible_locations.append("bg_mall")

                if time_index in [0, 3]:
                    possible_locations.append("bg_shower")

                renpy.random.shuffle(possible_locations)

                self.destination = possible_locations[0]

            return

        def try_on(self, Clothing, instant = False):
            self.Outfit.change_into(Clothing, instant = instant)

            return

        def take_off(self, type, instant = False):
            self.Outfit.change_out_of(type, instant = instant)

            return

        def give(self, Clothing):
            self.Wardrobe.add_Clothing(Clothing)

            return

        def change_into(self, Clothing_name, instant = False):
            if Clothing_name not in self.Wardrobe.Clothes.keys():
                self.voice(f"I don't have a piece of clothing named {Clothing_name}.")

                return

            self.Outfit.change_into(self.Wardrobe.Clothes[Clothing_name], instant = instant)

            return

        def undress(self, instant = False):
            self.Outfit.undress(instant = instant)

            return

        def expose_bra(self, instant = False):
            for type in reversed(bra_hiding_Clothing_types):
                self.Clothes[type].take_off(instant = instant)

                if self.Clothes[type].state < 1:
                    self.Outfit.remove_Clothing(type)
            
            return

        def expose_breasts(self, instant = False):
            for type in reversed(breast_hiding_Clothing_types):
                self.Clothes[type].take_off(instant = instant)

                if self.Clothes[type].state < 1:
                    self.Outfit.remove_Clothing(type)

            return

        def expose_underwear(self, instant = False):
            for type in reversed(underwear_hiding_Clothing_types):
                self.Clothes[type].take_off(instant = instant)

                if self.Clothes[type].state < 1:
                    self.Outfit.remove_Clothing(type)

            return

        def expose_pussy(self, instant = False):
            for type in reversed(pussy_hiding_Clothing_types):
                self.Clothes[type].take_off(instant = instant)

                if self.Clothes[type].state < 1:
                    self.Outfit.remove_Clothing(type)

            return

        def fix_clothing(self, instant = False):
            for type in removable_Clothing_types:
                if self.Clothes[type] and self.Clothes[type].state > 0:
                    self.Clothes[type].put_on(instant = instant)

            return

        def add_Outfit(self, Outfit):
            self.Wardrobe.add_Outfit(Outfit)

            return

        def remove_Outfit(self, Outfit_name):
            self.Wardrobe.remove_Outfit(Outfit_name)

            return

        def change_Outfit(self, Outfit_name = None, instant = False):
            if not Outfit_name:
                if self.location == "bg_danger":
                    Outfit_name = self.Wardrobe.gym_Outfit.name
                elif self.location == "bg_pool":
                    Outfit_name = self.Wardrobe.swimming_Outfit.name

                if not Outfit_name or Outfit_name == "null":
                    Outfit_name = self.Wardrobe.public_Outfit.name

            if Outfit_name not in self.Wardrobe.Outfits.keys():
                self.voice(f"I don't have an outfit named {Outfit_name}.")

                return

            if self.wet:
                self.wet = False

            self.Wardrobe.change_Outfit(self.Wardrobe.Outfits[Outfit_name], instant = instant)
            self.Outfit = self.Wardrobe.current_Outfit
            self.Clothes = self.Outfit.Clothes

            return

        def choose_Outfits(self):
            self.Wardrobe.choose_Outfits()

            return

    class NPCClass(object):
        def __init__(self, name, **properties):
            self.name = name
            self.tag = name

            self.voice = properties.get("voice", None)
            self.text = properties.get("text", None)

            self.brows = "neutral"
            self.eyes = "neutral"
            self.mouth = "neutral"

            self.sprite_location = stage_center

            # sprite_layer = [background_characters (eg. teachers), midground (eg. steam), midground_characters (eg. teachers), foreground (eg. podium), foreground_characters (eg. Present), Player.focused_Girl, cover (eg. steam)]
            self.sprite_layer = 6

            self.destination = "hold"
            self.location = "hold"

            all_Characters.append(self)

        def change_face(self, face, **kwargs):
            brows = kwargs.get("brows", None)
            eyes = kwargs.get("eyes", None)
            mouth = kwargs.get("mouth", None)

            if face == "neutral":
                self.mouth = "neutral"
                self.brows = "neutral"
                self.eyes = "neutral"
            elif face == "angry":
                self.brows = "furrowed"
                self.eyes = "neutral"
                self.mouth = "frown"
            elif face == "confused":
                self.brows = "furrowed"
                self.eyes = "squint"
                self.mouth = "neutral"
            elif face == "stunned":
                self.brows = "neutral"
                self.eyes = "up"
                self.mouth = "neutral"
            elif face == "sad":
                self.brows = "neutral"
                self.eyes = "neutral"
                self.mouth = "frown"
            elif face == "smile":
                self.brows = "neutral"
                self.eyes = "neutral"
                self.mouth = "smile"
            elif face == "surprised":
                self.brows = "raised"
                self.eyes = "wide"
                self.mouth = "neutral"

            if brows:
                self.brows = brows

            if eyes:
                self.eyes = eyes

            if mouth:
                self.mouth = mouth

            return