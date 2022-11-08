init -1:
    
    define ch_jean = Character("[Jean.name]", who_color = "#d92912", image = "Jean_sprite")
    define ch_jean_nvl = Character("[Jean.name]", kind = nvl)
    define ch_jean_tele = Character("[Jean.name]", who_color = "#d92912", what_italic = True)

transform Jean_color:
    matrixcolor TintMatrix("#d92912")

init python:

    def create_Jean():
        Jean = GirlClass(
            "Jean",
            voice = ch_jean, text = ch_jean_nvl,
            love = 10, trust = 20, desire = 0)

        Jean.player_petname = Player.name
        Jean.player_petnames = [Jean.player_petname]

        Jean.pubes = "strip"

        Jean.used_to_anal = False

        Jean.psychic = False

        Professors.append(Jean)

        set_default_Outfits(Jean)

        return Jean