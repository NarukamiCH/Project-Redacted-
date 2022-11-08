label splashscreen:
    python:
        # Preference("gl powersave", "auto")

        renpy.start_predict("images/backgrounds/*.webp")
        renpy.start_predict("images/GUI/*.webp")
        renpy.start_predict("images/GUI/*/*.webp")
        renpy.start_predict("images/effects/*.webp")

        for C in Cast:
            renpy.start_predict(f"characters/{C}/images/*.webp")
            renpy.start_predict(f"characters/{C}/images/*/*.webp")
        
    return

label start:
    python:        
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
        create_Player()

        for C in Cast:
            eval(f"create_{C}()")

        register_Events()

    jump prologue

return

label after_load:
    python:
        renpy.block_rollback()

        all_Character_names = []

        for Character in all_Characters:
            all_Character_names.append(Character.tag)

        for C in Cast:
            if C not in all_Character_names:
                eval(f"create_{C}()")

        for G in all_Girls:
            set_default_Outfits(G, change = False)

        register_Events()

    return