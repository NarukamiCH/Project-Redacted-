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

    $ Rogue.change_Outfit("casual", instant = True)

    call show_Character(Rogue, x_position = stage_right, transition = easeinright)

    $ Player.focused_Girl = Rogue

    $ Rogue.name = "???"
    $ Rogue.change_face("perplexed")

    ch_rogue "Professor? You wanted to see me?"

    $ Xavier.change_face("smile")

    ch_xavier "Ah, yes, thank you, Rogue."

    $ Rogue.name = "Rogue"

    ch_xavier "[Player.name], I would like you to meet one of our students. [Rogue.name], this is [Player.name]."
    
    $ Rogue.change_face("smile")

    ch_rogue "Pleasure to meet ya, [Rogue.player_petname]!"

    menu:
        extend ""
        "You've convinced me, [Xavier.name]. I'll stay.":
            $ Rogue.change_face("confused")

            ch_rogue "I. . . what?"
        "It's a pleasure to meet you too!":
            $ Rogue.change_face("sexy")

            call change_Girl_stat(Rogue, "love", 1)

    ch_xavier "[Rogue.name], I was hoping that you might be able to help show [Player.name] around. You know, introduce him to the other students and make him feel welcome."
    
    $ Rogue.change_face("smile")

    ch_rogue "Well sure, Prof!"
    ch_xavier "[Player.name], I leave you in [Rogue.name]'s capable hands."

    menu:
        extend ""
        "Bless you, old man":
            $ Xavier.change_face("confused")

            ch_xavier ". . ."
        "Capable hands indeed.":
            call change_Girl_stat(Rogue, "love", 1)
            $ Rogue.change_face("sly")

            ch_rogue "Heh, okay Romeo."

    call hide_Character(Xavier, transition = easeoutright)

    $ Xavier.name = "Xavier"

    $ Rogue.change_face("smile")

    ch_rogue "Shall we, [Rogue.player_petname]?"

    jump chapter_one_tour

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

