label cheat_menu(Girl):
    while True:
        menu:
            "[Girl.name]: Love: [Girl.love], Trust: [Girl.trust], Desire: [Girl.desire], Location: [Girl.location]"
            "Raise love":
                call change_Girl_stat(Girl, "love", 10)
            "Lower love":
                call change_Girl_stat(Girl, "love", -10)
            "Raise trust":
                call change_Girl_stat(Girl, "trust", 10)
            "Lower trust":
                call change_Girl_stat(Girl, "trust", -10)
            "Raise desire":
                call change_Girl_stat(Girl, "desire", 10)
            "Lower desire":
                call change_Girl_stat(Girl, "desire", -10)
            "Wardrobe":
                call wardrobe_editor(Girl)
            "Unlock all Girls":
                python:
                    Girls = []

                    if chapter >= 2:
                        for G in chapter_two_Girls:
                            Girls.append(eval(f"{G}"))

                    if chapter >= 1:
                        for G in chapter_one_Girls:
                            Girls.append(eval(f"{G}"))

                    for G in Girls:
                        if G not in active_Girls:
                            G.History.update("met")

                            active_Girls.append(G)

                            Player.Phonebook.append(G)
            "Maximize all Girls' stats":
                python:
                    for G in active_Girls:
                        G.love = 100
                        G.devotion = 100
                        G.trust = 100
            "Add all Girls to Harem":
                python:
                    for G in active_Girls:
                        if G not in Player.Harem:
                            Player.Harem.append(G)
            "Unlock all clothes":
                python:
                    for G in active_Girls:
                        Clothes = eval(f"all_{G.tag}_Clothes()")

                        for Clothing in Clothes:
                            G.give(Clothing)
            "Done":
                return

label wardrobe_editor(Girl):
    while True:
        menu wardrobe_menu:
            "View":
                while True:
                    menu:
                        "Default":
                            call show_Character(Girl)
                        "Blowjob":
                            if not renpy.showing(f"{Girl.tag}_sprite blowjob"):
                                call show_blowjob(Girl)
                            else:
                                call show_Character(Girl)
                        "Sex":
                            if not renpy.showing(f"{Girl.tag}_sprite sex"):
                                call show_sex(Girl)
                            else:
                                call show_Character(Girl)
                        "Doggy":
                            if not renpy.showing(f"{Girl.tag}_sprite doggy"):
                                call show_doggy(Girl)
                            else:
                                call show_Character(Girl)
                        "Back":
                            jump wardrobe_menu
            "Wardrobe":
                $ quit = False

                while not quit:
                    call screen Wardrobe_picker(Girl)

                    python:
                        if _return != "quit":
                            new_Clothing = _return

                            currently_wearing = False

                            for Clothing in Girl.Wardrobe.current_Outfit.Clothes.values():
                                if Clothing.name == new_Clothing.name:
                                    currently_wearing = True

                                    break

                            if currently_wearing:
                                Girl.take_off(new_Clothing.type)
                            else:
                                Girl.change_into(new_Clothing.name)
                        else:
                            quit = True
            "Back":
                return

    return
