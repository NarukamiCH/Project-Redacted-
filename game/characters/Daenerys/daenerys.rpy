init -1:
    
    define ch_dany = Character("[Daenerys.name]", who_color = "#1945a4", image = "Daenerys_sprite")
    define ch_dany_nvl = Character("[Daenerys.name]", kind = nvl)

init python:

    def create_Daenerys():
        Daenerys = GirlClass(
            "Daenerys",
            voice = ch_dany, text = ch_dany_nvl,
            love = 0, trust = 0, desire = 10)

        Daenerys.player_petname = Player.name
        Daenerys.player_petnames = [Daenerys.player_petname]

        Daenerys.pubes = "triangle"

        Daenerys.used_to_anal = False

        return Daenerys