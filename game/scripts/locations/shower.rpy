label take_a_shower:
    python:
        showering_Girls = []

        for G in active_Girls:
            if G.location == "bg_shower":
                showering_Girls.append(G)

        renpy.random.shuffle(showering_Girls)

    if showering_Girls:
        python:
            for G in showering_Girls:
                G.change_into("towel")

    $ clock -= 30 if clock >= 30 else clock

    return
