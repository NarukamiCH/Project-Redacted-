init python:

    def caught_showering():
        label = "caught_showering"

        conditions = [
            "len(active_Girls) > len(Player.Party)",
            "Player.destination != Player.location",
            "Player.destination == 'bg_shower'"]

        conversation = False

        priority = False

        repeatable = True

        return EventClass(label, conditions, conversation = conversation, priority = priority, repeatable = repeatable)

label caught_showering:
    call remove_all(location = Player.destination)

    while Girl in Player.Party:
        $ Girl = renpy.random.choice(active_Girls)
    
    $ Girl.wet = True
    $ Girl.location = Player.destination
    $ Girl.undress(instant = True)

    $ Player.focused_Girl = Girl

    "As you approach the showers, you hear some humming noises from inside."
    
    menu:
        "What do you do?"
        "Enter":
            $ choice = None
        "Knock":
            $ choice = "knock"
        "Come back later":
            $ Player.destination = "bg_player"

            jump player_room

    if choice == "knock":
        "You knock on the door. You hear some shuffling inside."

        $ Girl.change_into("towel")

        "You hear the rustling of a towel and some knocking around, but after a few seconds [Girl.name] comes to the door."
        
        call set_the_scene(location = Player.destination, fade = True)

        if Girl.tag == "Rogue":
            Girl.voice "Sorry about that [Girl.player_petname], I was just wrapping up my shower."
        elif Girl.tag == "Laura":
            Girl.voice "Oh, hey [Girl.player_petname]. I was just finishing up."
    else:
        $ D20 = renpy.random.randint(1, 20)

        if D20 > 15:
            call set_the_scene(location = Player.destination, fade = True)
            
            "As you enter the showers, you see [Girl.name] washing up."
            
            if not approval_check(Girl, "love", 80) and not approval_check(Girl, "trust", 100):
                $ Girl.change_into("towel")

                "She grabs a towel and covers up."

            if Girl.tag == "Rogue":
                Girl.voice "Hey! Learn to knock maybe?!"
            elif Girl.tag == "Laura":
                Girl.voice "Um, hey? Don't knock much?"

            menu:
                extend ""
                "Sorry!":
                    pass
                "I uh. . .":
                    pass
                "And miss the view?":
                    pass
                "Why, would it have made a difference?":
                    pass
        else:
            $ Girl.change_into("towel", instant = True)
            
            call set_the_scene(location = Player.destination, fade = True)

            "As you enter the showers, you see [Girl.name] putting on a towel."

            if Girl.tag == "Rogue":
                Girl.voice "Well hello there, [Girl.player_petname]. Hoping to see something more?"
            elif Girl.tag == "Laura":
                Girl.voice "Oh, hey [Girl.player_petname]. Trying to slip in unnoticed?"
            
            menu:
                extend ""
                "Sorry, I should have knocked.":
                    pass
                "Well, to be honest. . .":
                    pass
                "I still like the view. . .":
                    pass
        
        if not approval_check(Girl, threshold = 120):
            if Girl.tag == "Rogue":
                Girl.voice "Well, it happens, just be careful."
            elif Girl.tag == "Laura":
                Girl.voice "Well, just keep an eye on your own bits."
                Girl.voice "Wouldn't want them going missing."
        elif not approval_check(Girl, threshold = 160):
            if Girl.tag == "Rogue":
                Girl.voice "Well, it happens, just be careful next time."
            elif Girl.tag == "Laura":
                Girl.voice "Uh-huh."
        else:
            if Girl.tag == "Rogue":
                Girl.voice "You could have just asked, [Girl.player_petname]."
            elif Girl.tag == "Laura":
                Girl.voice "Meh, I don't mind much. . ."

            if Girl.Clothes["top"].name == "towel":
                $ Girl.expose_breasts()
                $ Girl.expose_pussy()
                
                pause 1.0
                
                $ Girl.fix_clothing()

                "She flashes you real quick."

    if Girl.tag == "Rogue":
        Girl.voice "I should probably get going. . ."
    elif Girl.tag == "Laura":
        Girl.voice "I should get going. . ."
        
    menu:
        extend ""
        "Sure, see you later then.":
            call hide_Character(Girl)
        "Actually, could you stick around a minute?":
            if approval_check(Girl, "love", 60) or approval_check(Girl, "trust", 80):
                if Girl.tag == "Rogue":
                    Girl.voice "Sure, what's up?"
                elif Girl.tag == "Laura":
                    Girl.voice "Huh? Ok, what's up?"
            else:
                if Girl.tag == "Rogue":
                    Girl.voice "Um, actually, I'm not really comfortable being so. . . exposed?"
                    Girl.voice "I'll just see you around later."
                elif Girl.tag == "Laura":
                    Girl.voice "I probably shouldn't hang out like this."
                    Girl.voice "We'll talk later."

                call hide_Character(Girl)

    return