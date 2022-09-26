label splashscreen:
    return

label start:
    python:
        renpy.start_predict("images/backgrounds/*.png")
        renpy.start_predict("images/GUI/*.png")

        for G in ["Rogue", "Laura", "Jean"]:
            renpy.start_predict(f"images/{G}_standing/*.png")

        renpy.start_predict("images/Xavier/*.png")
        
        name = renpy.input("What is your name?", default = "Zero", length = 10)
        name = name.strip()

        if not name:
            name = "Zero"

    menu:
        "What is your skin color?"
        "Green":
            $ color = "green"
        "White":
            $ color = "white"
        "Black":
            $ color = "black"

    python:
        Player = PlayerClass(
            name,
            voice = ch_player, text = ch_player_nvl,
            skin_color = color)

        Rogue = GirlClass(
            "Rogue",
            voice = ch_rogue, text = ch_rogue_nvl,
            love = 20, trust = 20, desire = 0)

        Laura = GirlClass(
            "Laura",
            voice = ch_laura, text = ch_laura_nvl,
            love = 10, trust = 10, desire = 0)

        Storm = GirlClass(
            "Storm",
            voice = ch_storm, text = ch_storm_nvl,
            love = 10, trust = 30, desire = 0)

        Jean = GirlClass(
            "Jean",
            voice = ch_jean, text = ch_jean_nvl,
            love = 10, trust = 20, desire = 0)

        Farouk = NPCClass(
            "Farouk",
            voice = ch_farouk)

        Xavier = NPCClass(
            "Xavier",
            voice = ch_xavier)

        register_Events()

    jump prologue

return

label after_load:
    python:
        renpy.block_rollback()
        
        renpy.start_predict("images/backgrounds/*.png")
        renpy.start_predict("images/GUI/*.png")

        for G in ["Rogue", "Laura", "Jean"]:
            renpy.start_predict(f"images/{G}_standing/*.png")

        renpy.start_predict("images/Xavier/*.png")

        all_Character_names = []

        for Character in all_Characters:
            all_Character_names.append(Character.tag)

        if "Rogue" not in all_Character_names:
            Rogue = GirlClass(
                "Rogue",
                voice = ch_rogue, text = ch_rogue_nvl,
                love = 20, trust = 20, desire = 0)
        elif "Laura" not in all_Character_names:
            Laura = GirlClass(
                "Laura",
                voice = ch_laura, text = ch_laura_nvl,
                love = 10, trust = 10, desire = 0)
        elif "Storm" not in all_Character_names:
            Storm = GirlClass(
                "Storm",
                voice = ch_storm, text = ch_storm_nvl,
                love = 10, trust = 30, desire = 0)
        elif "Jean" not in all_Character_names:
            Jean = GirlClass(
                "Jean",
                voice = ch_jean, text = ch_jean_nvl,
                love = 10, trust = 20, desire = 0)

        if "Farouk" not in all_Character_names:
            Farouk = NPCClass(
                "Farouk",
                voice = ch_farouk)
        elif "Xavier" not in all_Character_names:
            Xavier = NPCClass(
                "Xavier",
                voice = ch_xavier)

        for G in all_Girls:
            set_default_Outfits(G, change = False)

        register_Events()

    return