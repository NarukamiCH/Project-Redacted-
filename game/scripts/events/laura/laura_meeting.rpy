init python:

    def Laura_meeting():
        label = "Laura_meeting"

        conditions = [
            "Laura not in active_Girls",
            "Player.destination == 'bg_danger'"]

        conversation = False

        priority = True

        repeatable = False

        return EventClass(label, conditions, conversation = conversation, priority = priority, repeatable = repeatable)

label Laura_meeting:
    call set_the_scene(location = "bg_danger", show_Characters = False, fade = True)
    call remove_all

    "As you approach the Danger Room, you hear a ferocious clanging of metal."
    "Just as you pass through the door, a robotic arm smashes into your face."

    show black_screen onlayer black with vpunch

    pause 0.5

    $ Laura.name = "???"
    $ Laura.names = []
    $ Laura.location = Player.location
    $ Laura.change_Outfit(instant = True)

    $ color_transform = get_color_transform(location = Player.location)

    call show_Character(Laura, x_position = stage_center, color_transform = color_transform, transition = False)

    pause 0.5

    hide black_screen onlayer black with dissolve

    "When you come to, a girl pulls you up by your arm."

    $ active_Girls.append(Laura)

    $ Player.focused_Girl = Laura

    ch_laura "Oh, good, you don't look too damaged."
    ch_laura "Sorry about that, I was getting a work-out in. Must have forgotten to lock the door."

    $ loop = True
    $ topics = []

    while loop:
        menu:
            extend ""
            "Who are you?" if Laura.name == "???":
                $ Laura.name = "X-23"

                ch_laura "I go by \"X-23\" in the field."

                $ Laura.names.append("X-23")
            "X-23? Is that your real name?" if Laura.name == "X-23" and "X-23" not in topics:
                $ topics.append("X-23")

                ch_laura "It's the one I was born with."
            "Is there anything else I could call you?" if "X-23" in topics and "Laura" not in topics:
                $ topics.append("Laura")

                call change_Girl_stat(Laura, "love", 1)
                
                $ Laura.name = "Laura"

                ch_laura "I also go by Laura. Laura Kinney."

                $ Laura.names.append("Laura")

                menu:
                    extend ""
                    "Nice to meet you Laura.":
                        call change_Girl_stat(Laura, "love", 1)

                        ch_laura "Yeah, ok."
                    "Hello Laura Laura Kinney.":
                        ch_laura "It's just -"

                        call change_Girl_stat(Laura, "love", 1)

                        ch_laura "Oh, I get it."
                    "How did you get that name?":
                        call change_Girl_stat(Laura, "love", -1)

                        ch_laura "That's a little personal."

                        $ Laura.blush = 0
            "I think I'd prefer calling you X-23." if Laura.name == "Laura":
                call change_Girl_stat(Laura, "love", -1)

                $ Laura.name = "X-23"

                ch_laura "Suit yourself."
            "My name is [Player.name]" if Laura.name != "???" and "Player" not in topics:
                $ topics.append("Player")

                ch_laura "Ok."

                menu:
                    extend ""
                    ". . .and it's nice to meet you?":
                        call change_Girl_stat(Laura, "love", 1)

                        ch_laura "Yeah, you too."
                    "So. . .":
                        pass
            "What are you doing here?" if "training" not in topics:
                $ topics.append("training")

                ch_laura "Training. That's the point of this place."

                menu:
                    extend ""
                    "I meant in the school, I haven't seen you around before.":
                        pass
                    "Ok, that's fair.":
                        pass

                ch_laura "I've been here since before your time."
                ch_laura "Mostly out in the field though."
            "So you don't stay here long?" if "training" in topics and "stay" not in topics:
                $ topics.append("stay")

                call change_Girl_stat(Laura, "love", 1)

                ch_laura "I take on a lot of solo assignments for the team."
                ch_laura "I think I'll stick around for a while this time, though."
                ch_laura "Try just being a student for a change."
            "What the hell was that?" if len(topics) < 2 and "wtf" not in topics:
                $ topics.append("wtf")

                ch_laura "It was a robot arm."
                ch_laura "Like I said, sorry."
                ch_laura "You probably should have ducked though."
            "So what's your mutant power?" if Laura.name != "???" and "claws" not in topics:
                $ topics.append("claws")

                call change_Girl_stat(Laura, "love", 1)

                ch_laura "I can heal fast."
                ch_laura "Also, I have claws."

                $ Laura.arm_pose = 2
                $ Laura.claws = True

                "*snikt*"

                menu:
                    extend ""
                    "Wow, they look pretty sharp.":
                        ch_laura "Yeah, indestructible too."
                    "Cool.":
                        call change_Girl_stat(Laura, "love", 1)

                        ch_laura "Yeah, indestructible too."
                    "Ouch.":
                        $ Laura.claws = False
                        call change_Girl_stat(Laura, "love", -1)
                        
                        ch_laura "Don't worry, I won't stab you."                        
                        ch_laura "Probably."

                $ Laura.claws = False
                $ Laura.arm_pose = 1
            "Don't you want to know my power?" if "claws" in topics and "powers" not in topics:
                $ topics.append("powers")

                if approval_check(Laura, "love", 20):
                    ch_laura "Yeah, I guess."
                else:
                    ch_laura "Not really, but whatever."

                ch_player "I'm immune to mutant powers and can shut them off."
                ch_laura "Huh. Interesting. So you can stop me from healing?"
                ch_player "I think so, if I touch you. Just temporarily."

                call change_Girl_stat(Laura, "desire", 3)

                ch_laura "Give it a try."
                "She holds out her arm, and you grab it."

                call change_Girl_stat(Laura, "love", 1)
                call change_Girl_stat(Laura, "trust", 2)
                call change_Girl_stat(Laura, "desire", 5)

                ch_laura "Huh."

                $ Laura.craving_rate += 1

                "You can feel her shudder a little."

                $ Laura.craving_rate += 1
                call change_Girl_stat(Laura, "love", 1)
                call change_Girl_stat(Laura, "desire", 5)

                ch_laura "That feels weird."

                $ Laura.craving_rate += 1
                call change_Girl_stat(Laura, "desire", 3)

                ch_laura ". . . a little more \"alive\" than usual."

                $ Laura.craving_rate += 1
                call change_Girl_stat(Laura, "desire", 5)

                ch_laura "Almost. . . dangerous."
            "Anyways. . ." if Laura.name != "???":
                $ loop = False

        if len(topics) > 2 and Laura.name == "???":
            call change_Girl_stat(Laura, "love", -2)

            ch_laura "Oh, by the way, you can call me \"X-23\"."

            $ Laura.name = "X-23"
            $ Laura.names.append("X-23")

        if len(topics) > 7:
            $ loop = False

    ch_laura "Anyways, I'll let you have the Room."

    if "player" in topics:
        call change_Girl_stat(Laura, "love", 1)
        call change_Girl_stat(Laura, "desire", 1)

        ch_laura "I'll see you around [Player.name]."
    else:
        ch_laura "I'll see you around, stranger."

    if "powers" in topics:
        call change_Girl_stat(Laura, "desire", 3)

        ch_laura "Maybe we can. . . spar."

    call hide_Character(Laura)

    $ Nearby = []

    $ Laura.location = Laura.home
    $ Laura.History.update("met")
    
    $ clock -= 20

    return