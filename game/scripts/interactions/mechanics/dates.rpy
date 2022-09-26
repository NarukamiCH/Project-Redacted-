label ask_on_date(Girl):
    if Girl.History.check("agreed_to_date", tracker = "daily"):
        if Girl.tag == "Rogue":
            Girl.voice "Come on, I already said \"yes.\""
        elif Girl.tag == "Laura":
            Girl.voice "I already told you \"ok.\""

        return
    elif Girl.History.check("turned_down_date", tracker = "daily"):
        if Girl.tag == "Rogue":
            Girl.voice "I think you got your answer already."
        elif Girl.tag == "Laura":
            Girl.voice "Back off."
            
        return
        
    if not approval_check(Girl, "love", 20):
        if Girl.tag == "Rogue":
            Girl.voice "Yeah, you wish."
        elif Girl.tag == "Laura":
            Girl.voice "Nah."
        
        $ Girl.History.update("turned_down_date")

        return
    elif approval_check(Girl, "trust", 20):
        if Girl.tag == "Rogue":
            Girl.voice "Yeah, sounds good. See ya in a bit, [Girl.Petname]."
        elif Girl.tag == "Laura":
            Girl.voice "Sure, see you there."
    else:
        if Girl.tag == "Rogue":
            Girl.voice "I think I'm washing my hair tonight. . ."
        elif Girl.tag == "Laura":
            Girl.voice "I've got some other stuff to do. . ."
        
        $ Girl.History.update("turned_down_date")

        return

    menu:
        "Cool, I'll meet you in the campus square." if bg_current != "bg campus" or time_index < 2:
            pass
        "Let's get going then." if bg_current == "bg campus" and time_index == 2:
            pass
         
    if bg_current != "bg campus" or time_index < 2:
        if Girl.tag == "Rogue":
            Girl.voice "Yeah, see you then!"
        elif Girl.tag == "Laura":
            Girl.voice "Right."
        
    $ Player.History.update("date")
    
    $ Girl.History.update("agreed_to_date")

    return

label date_night:
    $ Player.Party = []

    python:
        for G in active_Girls:
            if G.History.check("agreed_to_date", tracker = "daily"):
                Player.Party.append(G)

    call set_the_scene(location = "bg_campus", fade = True)

    $ Player.Party = sort_Girls_by_approval(Player.Party)

    $ Player.focused_Girl = Player.Party[0]

    "As you arrive, you see [Player.Party[0].name] waiting for you."

    if clock < 60:
        if Player.Party[0].tag == "Rogue":
            Player.Party[0].voice "You really kept me waiting, [Player.Party[0].player_petname]!"
        elif Player.Party[0].tag == "Laura":
            Player.Party[0].voice "What took you so long?"

        menu:
            "Sorry, I got held up!":
                Player.Party[0].voice "Don't let it happen again."
            "I lost track of time.":
                Player.Party[0].voice "Well spend your time better!"
            "I had stuff to take care of.":
                Player.Party[0].voice "That's not an excuse!"

    if clock < 25:
        Player.Party[0].voice "There's no time to actually do anything tonight!"
            
        "[Player.Party[0].name] storms off."
        
        call remove_Character(Player.Party[0])
        
        return

    if Player.Party[0].tag == "Rogue":
        Player.Party[0].voice "Where are we going?"
    elif Player.Party[0].tag == "Laura":
        Player.Party[0].voice "Where we headed?"

    $ choice = None

    menu choose_date_location:
        extend ""
        "Let's go to the mall." if not Player.History.check("shopping", tracker = "recent") and clock >= 20:
            $ choice = "shopping"
        "Let's go to the mall. (locked)" if Player.History.check("shopping", tracker = "recent") or clock < 20:
            $ choice = "shopping"
        "Let's get dinner." if not Player.History.check("dinner", tracker = "recent") and clock >= 20:
            $ choice = "dinner"
        "Let's get dinner. (locked)" if Player.History.check("dinner", tracker = "recent") or clock < 20:
            $ choice = "dinner"
        "Let's catch a movie." if not Player.History.check("movie", tracker = "recent") and clock >= 60:
            $ choice = "movie"
        "Let's catch a movie. (locked)" if Player.History.check("movie", tracker = "recent") or clock < 60:
            $ choice = "movie"
        "Let's call it a night.":
            if Player.History.check("shopping", tracker = "recent") or Player.History.check("dinner", tracker = "recent") or Player.History.check("movie", tracker = "recent"):
                show blackscreen onlayer black with dissolve

                "It's getting late, you head back to the dorms. . ."
            else:
                if Player.Party[0].tag == "Rogue":
                    Player.Party[0].voice "Well why even bother cleaning up?"
                elif Player.Party[0].tag == "Laura":
                    Player.Party[0].voice "Huh."
                    
                show blackscreen onlayer black with dissolve

            jump end_of_date

    if Player.Party[0].tag == "Rogue":
        Player.Party[0].voice "Sounds fun."
    elif Player.Party[0].tag == "Laura":
        Player.Party[0].voice "Cool."

    show blackscreen onlayer black with dissolve

    if choice == "shopping":
        "You wander the mall, checking out some of the nicer boutiques."
        
        jump shopping_date
    elif choice == "dinner":
        "You go to one of the nicer restaurants in town. The food is quality but reasonably affordable."
        
        jump dinner_date
    elif choice == "movie":
        "You head to the local theater and check out the film listings."
        
        jump movie_date
