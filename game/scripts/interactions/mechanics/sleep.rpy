label sleep:
    $ Player.Party = []

    python:
        for G in active_Girls:
            if G.location == Player.location:
                Player.Party.append(G)

    if not Player.Party:
        if Player.location == "bg_player":
            "It's getting late, so you go to sleep."

            call wait

            return
        else:
            jump return_player_to_room
    else:
        $ Player.Party = sort_Girls_by_approval(Player.Party)

    $ Player.focused_Girl = Player.Party[0]

    if Player.location != "bg_player":
        $ temp_Girls = active_Girls[:]

        while temp_Girls:
            if temp_Girls[0].home == Player.location:
                if temp_Girls[0] not in Player.Party:
                    "[temp_Girls[0].name] probably wouldn't appreciate you staying over, you head back to your own room."

                    call remove_all
                    jump return_player_to_room

                while temp_Girls[0] != Player.Party[0]:
                    $ renpy.random.shuffle(Player.Party)

                $ temp_Girls = [None]

            $ temp_Girls.remove(temp_Girls[0])

    if Player.location == "bg_player":
        if Player.Party[0].tag == "Rogue":
            Player.Party[0].voice "It's getting late and I'm getting a bit tired."
        elif Player.Party[0].tag == "Laura":
            Player.Party[0].voice "I need some sleep. . ."
    elif Player.Party and Player.location == Player.Party[0].home:
        if Player.Party[0].tag == "Rogue":
            Player.Party[0].voice "It's getting late and I'm turning in."
        elif Player.Party[0].tag == "Laura":
            Player.Party[0].voice "I'm tired. . ."

    $ asked = False

    if Player.Party[0].History.check("had_sleepover") > 2 and approval_check(Player.Party[0], threshold = 120):
        if Player.Party[0].home == Player.location:
            Player.Party[0].voice "Are you staying over tonight?"
        else:
            Player.Party[0].voice "I'm staying over, right?"

        $ asked = True
    elif Player.Party[0].History.check("had_sleepover") < 3 and approval_check(Player.Party[0], threshold = 160):
        if Player.Party[0].tag == "Rogue":
            if Player.location == Player.Party[0].home:
                Player.Party[0].voice "I was thinking. . . maybe you wanted to stay the night?"
            else:
                Player.Party[0].voice "I was thinking. . . maybe I could stay the night?"
        elif Player.Party[0].tag == "Laura":
            if Player.location == Player.Party[0].home:
                Player.Party[0].voice "So, are you staying over?"
            else:
                Player.Party[0].voice "So, can I stay here tonight?"

        $ asked = True

    $ decision = None
    $ agreed = False

    if asked:
        menu:
            extend ""
            "Sure.":
                $ agreed = True
            "No, sorry.":
                if Player.Party[0].tag == "Rogue":
                    Player.Party[0].voice "Ok, see you tomorrow then. 'Night."
                elif Player.Party[0].tag == "Laura":
                    Player.Party[0].voice "Ok."
    else:
        if Player.Party[0].tag == "Rogue":
            if Player.location == Player.Party[0].home:
                Player.Party[0].voice "You should get going."
            else:
                Player.Party[0].voice "I'm heading out, see you tomorrow."
        elif Player.Party[0].tag == "Laura":
            if Player.location == Player.Party[0].home:
                Player.Party[0].voice "Clear out."
            else:
                Player.Party[0].voice "So, later."

        menu:
            extend ""
            "Ok, I'll head out. Goodnight." if Player.Party[0].home == Player.location:
                $ decision = "leave"
            "Ok, see you later then. Goodnight." if Player.Party[0].home != Player.location:
                $ decision = "leave"
            "Are you sure I can't stay the night? . ." if not Player.Party[0].History.check("had_sleepover") and Player.Party[0].home == Player.location:
                $ decision = "please"
            "Are you sure you can't stay? . ." if not Player.Party[0].History.check("had_sleepover") and Player.Party[0].home != Player.location:
                $ decision = "please"
            "That's not what you said the other night . ." if Player.Party[0].History.check("had_sleepover"):
                if approval_check(Player.Party[0], threshold = 160) or approval_check(Player.Party[0], "love", 60):
                    if Player.Party[0].tag == "Rogue":
                        Player.Party[0].voice "Well. . . that didn't turn out so bad, I suppose. . ."
                    elif Player.Party[0].tag == "Laura":
                        Player.Party[0].voice "That's true."

                    $ agreed = True
                else:
                    if Player.Party[0].tag == "Rogue":
                        Player.Party[0].voice "I'm afraid not this time, [Player.Party[0].player_petname]. I'll see you later."
                    elif Player.Party[0].tag == "Laura":
                        Player.Party[0].voice "Yeah, but not this time."

                    if Player.location != "bg_player":
                        ch_player "Ok, I'll be going then."

    if decision == "leave":
        if Player.Party[0].tag == "Rogue":
            Player.Party[0].voice "Yeah, good night, [Player.Party[0].player_petname]. . ."
        elif Player.Party[0].tag == "Laura":
            Player.Party[0].voice "Ok, good night then."
    elif decision == "please":
        if approval_check(Player.Party[0], threshold = 120) or approval_check(Player.Party[0], "love", 60):
            $ agreed = True

            if Player.Party[0].tag == "Rogue":
                Player.Party[0].voice "Well. . . I suppose it would be alright."
            elif Player.Party[0].tag == "Laura":
                Player.Party[0].voice "Suit yourself."
        else:
            if Player.Party[0].tag == "Rogue":
                Player.Party[0].voice "I'm afraid not, [Player.Party[0].player_petname]. Head home, I'll see you later."
            elif Player.Party[0].tag == "Laura":
                Player.Party[0].voice "Don't push it."

    if not agreed:
        if Player.Party[0].home == Player.location:
            jump return_player_to_room
        else:
            call hide_Character(Player.Party[0])
            call sleep

            return

    python:
        for G in Player.Party:
            G.change_Outfit(G.Wardrobe.sleeping_Outfit.name)

    if Player.Party[0].tag == "Rogue":
        Player.Party[0].voice "Hmm, that's a bit more comfortable."
    elif Player.Party[0].tag == "Laura":
        Player.Party[0].voice ". . ."

    if Player.Party[0].tag == "Rogue":
        Player.Party[0].voice "Let's turn in."
    elif Player.Party[0].tag == "Laura":
        Player.Party[0].voice "Night."

    jump morning_after

