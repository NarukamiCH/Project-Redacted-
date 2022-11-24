label chat_menu(Girl):
    hide screen Girl_picker

    $ Player.focused_Girl = Girl

    $ chatting = True

    while chatting:
        menu:
            "How's it going?":
                $ selected_Event = EventScheduler.choose_Event(conversation = True)

                if selected_Event:
                    $ selected_Event.start()
                else:
                    if Girl.tag == "Rogue":
                        $ lines = [
                            "Sorry, a little busy here!"]
                    elif Girl.tag == "Laura":
                        $ lines = [
                            "Let's talk later."]

                    $ line = renpy.random.choice(lines)

                    Girl.voice "[line]"
            "Talk to you later.":
                if Girl.tag == "Rogue":
                    Girl.voice "Ok, later then."
                elif Girl.tag == "Laura":
                    Girl.voice "Ok."

                $ chatting = False

    show screen Girl_picker()

    return
