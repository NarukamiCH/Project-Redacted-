label prologue:
    $ chapter = 0

    $ time_index = 0
    $ current_time = time_options[time_index]

    $ Player.location = "hold"

    scene background onlayer background
    scene

    show midground zorder 2
    show foreground zorder 4
    show cover zorder 7

    show black_screen onlayer black

    menu:
        "Skip prologue?"
        "Yes":
            $ Farouk.name = "???"

            jump chapter_one_intro
        "No":
            pass

    $ Player.location = "bg_lecture_blurred"

    "The year is 2022.{p}The world's population of mutants - individuals born with the X-Gene that can give rise to superhuman abilities - grows everyday."
    "Tensions between mutants and non-mutants are at an all-time high."
    "A team of mutant heroes known as the X-Men fight against threats to the tenuous peace between human and mutantkind."
    "As a young college student, however, a geopolitcal inter-species power struggle is a little outside your worldview."

    hide black_screen onlayer black

    "At least, until you decided to distract yourself from your morning lecture by watching the news."
    ch_reporter ". . . from the wreckage here in downtown Manhattan, where first responders are still combing through the debris from the incident last night. . ."
    ch_reporter ". . . in addition to the multiple explosions, we have footage of what appears to be a massive hurricane swelling above the city before disappearing moments later. . ."
    ch_reporter ". . . I'm receiving confirmation that the wreckage is indeed that of a Sentinel. . ."
    ch_player "Holy shit, I was just there!"

    $ Farouk.name = "Prof. Farouk"

    $ last_name = get_last_name(Player)

    $ Player.location = "bg_lecture"

    ch_farouk "Mr. [last_name]!" with vpunch
    ch_farouk "Have you ever considered that, if you spent less time on your computer in class and more time paying attention, you might not have failed our last midterm exam?"
    ch_farouk "Do you have no respect for my lecture, [last_name], no discipline?"
    "Your face flushes as you feel an entire lecture hall of students turn your way."

    menu:
        extend ""
        "Sorry, Prof. Farouk. You know freshman Psych is the reason I wake up every morning.":
            call prologue_1A
        "Grumpy college professor is a little cliche, isn't it Farouk?":
            call prologue_1B
        "You're right, Prof. Farouk, fuck this class. You could make the Oedipus complex sound boring.":
            call prologue_1C

    "For the briefest moment, a terrifying look of malice flashes across Prof. Farouk's face. . .{p}quickly replaced by mild irritation."
    ch_farouk "I've had enough of your insolence, [last_name]. Get out of my lecture hall and don't come back."

    show black_screen onlayer black

    "Shit, now I've done it. . ."

    pause 1.0

    $ Player.location = "bg_stall_closed"

    "Some time later. . ."

    hide black_screen onlayer black

    "You've locked yourself in a campus bathroom stall, crouched on a toilet seat."
    ch_player "Fuck, suspended? What am I going to do. . ."
    ch_player "Dad's going to kill me when he finds out."
    "Your mounting anxiety gives way to a sense of dread."
    "The hairs on your arms and the back of your neck rise up. You begin shivering uncontrollably."

    if Player.skin_color == "green":
        "Before your eyes, your skin begins to ripple and. . . change color."

    pause 1.0

    "Your attention suddenly shifts to the sound of the bathroom door slamming shut." with vpunch

    $ Farouk.name = "???"

    $ i = 10

    while i > 0:
        if i % 2 == 0:
            $ Player.location = "bg_stall_dark_closed"
        else:
            $ Player.location = "bg_stall_closed"

        pause 0.02

        $ i -= 1

    $ Player.location = "bg_stall_dark_closed"

    ch_farouk_tele "Mr. [last_name]." with rumble
    "The deep, inhuman voice is like something from your nightmares."
    "You cover your ears in a primal reaction."
    ch_farouk_tele "I know you are in there." with rumble
    "You realize the voice is coming from inside your head."
    "Panic fills your lungs. Something inside you knows it's already too late to call for help."

    $ Player.location = "bg_stall_dark_open"

    "The stall door unlocks itself and begins to open."
    "You kick out wildly, trying to shut the door."
    ch_farouk_tele "Do not resist. Sleep." with rumble
    "The command causes you to collapse to the floor."
    "An immense weight presses down on you."
    "You are an insect being crushed under a boot."

    pause 1.0

    $ i = 10

    while i > 0:
        if i % 2 == 0:
            $ Player.location = "bg_stall_dark_open"
        else:
            $ Player.location = "bg_stall_open"

        pause 0.02

        $ i -= 1

    $ Player.location = "bg_stall_open"

    "Suddenly, the weight lifts off you."
    "The stall door drifts, afloat in the air."
    "Gasping for air, you drift in and out of consciousness. You hear a new voice."
    "A human voice."

    $ Xavier.name = "???"

    ch_xavier_tele "You're okay, [Player.name]. . . You're safe. . . You're among friends now. . ."

    show black_screen onlayer black

    pause 2.0

    jump chapter_one_intro

label prologue_1A:
    "You succeed in making some of your classmates chuckle."
    ch_farouk "I am honored by your enthusiasm, Mr. [last_name]."
    ch_farouk "Perhaps you would care to prove your fervor, and enlighten us with your insights on today's subject?"

    menu:
        extend ""
        "Let's see. . . Jung's Shadow, encompasses not only our darkest, most reprehensible tendencies, but also our strongest creative desires. For example, your driving urge to find new ways to suck my dick":
            pass

    return

label prologue_1B:
    ch_farouk "Believe me, Mr. [last_name], you would not care to see me when I am grumpy."
    ch_farouk "At any rate, your lack of respect and plummeting academic performance does you more disservice than it does me."
    ch_farouk "Whether you succeed or fail, your tuition still funds my penthouse in Cairo."

    menu:
        extend ""
        "If I'm paying for your fancy crib, could I at least stay there for a couple of weeks next summer? I'll take good care of it, ask your wife!":
            pass

    return

label prologue_1C:
    "You succeed in making some of your classmates chuckle."
    ch_farouk "If you dislike my class that much, you are free to attend whatever matters interest you more."
    ch_farouk "What you are not entitled to do, Mr. [last_name], is waste my time."

    menu:
        extend ""
        "Alright, peace, dickhead.":
            pass

    return