label swim:
    python:
        Swimmers = []
        Chillers = []
        Changers = []

        for G in Present:
            if approval_check(G, threshold = 70):
                if G.Outfit.swimwear:
                    Swimmers.append(G)
                elif G.Wardrobe.current_Outfit.fully_nude:
                    Swimmers.append(G)
                elif G.Wardrobe.swimming_Outfit.name != "null":
                    Changers.append(G)

    if Changers:
        show black_screen onlayer black

        pause 0.4

        python:
            for G in Changers:
                G.change_Outfit(G.Wardrobe.swimming_Outfit.name, instant = True)

        hide black_screen onlayer black

    # call show_swimming(Swimmers[:])

    $ D20 = renpy.random.randint(1, 20)

    $ clock -= 20 if clock >= 20 else clock

    $ temp_Girls = Swimmers[:]

    while temp_Girls:
        call show_Character(temp_Girls[0], sprite_layer = 6, animation_transform = reset_zoom_instantly, transition = dissolve)

        $ temp_Girls.remove(temp_Girls[0])

    return

label show_swimming(Swimmers):
    if Swimmers in all_Girls:
        $ Swimmers = [Swimmers]

    while Swimmers:
        $ x_position = renpy.random.random()

        while x_position < 0.3 or x_position > 0.7:
            $ x_position = renpy.random.random()

        call show_Character(Swimmers[0], sprite_layer = 1, animation_transform = swimming(x_position), transition = dissolve)

        $ Swimmers.remove(Swimmers[0])

    return
