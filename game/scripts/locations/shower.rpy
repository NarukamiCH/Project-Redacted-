label take_a_shower:
    python:
        showering_Girls = []

        for G in active_Girls:
            if G.location == "bg_shower":
                showering_Girls.append(G)

        renpy.random.shuffle(showering_Girls)

    if showering_Girls:
        ch_player "I'm taking a shower, care to join me?"

        python:
            for G in showering_Girls:
                G.undress()
                G.wet = True

    if showering_Girls:
        if len(showering_Girls) > 2:
            "You take a quick shower with the girls."
        elif len(showering_Girls) == 2:
            "You take a quick shower with [showering_Girls[0].name] and [showering_Girls[1].name]."
        else:
            "You take a quick shower with [showering_Girls[0].name]."
    else:
        "You take a quick shower."

        $ line = renpy.random.choice([
            "It was fairly uneventful.",
            "A few people came and went as you did so.",
            "That was refreshing."])

        "[line]"

    if showering_Girls:
        python:
            for G in showering_Girls:
                G.change_into("towel")

    $ clock -= 30 if clock >= 30 else clock

    return
