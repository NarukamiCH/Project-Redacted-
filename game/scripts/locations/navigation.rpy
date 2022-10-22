label world_map:
    while True:
        $ Player.destination = None

        menu:
            "Where would you like to go?"
            "Campus" if Player.location != "bg_campus":
                $ Player.destination = "bg_campus"
            "Campus (locked)" if Player.location == "bg_campus":
                pass
            "My room" if Player.location != "bg_player":
                $ Player.destination = "bg_player"
            "My room (locked)" if Player.location == "bg_player":
                pass
            "Girls' rooms":
                menu:
                    "[Rogue.name]'s room" if Rogue in active_Girls and Player.location != "bg_rogue":
                        $ Player.destination = Rogue
                    "[Rogue.name]'s room (locked)" if Rogue in active_Girls and Player.location == "bg_rogue":
                        pass
                    "[Laura.name]'s room" if Laura in active_Girls and Player.location != "bg_laura":
                        $ Player.destination = Laura
                    "[Laura.name]'s room (locked)" if Laura in active_Girls and Player.location == "bg_laura":
                        pass
                    "Back":
                        pass
            "Class" if Player.location != "bg_classroom":
                $ Player.destination = "bg_classroom"
            "Class (locked)" if Player.location == "bg_classroom":
                pass
            "The Danger Room" if Player.location != "bg_danger":
                $ Player.destination = "bg_danger"
            "The Danger Room (locked)" if Player.location == "bg_danger":
                pass
            "The pool" if Player.location != "bg_pool":
                $ Player.destination = "bg_pool"
            "The pool (locked)" if Player.location == "bg_pool":
                pass
            "The mall" if Player.location not in ["bg_mall", "bg_shop"]:
                $ Player.destination = "bg_mall"
            "The mall (locked)" if Player.location in ["bg_mall", "bg_shop"]:
                pass
            "The showers" if Player.location != "bg_shower":
                $ Player.destination = "bg_shower"
            "The showers (locked)" if Player.location == "bg_shower":
                pass
            "Stay where I am":
                $ Player.destination = Player.location

                return

        if Player.destination:
            $ stack_depth = renpy.call_stack_depth()

            while stack_depth > 0:
                $ stack_depth -= 1

                $ renpy.pop_call()

            show black_screen onlayer black

            call hide_all

            if Player.destination == "bg_campus":
                jump campus
            elif Player.destination == "bg_player":
                jump player_room
            elif Player.destination in all_Girls:
                $ Girl = Player.destination
                $ Player.destination = f"bg_{Girl.tag.lower()}"

                jump girls_room
            elif Player.destination == "bg_classroom":
                jump classroom
            elif Player.destination == "bg_danger":
                jump danger_room
            elif Player.destination == "bg_pool":
                jump pool
            elif Player.destination == "bg_mall":
                jump mall
            elif Player.destination == "bg_shower":
                jump showers

label campus:
    $ door_locked = False

    if Player.destination != Player.location:
        $ selected_Event = EventScheduler.choose_Event()

        if selected_Event:
            show black_screen onlayer black

            $ selected_Event.start()

        if Player.destination != Player.location:
            $ Nearby = []

            call set_the_scene(location = "bg_campus", fade = True)
    else:
        call set_the_scene(location = "bg_campus")

    if clock <= 10:
        if time_index > 2:
            "You're getting tired, you head back to your room."

            $ Player.destination = "bg_player"

            jump player_room
        else:
            call wait

    while True:
        menu:
            "Wait" if time_index < 3:
                call wait
            "Wait (locked)" if time_index > 2:
                pass
            "Leave":
                call world_map

label player_room:
    $ door_locked = False

    if Player.destination != Player.location:
        $ selected_Event = EventScheduler.choose_Event()

        if selected_Event:
            show black_screen onlayer black

            $ selected_Event.start()

        if Player.destination != Player.location:
            $ Nearby = []

            call set_the_scene(location = "bg_player", fade = True)
    else:
        call set_the_scene(location = "bg_player")

    if clock <= 10:
        call wait

    while True:
        menu:
            "Lock the door" if not door_locked:
                $ door_locked = True
            "Unlock the door" if door_locked:
                $ door_locked = False
            "Wait" if time_index < 3:
                call wait
            "Sleep" if time_index > 2:
                call sleep
            "Leave":
                call world_map

label girls_room:
    $ door_locked = False

    if Player.destination != Player.location:
        $ selected_Event = EventScheduler.choose_Event()

        if selected_Event:
            show black_screen onlayer black

            $ selected_Event.start()

        if Player.destination != Player.location:
            $ Nearby = []

            call set_the_scene(location = Girl.home, fade = True)
    else:
        call set_the_scene(location = Girl.home)

    if clock <= 10:
        call wait

    while True:
        menu:
            "Lock the door" if not door_locked:
                $ door_locked = True
            "Unlock the door" if door_locked:
                $ door_locked = False
            "Wait" if time_index < 3:
                call wait
            "Sleep" if time_index > 2:
                call sleep
            "Leave":
                call world_map

