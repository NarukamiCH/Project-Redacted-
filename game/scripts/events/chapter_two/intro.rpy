label chapter_two_intro:
    $ chapter = 2

    $ clock = 80
    
    "You hear some commotion down the hallway and decide to check it out."

    call set_the_scene(location = "bg_entrance", fade = True)

    "It looks like the X-Men are back from their mission. You recognize some familiar faces from news broadcasts."
    
    call show_Character(Xavier, x_position = stage_left, transition = easeinleft)
    
    if good_ending:
        ch_xavier "Hello, [Player.name]. [Rogue.name] was just here catching us up on the events of last night."
        ch_xavier "It is extremely fortunate that she realized the deception before the X-Sentinels entered the school."

        if approval_check(Rogue, threshold = 100):
            ch_xavier "She seemed more interested in leaving to make sure you were alright than in basking in any praise, at least from me."
            
            if approval_check(Rogue, "love", 40):
                ch_xavier "You might have an admirer, young man."
    else:
        ch_xavier "Hello, [Player.name]. I am glad to see you are safe."

        menu:
            extend ""
            "You too, Professor.":
                pass
            "Am I really safer here than out there?":
                ch_xavier "I fear the world is growing more and more dangerous to our kind. Our only hope is to work together to keep each other safe."
            "What were you thinking, leaving us defenseless here?":
                ch_xavier "I am sorry, [Player.name]."
                ch_xavier "The X-Men and I were lured into a clever trap. We narrowly escaped, but it seems that the people behind this trap intended more than just our deaths."

        ch_xavier "We do not yet know what the X-Sentinels and their master have planned for the students they kidnapped, but we will do everything in our power to locate and rescue them."

    $ active_Girls.append(Jean)

    call show_Character(Jean, x_position = stage_right, transition = easeinright)

    $ Player.focused_Girl = Jean

    ch_xavier "Ah, [Jean.name]. We should get you to the infirmary."
    ch_jean "Are you sure, Professor? I don't think I'm hurt. I feel so alive!"
    ch_xavier "Hmm. . . There are some diagnostics we should run, just for peace of mind."
    ch_xavier "What you were exposed to up there. . . It's a miracle you're alive at all."
    ch_xavier "We will talk more later, [Player.name]. Come, [Jean.name]."
    
    call hide_Character(Xavier, transition = easeoutright)
    
    "[Jean.name] seems to notice you staring at her."
    ch_jean "Uh, do I know you?"

    menu:
        extend ""
        "Oh, I'm - ":
            pass
        "Yeah, I - ":
            pass
        "No, we - ":
            pass

    ch_xavier "[Jean.name], quickly!"
    ch_jean "Coming!"

    call hide_Character(Xavier, transition = easeoutright)
    
    "She sprints down the hallway."
    "You head back to your room, red hair on your mind."

    $ Player.destination = "bg_player"

    call set_the_scene(location = "bg_player", fade = True)

    jump player_room