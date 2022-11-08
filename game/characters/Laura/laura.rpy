init -1:
    
    define ch_laura = Character("[Laura.name]", who_color = "#d9bb12", image = "Laura_sprite")
    define ch_laura_nvl = Character("[Laura.name]", kind = nvl)

transform Laura_color:
    matrixcolor TintMatrix("#d9bb12")

init python:

    def create_Laura():
        Laura = GirlClass(
            "Laura",
            voice = ch_laura, text = ch_laura_nvl,
            love = 10, trust = 10, desire = 0)

        Laura.names.append("X-23")

        Laura.player_petname = Player.name
        Laura.player_petnames = ["guy", Laura.player_petname]

        Laura.piercings.update({
            "nipple": "barbell",
            "labia": "both"})

        Laura.pubes = "hairy"

        Laura.used_to_anal = True

        Laura.claws = False

        Students.append(Laura)

        set_default_Outfits(Laura)

        return Laura