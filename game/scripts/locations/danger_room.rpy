label train:
    $ selected_Event = EventScheduler.choose_Event()

    if selected_Event:
        $ selected_Event.start()

        return

    $ D20 = renpy.random.randint(1, 20)

    call wait

    $ Player.XP += 5 + int(clock/10)

    return