label classroom:
    $ door_locked = False

    if Player.destination != Player.location:
        $ selected_Event = EventScheduler.choose_Event()

        if selected_Event:
            show black_screen onlayer black

            $ selected_Event.start()

        if Player.destination != Player.location:
            $ Nearby = []

            call set_the_scene(location = "bg_classroom", fade = True)

        if time_index < 2 and weekday < 5:
            call find_a_seat
    else:
        call set_the_scene(location = "bg_classroom")

    if clock <= 10:
        if time_index > 2:
            "It's getting late, you head back to your room."

            $ Player.destination = "bg_player"

            jump player_room
        else:
            call wait

    while True:
        menu:
            "Take morning class" if time_index == 0 and weekday < 5 and clock >= 30:
                call take_class
            "Take afternoon class" if time_index == 1 and weekday < 5 and clock >= 30:
                call take_class
            "Take class (locked)" if time_index > 1 or weekday > 4 or clock < 30:
                pass
            "Wait" if time_index < 3:
                call wait
            "Wait (locked)" if time_index > 2:
                pass
            "Leave":
                call world_map

label danger_room:
    $ door_locked = False

    if Player.destination != Player.location:
        $ selected_Event = EventScheduler.choose_Event()

        if selected_Event:
            show black_screen onlayer black

            $ selected_Event.start()

        if Player.destination != Player.location:
            $ Nearby = []

            call set_the_scene(location = "bg_danger", fade = True)
    else:
        call set_the_scene(location = "bg_danger")

    if clock <= 10:
        if time_index > 2:
            "It's getting late, you head back to your room."

            $ Player.destination = "bg_player"

            jump player_room
        else:
            call wait

    while True:
        menu:
            "Train" if clock >= 30 and time_index < 3:
                call train
            "Train (locked)" if clock < 30 or time_index > 2:
                pass
            "Wait" if time_index < 3:
                call wait
            "Wait (locked)" if time_index > 2:
                pass
            "Leave":
                call world_map

label pool:
    $ door_locked = False

    if Player.destination != Player.location:
        $ selected_Event = EventScheduler.choose_Event()

        if selected_Event:
            show black_screen onlayer black

            $ selected_Event.start()

        if Player.destination != Player.location:
            $ Nearby = []

            call set_the_scene(location = "bg_pool", fade = True)
    else:
        call set_the_scene(location = "bg_pool")

    if clock <= 10:
        if time_index > 2:
            "You're getting tired, you head back to your room."

            $ Player.destination = "bg_player"

            jump player_room
        else:
            call wait

    while True:
        menu:
            "Swim" if clock >= 30:
                call swim
            "Swim (locked)" if clock < 30:
                pass
            "Wait" if time_index < 3:
                call wait
            "Wait (locked)" if time_index > 2:
                pass
            "Leave":
                call world_map

label mall:
    $ door_locked = False

    if Player.destination != Player.location:
        $ selected_Event = EventScheduler.choose_Event()

        if selected_Event:
            show black_screen onlayer black

            $ selected_Event.start()

        $ Nearby = []

        if Player.destination != Player.location:
            call set_the_scene(location = "bg_mall", fade = True)
    else:
        call set_the_scene(location = "bg_mall")

    if clock <= 10:
        if time_index > 2:
            "The mall is now closing, please make your way to the nearest exit."

            $ Player.destination = "bg_player"

            jump player_room
        else:
            call wait

    while True:
        menu:
            "Shop" if clock >= 30:
                call shop
            "Shop (locked)" if clock < 30:
                pass
            "Wait" if time_index < 3:
                call wait
            "Wait (locked)" if time_index > 2:
                pass
            "Leave":
                call world_map

label showers:
    $ door_locked = False

    if Player.destination != Player.location:
        $ selected_Event = EventScheduler.choose_Event()

        if selected_Event:
            show black_screen onlayer black

            $ selected_Event.start()

        if Player.destination != Player.location:
            $ Nearby = []

            call set_the_scene(location = "bg_shower", fade = True)
    else:
        call set_the_scene(location = "bg_shower")

    if clock <= 10:
        if time_index == 3:
            "You're getting tired, you head back to your room."

            $ Player.destination = "bg_player"

            jump player_room
        else:
            call wait

    while True:
        menu:
            "Shower" if clock >= 30:
                call take_a_shower
            "Shower (locked)" if clock < 30:
                pass
            "Wait" if time_index < 3:
                call wait
            "Wait (locked)" if time_index > 2:
                pass
            "Leave":
                call world_map