label chapter_one_tour:
    call hide_Character(Rogue)
    call set_the_scene(location = "bg_player", fade = True)
    call add_Characters(Rogue)

    $ Rogue.change_face("neutral")

    ch_rogue "You've already seen your room, right [Rogue.player_petname]? We each get private rooms now that the campus has been expanded."
    ch_player "Nice, where's yours?"
    ch_rogue "Oh, right down the hall, all the doors are labeled."

    call hide_Character(Rogue)
    call set_the_scene(location = "bg_classroom", fade = True)
    call add_Characters(Rogue)

    ch_rogue "This here is one of our classrooms."
    ch_rogue "We gotta bunch of real neat classes you can sign up to take."

    menu:
        extend ""
        "So uh. . . what are you taking?":
            ch_rogue "Mutant Physiology, World Politics, Inorganic Chem, a few others."
        "Aw man, I have to do work here too?":
            call change_Girl_stat(Rogue, "love", -2)
            call change_Girl_stat(Rogue, "trust", -1)

            $ Rogue.change_face("sad", mouth = "neutral")

            ch_rogue "'Fraid so, [Rogue.player_petname]."

    if approval_check(Rogue, threshold = 40):
        $ Rogue.change_face("sexy")

        ch_rogue "Ya know, if you sign up for a class with me, we could study together…"

    call hide_Character(Rogue)
    call set_the_scene(location = "bg_danger", fade = True)
    call add_Characters(Rogue)

    $ Rogue.change_face("neutral")

    ch_rogue "This is the Danger Room. It's decked out with all sorts of advanced tech. It can even simulate realistic battlefield scenarios."
    ch_rogue "You'll spend a lot of time here with the rest of us, training to use our powers."
    
    $ Rogue.change_face("smile")
    
    ch_rogue "If you show some combat promise, you'll do teamwork exercises with your X-squad here too."

    $ Rogue.change_face("neutral")

    call hide_Character(Rogue)
    call set_the_scene(location = "bg_campus", fade = True)
    call add_Characters(Rogue)

    ch_player "Wow, nice place."
    ch_rogue "Yeah, it's a treat getting to live here. Prof. X was really generous to turn his mansion into the Institute."    
    
    ch_rogue "Well [Rogue.player_petname], that's the end of the tour."

    $ Rogue.change_face("sly", eyes = "side")
    $ Rogue.arm_pose = 2
    
    ch_rogue "So uh. . . is it true what Xavier said? That other mutants' abilities don't work on you?"

    menu:
        extend ""
        "Seems that way.":
            ch_rogue "Wow. . ."
            ch_rogue "So. . . my power is the ability to absorb the mutant powers and memories of those I touch."
        "I guess. Why do you care?":
            call change_Girl_stat(Rogue, "love", -1)

            ch_rogue "Well, my power is the ability to absorb the mutant powers and memories of those I touch."

    $ Rogue.arm_pose = 1

    $ Rogue.change_face("neutral", eyes = "down")

    ch_rogue "Only, I still can't really control it. I can't touch people without hurting them, and I might even put them into a coma if I'm not careful."
    
    $ Rogue.change_face("sad")

    ch_rogue "I haven't been able to touch someone in a really long time. . ."

    menu:
        extend ""
        "So? Whatcha waiting for?":
            $ Rogue.change_face("surprised")

            ch_rogue ". . . Really? You don't mind?"

            menu:
                extend ""
                "Go for it!":
                    call change_Girl_stat(Rogue, "love", 5)
                    call change_Girl_stat(Rogue, "trust", 2)

                    $ Rogue.change_face("smile")

                    ch_rogue "Wow, thanks, [Rogue.player_petname]!"

                    $ Rogue.arm_pose = 2
                    $ Rogue.take_off("gloves")

                    "She takes off her gloves and reaches out to touch your face."
                    "Her fingers brush against your skin, and she shivers slightly. She pulls away shyly."
                "What about a kiss?":
                    if approval_check(Rogue, "love", 40):
                        $ Rogue.change_face("sexy")

                        ch_rogue "Hmm. . . okay. . ."

                        $ Rogue.change_face("kiss")

                        "She gives you a little peck on the cheek."
                    else:
                        $ Rogue.change_face("neutral", eyes = "side")

                        ch_rogue "Heh, no thanks, [Rogue.player_petname]."
                        ch_rogue "But maybe. . ."

                        $ Rogue.arm_pose = 2
                        $ Rogue.take_off("gloves")

                        "She takes off her gloves and reaches out to touch your face."
                        "Her fingers brush against your skin, and she shivers slightly. She pulls away shyly."

            $ Rogue.arm_pose = 1

            $ Rogue.craving_rate += 1

            ch_rogue "Whoa, that was. . . intense."

            $ Rogue.craving_rate += 1

            call change_Girl_stat(Rogue, "love", 2)
            call change_Girl_stat(Rogue, "trust", 2)

            $ Rogue.change_into("black gloves")

            ch_rogue "Thanks, [Rogue.player_petname], I. . . really appreciate it."
        "[[Move in for a kiss]":
            $ Rogue.change_face("angry")

            "She pushes you away." with vpunch

            call change_Girl_stat(Rogue, "trust", -5)

            ch_rogue "[Player.name]! I just met you!"
        "Damn, that sucks.":
            call change_Girl_stat(Rogue, "love", -2)
            call change_Girl_stat(Rogue, "trust", -1)

            $ Rogue.change_face("sad")

            ch_rogue "Yeah. . . anyways. . ."

    if approval_check(Rogue, threshold = 80):
        $ Rogue.change_face("smile")

        ch_rogue "Let's hang out later!"
    else:
        $ Rogue.change_face("neutral", mouth = "lipbite")

        ch_rogue "I'll uh. . . I'll see you later!"

    call hide_Character(Rogue)

    "She hurries off, back to her room."
    "You head to yours."

    jump chapter_one_tour_end

label chapter_one_tour_end:
    $ Rogue.location = "bg_rogue"
    $ Rogue.History.update("met")

    show screen status()
    show screen Girl_picker()

    jump player_room
