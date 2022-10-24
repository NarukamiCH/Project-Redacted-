init python:

    def caught_changing():
        label = "caught_changing"

        conditions = [
            "len(active_Girls) > len(Player.Party)",
            "Player.destination != Player.location",
            "Player.destination == 'bg_shower' or (Player.destination in bedrooms and Player.destination != 'bg_player')"]

        conversation = False

        priority = False

        repeatable = True

        return EventClass(label, conditions, conversation = conversation, priority = priority, repeatable = repeatable)

label caught_changing:
    call remove_all(location = Player.destination)

    python:
        Girl = None

        if Player.destination in bedrooms:
            for G in active_Girls:
                if G.home == Player.destination:
                    Girl = G

                    break

        while not Girl or Girl in Player.Party:
            Girl = renpy.random.choice(active_Girls)

    $ Girl.location = Player.destination

    $ Player.focused_Girl = Girl

    $ D20 = renpy.random.randint(1, 20)
    
    if D20 > 19:
        $ Girl.undress(instant = True)
    elif D20 > 17:
        $ Girl.expose_pussy(instant = True)
    elif D20 > 15:
        $ Girl.expose_breasts(instant = True)
    elif D20 > 10:
        $ Girl.expose_underwear(instant = True)
    elif D20 > 5:
        $ Girl.expose_bra(instant = True)

    call set_the_scene(location = Player.destination, fade = True)

    if D20 > 19:
        "As you enter the room, you see [Girl.name] is naked and seems to be getting dressed."
    elif D20 > 15:
        "As you enter the room, you see [Girl.name] is practically naked and seems to be getting dressed."
    elif D20 > 10:
        "As you enter the room, you see [Girl.name] is in her underwear and seems to be getting dressed."
    elif D20 > 5:
        "As you enter the room, you see [Girl.name] has her top off and seems to be getting dressed."
    else:
        "As you enter the room, [Girl.name] seems to have just finished getting dressed."

    if approval_check(Girl, "love", 80) or approval_check(Girl, "trust", 80):
        if Girl.tag == "Rogue":
            Girl.voice "Oh, hey."
        elif Girl.tag == "Laura":
            Girl.voice "Hey."
    else:
        if D20 > 5:
            $ Girl.change_into("towel")

            "She grabs a towel and covers up."

            if Girl.tag == "Rogue":
                Girl.voice "Hey! Learn to knock maybe?!"
            elif Girl.tag == "Laura":
                Girl.voice "Didn't think about knocking?"

            menu:
                extend ""
                "Sorry!":
                    pass
                "I uh. . .":
                    pass
                "And miss the view?":
                    pass
        else:
            if Girl.tag == "Rogue":
                Girl.voice "Well hello there, [Girl.player_petname]. Hoping to see something more?"
            elif Girl.tag == "Laura":
                Girl.voice "Hey, [Girl.player_petname]. Trying to catch a peek?"
            
            menu:
                extend ""
                "Sorry, I should have knocked.":
                    pass
                "Well, to be honest. . .":
                    pass

        if approval_check(Girl, "love", 60):
            if Girl.tag == "Rogue":
                Girl.voice "You could have just asked, [Girl.player_petname]."
            elif Girl.tag == "Laura":
                Girl.voice "I don't mind."

            $ Girl.expose_breasts()
            $ Girl.expose_pussy()
            
            pause 1.0
            
            $ Girl.fix_clothing()

            "She flashes you real quick."
        else:
            if Girl.tag == "Rogue":
                Girl.voice "Well, it happens, just be careful next time."
            elif Girl.tag == "Laura":
                Girl.voice "Uh-huh . . ."

    return