label return_player_to_room:
    $ Player.Party = []

    $ temp_Girls = active_Girls[:]
    $ renpy.random.shuffle(temp_Girls)

    while temp_Girls:
        if Player.location != temp_Girls[0].home and temp_Girls[0].location == Player.location:
            "[temp_Girls[0].name] heads out."

            call hide_Character(temp_Girls[0])

        $ temp_Girls.remove(temp_Girls[0])

    if Player.location != "bg_player":
        call remove_all

        "You head back to your room."

    jump player_room

label morning_after:
    call wait

    if Player.Party[0].tag == "Rogue":
        Player.Party[0].voice "'Morning [Player.Party[0].player_petname]. Sleep well?"
    elif Player.Party[0].tag == "Laura":
        Player.Party[0].voice "'Morning."

    menu:
        extend ""
        "It's always nice sleeping with you." if Player.Party[0].History.check("had_sleepover"):
            $ reaction = None

            if Player.Party[0].tag == "Rogue":
                Player.Party[0].voice "Aw, that's right sweet of ya, [Player.Party[0].player_petname]."
                Player.Party[0].voice "We'll have to keep this regular."
            elif Player.Party[0].tag == "Laura":
                Player.Party[0].voice "Yeah. . ."
                Player.Party[0].voice "Warm. . ."
        "I loved sleeping next to you." if not Player.Party[0].History.check("had_sleepover"):
            $ reaction = "nice"
        "It was fun.":
            $ reaction = "fun"

            if Player.Party[0].tag == "Rogue":
                Player.Party[0].voice "Ok, well glad I wasn't {i}too{/i} much bother."
            elif Player.Party[0].tag == "Laura":
                Player.Party[0].voice "Yeah, I guess?"
        "You were constantly tossing around.":
            $ reaction = "toss"

            if approval_check(Player.Party[0], "love", 80) or approval_check(Player.Party[0], threshold = 180):
                Player.Party[0].voice "Hmm?"
            else:
                Player.Party[0].voice "!!!"

            if Player.Party[0].History.check("had_sleepover") < 5:
                if Player.Party[0].tag == "Rogue":
                    Player.Party[0].voice "It's not like I've had much experience sleeping next to someone. . ."
                elif Player.Party[0].tag == "Laura":
                    Player.Party[0].voice "Deal with it."
            else:
                if Player.Party[0].tag == "Rogue":
                    Player.Party[0].voice "Well you should probably be used to that by now."
                elif Player.Party[0].tag == "Laura":
                    Player.Party[0].voice "Yeah, it'll be like that."
        "You need to learn to stick to your side.":
            $ reaction = "toss"

            if approval_check(Player.Party[0], threshold = 180):
                if Player.Party[0].tag == "Rogue":
                    Player.Party[0].voice "Yes, [Player.Party[0].player_petname], I'll try my best."
                elif Player.Party[0].tag == "Laura":
                    Player.Party[0].voice "Ok."
            else:
                if Player.Party[0].tag == "Rogue":
                    Player.Party[0].voice "Hmmph, you'll be sleeping alone, keep talk'in like that."
                elif Player.Party[0].tag == "Laura":
                    Player.Party[0].voice "Good luck with that."

    if reaction == "nice":
        if Player.Party[0].tag == "Rogue":
            Player.Party[0].voice "Aw, that's right sweet of ya, [Player.Party[0].player_petname]."
            Player.Party[0].voice "Makes me want to do it again sometime."
        elif Player.Party[0].tag == "Laura":
            Player.Party[0].voice "Oh. . ."
            Player.Party[0].voice "Yeah, so did I, now that you mention it. . ."
            Player.Party[0].voice "Huh."

    python:
        for G in Player.Party:
            G.History.update("had_sleepover")
            G.change_Outfit()

    $ Player.Party = []

    call set_Girls_locations

    return