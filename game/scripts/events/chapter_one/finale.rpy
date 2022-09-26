init python:

    def chapter_one_finale():
        label = "chapter_one_finale"

        conditions = [
            "chapter == 1",
            "day > 6",
            "time_index == 0",
            "Rogue.location != Player.location",
            "Laura.location != Player.location",
            "clock == 100"]

        conversation = False

        priority = True

        repeatable = False

        return EventClass(label, conditions, conversation = conversation, priority = priority, repeatable = repeatable)

label chapter_one_finale:
    if approval_check(Rogue, threshold = 100):
        $ good_ending = True

        $ Player.History.update("chapter_one_good_ending")
    else:
        $ good_ending = False

        $ Player.History.update("chapter_one_bad_ending")

    "You wake up from a night filled with vivid dreams."
    "Dreams of shouting, crashes, and even explosions around you.{p}You must be spending too much time in the Danger Room."

    call set_the_scene(location = "bg_hallway", fade = True)

    "As you leave your room, you almost crash into [Rogue.name]."

    $ Player.focused_Girl = Rogue

    if good_ending:
        "She seems in great spirits."
        ch_rogue "Oh, there you are, [Rogue.player_petname]!"
        ch_rogue "You missed all the excitement!"
    else:
        "She looks pretty unhappy."
        
        menu:
            extend ""
            "Hey, everything alright?":
                pass
            "Sup.":
                pass
            "[[Say nothing]":
                pass

        ch_rogue "Oh, hey, [Player.name]."
        ch_rogue "I thought something bad might have happened to you, no one knew where you were."
        ch_player "What do you mean?"
        ch_rogue "Wait, were you. . . Did you really miss the alarm and commotion?"

    ch_player "Uh. . . what?"

    if good_ending:
        ch_rogue "!!!"
        ch_rogue "They thought they could catch us offguard while the X-Men were away on mission!"
        ch_rogue "Maybe now people will think twice before trying to attack the school."
    else:
        ch_rogue ". . ."
        ch_rogue "We were attacked last night. . ."
        ch_rogue "They looked just like the X-Men - the old X-Men - but. . ."
        ch_rogue "We're still trying to figure out what happened. Get a headcount on who's missing. . ."

    menu:
        extend ""
        "Okay, slowly walk me through what happened. . .":
            call chapter_one_finale_1A
        "Huh, well okay then.":
            pass

    if good_ending:
        ch_rogue "I'm heading back to my room, it was a long night! Catch up later?"
    else:
        ch_rogue "Anyways, I kind of want to be alone for a bit."

        if approval_check(Rogue, threshold = 80):
            ch_rogue "Maybe we can catch up later."
        else:
            "She wanders off sullenly."

    call hide_Character(Rogue)

    $ Rogue.location = Rogue.home

    jump chapter_two_intro

label chapter_one_finale_1A:
    if good_ending:
        ch_rogue "We're still trying to figure out the details."
        ch_rogue "Someone must have known that most of the X-Men weren't here - they sent robots disguised as the last X-Men team to the school."
        ch_rogue "I don't know what they were after, I'm just glad we figured out what was going on and activated the school's defenses before anyone could get hurt."
        ch_rogue "Heh, well, anyone {i}else{/i}. . . The phony X-Men are just scrap metal now."
    else:
        ch_rogue "I don't know. . ."
        ch_rogue "Someone must have known that most of the X-Men weren't here - they sent {i}things{/i} disguised as the last X-Men team to the school."
        ch_rogue "They snuck in past the perimeter defenses. I guess they were here to find and kidnap mutants. . ."
        ch_rogue "By the time anyone noticed something was up and raised the alarm, they had already disappeared with a handful of students."
        ch_rogue "I hope they're okay. . ."

        if approval_check(Rogue, threshold = 80):
            "She gives you a weak smile."
            ch_rogue "I'm glad you're safe, [Player.name]."

    return
