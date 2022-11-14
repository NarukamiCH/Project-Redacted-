init -1:
    
    define ch_rogue = Character("[Rogue.name]", who_color = "#2ca05aff", image = "Rogue_sprite")
    define ch_rogue_nvl = Character("[Rogue.name]", kind = nvl)

transform Rogue_color:
    matrixcolor TintMatrix("#2ca05aff")

init python:

    def create_Rogue():
        Rogue = GirlClass(
            "Rogue",
            voice = ch_rogue, text = ch_rogue_nvl,
            love = 20, trust = 20, desire = 0)

        Rogue.player_petname = "Sugar"
        Rogue.player_petnames = [Rogue.player_petname, Player.name]

        Rogue.piercings["belly"] = True

        Rogue.pubes = "hairy"

        Rogue.used_to_anal = False

        Students.append(Rogue)

        return Rogue