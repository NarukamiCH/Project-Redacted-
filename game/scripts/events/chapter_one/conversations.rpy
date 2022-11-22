init python:

    def chapter_one_conversation_A():
        label = "chapter_one_conversation_A"

        conditions = [
            "chapter == 1",
            "Player.focused_Girl.mood < 3"]

        conversation = True

        priority = False

        repeatable = True

        return EventClass(label, conditions, conversation = conversation, priority = priority, repeatable = repeatable)

label chapter_one_conversation_A:
    if Player.focused_Girl.tag == "Rogue":
        $ Rogue.change_face("neutral", brows = "worried")

        ch_rogue "I can't help feeling a little nervous with Prof. X on leave and the X-Men away on mission. . ."

        if approval_check(Rogue, threshold = 120):
            $ Rogue.change_face("neutral", mouth = "smirk")

            ch_rogue "Hey, at least we keep each other company, right, [Rogue.player_petname]?"
    elif Player.focused_Girl.tag == "Laura":
        ch_laura "I don't mind the quiet, but I'll feel better when the team is back home."

        $ Laura.mouth = "frown"

        ch_laura "People out {i}there{/i} are riled up."

    $ Player.focused_Girl.mouth = "frown"

    return

init python:

    def chapter_one_conversation_B():
        label = "chapter_one_conversation_B"

        conditions = [
            "chapter == 1",
            "Player.focused_Girl.mood < 3"]

        conversation = True

        priority = False

        repeatable = True

        return EventClass(label, conditions, conversation = conversation, priority = priority, repeatable = repeatable)

label chapter_one_conversation_B:
    if Player.focused_Girl.tag == "Rogue":
        ch_rogue "I was just thinking that it's probably good Prof. X is taking some time to relax."
        ch_rogue "He's seemed a little on edge, lately."

        $ Rogue.change_face("sad")

        ch_rogue "I guess we all have been."

        $ Rogue.change_face("neutral")
    elif Player.focused_Girl.tag == "Laura":
        $ Laura.change_face("neutral", mouth = "frown")

        ch_laura "I don't do well with downtime. Makes me antsy."

        if approval_check(Laura, threshold = 120):
            $ Laura.change_face("neutral", mouth = "lipbite")

            ch_laura "Meet me in the Danger Room later? I could use a good workout."

    $ Player.focused_Girl.change_face("neutral")

    return
