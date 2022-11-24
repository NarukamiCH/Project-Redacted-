label chapter_one_intro:
    $ chapter = 1

    $ Player.location = "bg_player"

    $ active_Girls.append(Rogue)

    menu:
        "Skip Chapter I intro?"
        "Yes":
            $ Player.destination = "bg_player"
            $ Player.focused_Girl = Rogue

            $ Xavier.name = "Xavier"
            
            jump chapter_one_tour_end
        "No":
            pass

    "You awake with a start."
    ch_player "Oh, thank god, it was just a nightmare. . ."
    ch_player ". . . Damn, has my bed always felt this good?"

    hide black_screen onlayer black

    "You open your eyes to a strange room. You're wearing fresh clothes you don't recognize."
    ch_player "What the. . . Where. . ."

    $ Xavier.name = "???"

    $ sleeping = True
    $ first_counter = 0

    while sleeping:
        menu:
            extend ""
            "Get out of bed":
                $ sleeping = False
            "Go back to sleep":
                show black_screen onlayer black

                pause 0.4

                if first_counter < 3:
                    if first_counter == 0:
                        "You close your eyes again."
                    elif first_counter == 1:
                        "There's plenty of time."
                    elif first_counter == 2:
                        "This bed is amazing."

                    $ first_counter += 1
                else:
                    ch_xavier_tele "Wake up, [Player.name]."

                    $ sleeping = False

    hide black_screen onlayer black

    "You climb out of the ultra-posh bed."
    "The rest of the room is just as nice."

    $ waiting = True
    $ second_counter = 0

    while waiting:
        menu:
            extend ""
            "Leave room":
                $ waiting = False
            "Stay":
                if second_counter < 3:
                    if second_counter == 0:
                        "What's the hurry?"
                    elif second_counter == 1:
                        "You're not in a rush."
                    elif second_counter == 2:
                        "Nice to catch your breath every once and a while."

                    $ second_counter += 1
                else:
                    ch_xavier_tele "Time to get moving."

                    $ waiting = False

    "You carefully and quietly open the door to the room."

    call set_the_scene(location = "bg_hallway", fade = True)

    "Before you is a beautifully decorated hallway."
    "With a shrug, you walk down the corridor."

    call set_the_scene(location = "bg_entrance", fade = True)
    call show_Character(Xavier, x_position = stage_left)

    ch_xavier "Good morning, [Player.name]."

    if first_counter + second_counter > 1:
        ch_xavier "Bit slow to get started, I see."

    ch_player "Who are you? What is this place?"

    $ Xavier.name = "Charles Xavier"

    ch_xavier "My name is Charles Xavier. This is my school."
    ch_xavier "Welcome to the Xavier Institute for Higher Learning."
    ch_xavier "You were attacked by. . . an evil entity. One I've faced before."
    ch_xavier "It seems he wanted something from you."
    ch_player "That thing inside my head? What? What would it want from me?"

    $ Xavier.change_face("smile")

    ch_xavier "You're a mutant, [Player.name]. Like me."
    ch_xavier "Your abilities emerged yesterday while you were under duress, although I believe Mr. Farouk has been watching you for some time already."
    ch_player "Farouk??? That was him???"
    ch_player "Jesus, I thought he was just a shitty professor."

    $ Xavier.change_face("neutral")

    ch_xavier "That too. I don't know why he has developed an interest in you, but you are safe here from him."
    ch_xavier "You see, this is both a school and a haven that I have built for people like you and me."
    ch_xavier "There are many forces out there that wish to harm or use mutants like yourself. I fear Mr. Farouk is not the worst of them."

    $ chatting = True
    $ asked_mutant = False
    $ asked_Xavier = False

    while chatting:
        menu:
            extend ""
            "Wait a second, I'm a mutant?" if not asked_mutant:
                call chapter_one_intro_1A

                $ asked_mutant = True
            "So. . . what's your power?" if asked_mutant and not asked_Xavier:
                $ Xavier.psychic = True
                $ Xavier.brows = "furrowed"

                ch_xavier_tele "I'm a telepath, not unlike your old professor. A professor myself as well, in fact. But that is where the similarities end."

                $ Xavier.psychic = False
                $ Xavier.change_face("neutral")

                $ asked_Xavier = True
            "Well, I'm out of questions.":
                if not asked_mutant and not asked_Xavier:
                    $ Xavier.change_face("confused")

                    ch_xavier ". . . Okay. . ."

                    $ Xavier.change_face("neutral")

                $ chatting = False

    ch_xavier "I know it's a lot to take in at once."
    ch_xavier "I hope you will agree to stay here, at least for the present time. For your own protection."
    ch_xavier "In time, you may even decide to call this place home, if you so desire."

    menu:
        extend ""
        "I don't know. . .":
            pass
        "Sounds good to me!":
            $ Xavier.change_face("surprised")

            ch_xavier ". . . Really? Just like that?"

    jump chapter_one_tour_end

label chapter_one_intro_1A:
    ch_xavier "Yes, you are."

    if Player.skin_color == "green":
        "You look down at your [Player.skin_color] skin."
        ch_player "I guess that's not the most shocking news after all."

    menu:
        extend ""
        "That's. . . awesome!":
            $ Xavier.brows = "raised"

            ch_xavier "I'm. . . glad you're taking this so well, [Player.name]."
        "Oh, godammit.":
            $ Xavier.change_face("smile")

            ch_xavier "Come now, [Player.name], you are still the same person you were yesterday."
            ch_player "That's. . . not very comforting."
        "Huh.":
            ch_xavier "Indeed."

    ch_player "So. . . what are my powers?"

    if Player.skin_color == "green":
        ch_player "Other than. . . well, you know."

    ch_player "I hope I can fly."

    $ Xavier.change_face("neutral")

    ch_xavier "Our scans indicate that you have a very unique ability: close contact with you seems to. . . nullify other mutants' powers."
    ch_xavier "Accordingly, you seem to be impervious to the effects of {i}some{/i} mutant powers."
    ch_xavier "We don't fully understand how it works, and I suspect it will take much time - and training - before you are able to control it reliably."

    menu:
        extend ""
        "Huh. That's kind of lame isn't it?":
            $ Xavier.change_face("sad")

            ch_xavier "If you only knew the lengths some mutants would go to have their abilities removed. . ."
        "Oh, that's cool I guess?":
            pass

    $ Xavier.change_face("neutral")

    ch_xavier "Indeed, news of your arrival has already caused a bit of a stir around here."

    return

label chapter_one_tour_end:
    $ Rogue.location = "bg_rogue"
    $ Rogue.History.update("met")

    show screen status()
    show screen Girl_picker()

    jump player_room
