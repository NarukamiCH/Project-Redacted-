label text_menu(Girl):
    hide screen Girl_picker
    nvl clear

    Player.text "Hey."

    if Girl.tag == "Rogue":
        $ line = f"hey {Girl.player_petname.lower()}"
    elif Girl.tag == "Laura":
        $ line = f"Hey"
    elif Girl.tag == "Jean":
        $ line = "Hey!"

    $ texting = True

    while texting:
        menu(nvl = True):
            Girl.text "[line]"
            "Want to come over?":
                Player.text "Want to come over?"

                call summon(Girl)

                $ texting = False
            "Never mind.":
                Player.text "Never mind."

                if Girl.tag == "Rogue":
                    Girl.text "ok. . ."
                elif Girl.tag == "Laura":
                    Girl.text "Huh?"
                elif Girl.tag == "Jean":
                    Girl.text "Oh, okay."

                $ texting = False

    show screen Girl_picker()

    return
