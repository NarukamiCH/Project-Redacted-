label find_a_seat:
    python:
        Girls = Present[:]

        for G in reversed(Girls):
            if G not in Students:
                Girls.remove(G)
            elif G in Player.Party:
                Girls.remove(G)

        renpy.random.shuffle(Girls)

    $ Present = Player.Party if Player.Party else []

    if len(Girls) > 1:
        $ flag = False

        while not flag:
            menu:
                "You see some familiar faces: who would you like to sit near?"
                "[Rogue.name]" if Rogue in Girls and Rogue not in Present:
                    $ Present.append(Rogue)
                "[Laura.name]" if Laura in Girls and Laura not in Present:
                    $ Present.append(Laura)
                "Done":
                    $ flag = True
    elif Girls:
        menu:
            "You see [Girls[0].name] already seated: do you sit next to her?"
            "Yes":
                $ Present.append(Girls[0])
            "No":
                pass

    python:
        for G in Girls:
            if G not in Present:
                Nearby.append(G)

                G.location = "nearby"

    if Present and Player.focused_Girl not in Present:
        $ Player.focused_Girl = Present[0]

    if len(Present) > 2:
        "You figure out seating arrangements with the girls."
    elif len(Present) == 2:
        "You look for a seat between [Present[0].name] and [Present[1].name]."
    elif len(Present) == 1:
        "You look for a seat next to [Present[0].name]."
    else:
        "You look for a seat off to the side."

    call set_the_scene

    return

label take_class:
    call wait

    $ Player.XP += 5 + int(clock/10)

    return
