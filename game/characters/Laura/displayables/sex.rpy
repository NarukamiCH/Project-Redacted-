image Laura_sex_right_hand:
    "characters/Laura/images/sex/right_hand.webp"

    anchor (0.5, 0.5)

image Laura_sex_body:
    "characters/Laura/images/sex/body.webp"

    anchor (0.5, 0.5)

layeredimage Laura_sex_legs:
    always:
        "characters/Laura/images/sex/legs.webp"

    # always:
    #     "characters/Laura/images/sex/reference.webp"

    if Laura.ass_Action.type == "anal":
        "Laura_sex_anus_animation[Laura.ass_Action.speed]" pos (0.54, 1.115)
    else:
        "characters/Laura/images/sex/anus_closed.webp" anchor (0.5, 0.5) pos (0.54, 1.115)

    if Laura.pussy_Action.type == "sex":
        "Laura_sex_pussy_animation[Laura.pussy_Action.speed]" pos (0.515, 1.04)
    else:
        "characters/Laura/images/sex/pussy_closed.webp" anchor (0.5, 0.5) pos (0.515, 1.04)

    if Laura.pubes:
        "characters/Laura/images/sex/pubes_[Laura.pubes].webp"

    anchor (0.5, 0.5)

image Laura_sex_feet:
    "characters/Laura/images/sex/feet.webp"

    anchor (0.5, 0.5)

image Laura_sex_right_hand_animation0:
    "Laura_sex_right_hand"

image Laura_sex_right_hand_animation1:
    animation
    "Laura_sex_right_hand"

    subpixel True
    pos (0.0, 0.015)
    parallel:
        pause 0.1
        ease 0.2 ypos 0.01
        pause 0.1
        ease 1.6 ypos 0.015
        repeat
    parallel:
        pause 0.1
        ease 0.2 xpos -0.01
        pause 0.1
        ease 1.6 xpos 0.0
        repeat

image Laura_sex_right_hand_animation2:
    animation
    "Laura_sex_right_hand"

    subpixel True
    pos (0.0, 0.015)
    parallel:
        pause 0.1
        ease 0.2 ypos 0.01
        pause 0.1
        ease 1.6 ypos 0.015
        repeat
    parallel:
        pause 0.1
        ease 0.2 xpos -0.01
        pause 0.1
        ease 1.6 xpos 0.0
        repeat

image Laura_sex_right_hand_animation3:
    animation
    "Laura_sex_right_hand"

    subpixel True
    pos (0.0, 0.015)
    parallel:
        pause 0.1
        ease 0.2 ypos 0.01
        pause 0.1
        ease 1.6 ypos 0.015
        repeat
    parallel:
        pause 0.1
        ease 0.2 xpos -0.01
        pause 0.1
        ease 1.6 xpos 0.0
        repeat

image Laura_sex_body_animation0:
    "Laura_sex_body"

image Laura_sex_body_animation1:
    animation
    "Laura_sex_body"

    subpixel True
    pos (0.0, 0.015)
    parallel:
        pause 0.1
        ease 0.2 ypos 0.0
        pause 0.1
        ease 1.6 ypos 0.015
        repeat
    parallel:
        pause 0.1
        ease 0.2 xpos -0.015
        pause 0.1
        ease 1.6 xpos 0.0
        repeat

image Laura_sex_body_animation2:
    animation
    "Laura_sex_body"

    subpixel True
    pos (0.0, 0.015)
    parallel:
        pause 0.1
        ease 0.2 ypos 0.0
        pause 0.1
        ease 1.6 ypos 0.015
        repeat
    parallel:
        pause 0.1
        ease 0.2 xpos -0.015
        pause 0.1
        ease 1.6 xpos 0.0
        repeat

image Laura_sex_body_animation3:
    animation
    "Laura_sex_body"

    subpixel True
    pos (0.0, 0.015)
    parallel:
        pause 0.1
        ease 0.2 ypos 0.0
        pause 0.1
        ease 1.6 ypos 0.015
        repeat
    parallel:
        pause 0.1
        ease 0.2 xpos -0.015
        pause 0.1
        ease 1.6 xpos 0.0
        repeat

image Laura_sex_legs_animation0:
    "Laura_sex_legs"

image Laura_sex_legs_animation1:
    animation
    "Laura_sex_legs"

    subpixel True
    pos (0.0, 0.0)
    parallel:
        pause 0.05
        ease 0.2 ypos -0.02
        easeout 0.45 ypos -0.015
        easein 1.3 ypos 0.0
        repeat
    parallel:
        pause 0.05
        ease 0.2 xpos -0.02
        easeout 0.45 xpos -0.015
        easein 1.3 xpos 0.0
        repeat

image Laura_sex_legs_animation2:
    animation
    "Laura_sex_legs"

    subpixel True
    pos (0.0, 0.0)
    parallel:
        pause 0.05
        ease 0.2 ypos -0.02
        easeout 0.45 ypos -0.015
        easein 1.3 ypos 0.0
        repeat
    parallel:
        pause 0.05
        ease 0.2 xpos -0.02
        easeout 0.45 xpos -0.015
        easein 1.3 xpos 0.0
        repeat

image Laura_sex_legs_animation3:
    animation
    "Laura_sex_legs"

    subpixel True
    pos (0.0, 0.0)
    parallel:
        pause 0.05
        ease 0.2 ypos -0.02
        easeout 0.45 ypos -0.015
        easein 1.3 ypos 0.0
        repeat
    parallel:
        pause 0.05
        ease 0.2 xpos -0.02
        easeout 0.45 xpos -0.015
        easein 1.3 xpos 0.0
        repeat

image Laura_sex_feet_animation0:
    "Laura_sex_feet"

image Laura_sex_feet_animation1:
    animation
    "Laura_sex_feet"

    subpixel True
    pos (0.0, 0.0)
    parallel:
        pause 0.05
        ease 0.2 ypos -0.02
        easeout 0.45 ypos -0.015
        easein 1.3 ypos 0.0
        repeat
    parallel:
        pause 0.05
        ease 0.2 xpos -0.02
        easeout 0.45 xpos -0.015
        easein 1.3 xpos 0.0
        repeat

image Laura_sex_feet_animation2:
    animation
    "Laura_sex_feet"

    subpixel True
    pos (0.0, 0.0)
    parallel:
        pause 0.05
        ease 0.2 ypos -0.02
        easeout 0.45 ypos -0.015
        easein 1.3 ypos 0.0
        repeat
    parallel:
        pause 0.05
        ease 0.2 xpos -0.02
        easeout 0.45 xpos -0.015
        easein 1.3 xpos 0.0
        repeat

image Laura_sex_feet_animation3:
    animation
    "Laura_sex_feet"

    subpixel True
    pos (0.0, 0.0)
    parallel:
        pause 0.05
        ease 0.2 ypos -0.02
        easeout 0.45 ypos -0.015
        easein 1.3 ypos 0.0
        repeat
    parallel:
        pause 0.05
        ease 0.2 xpos -0.02
        easeout 0.45 xpos -0.015
        easein 1.3 xpos 0.0
        repeat

image Laura_sex_pussy_animation0:
    "characters/Laura/images/sex/pussy_closed.webp"

    anchor (0.5, 0.5)

image Laura_sex_pussy_animation1:
    animation
    "characters/Laura/images/sex/pussy_open.webp"

    subpixel True
    anchor (0.5, 0.5)
    block:
        ease 0.2 zoom 1.025
        easeout 0.5 zoom 1.015
        easein 1.3 zoom 1.0
        repeat

image Laura_sex_pussy_animation2:
    animation
    "characters/Laura/images/sex/pussy_penetrated.webp"

    subpixel True
    anchor (0.5, 0.5)
    block:
        ease 0.2 zoom 1.025
        easeout 0.5 zoom 1.015
        easein 1.3 zoom 1.0
        repeat

image Laura_sex_pussy_animation3:
    animation
    "characters/Laura/images/sex/pussy_penetrated.webp"

    subpixel True
    anchor (0.5, 0.5)
    block:
        ease 0.2 zoom 1.025
        easeout 0.5 zoom 1.015
        easein 1.3 zoom 1.0
        repeat

image Laura_sex_anus_animation0:
    "characters/Laura/images/sex/anus_closed.webp"

    anchor (0.5, 0.5)

image Laura_sex_anus_animation1:
    animation
    "characters/Laura/images/sex/anus_open.webp"

    subpixel True
    anchor (0.5, 0.5)
    block:
        ease 0.2 zoom 1.03
        easeout 0.5 zoom 1.02
        easein 1.3 zoom 1.0
        repeat

image Laura_sex_anus_animation2:
    animation
    "characters/Laura/images/sex/anus_penetrated.webp"

    subpixel True
    anchor (0.5, 0.5)
    block:
        ease 0.2 zoom 1.03
        easeout 0.5 zoom 1.02
        easein 1.3 zoom 1.0
        repeat

image Laura_sex_anus_animation3:
    animation
    "characters/Laura/images/sex/anus_penetrated.webp"

    subpixel True
    anchor (0.5, 0.5)
    block:
        ease 0.2 zoom 1.03
        easeout 0.5 zoom 1.02
        easein 1.3 zoom 1.0
        repeat

image Laura_sex_cock_animation0:
    "Zero_cock"

image Laura_sex_cock_animation1:
    animation
    "Zero_cock"

    subpixel True
    pos (0.0, 0.0)
    parallel:
        ease 0.2 ypos -0.05
        easeout 0.5 ypos -0.04
        easein 1.5 ypos 0.0
        repeat
    parallel:
        ease 0.2 xpos -0.04
        easeout 0.5 xpos -0.03
        easein 1.5 xpos 0.0
        repeat

image Laura_sex_cock_animation2:
    animation
    "Zero_cock"

    subpixel True
    pos (0.0, 0.0)
    parallel:
        ease 0.2 ypos -0.05
        easeout 0.5 ypos -0.04
        easein 1.5 ypos 0.0
        repeat
    parallel:
        ease 0.2 xpos -0.04
        easeout 0.5 xpos -0.03
        easein 1.5 xpos 0.0
        repeat

image Laura_sex_cock_animation3:
    animation
    "Zero_cock"

    subpixel True
    pos (0.0, 0.0)
    parallel:
        ease 0.2 ypos -0.05
        easeout 0.5 ypos -0.04
        easein 1.5 ypos 0.0
        repeat
    parallel:
        ease 0.2 xpos -0.04
        easeout 0.5 xpos -0.03
        easein 1.5 xpos 0.0
        repeat

image Laura_sex_cock_anal_animation0:
    "Zero_cock"

image Laura_sex_cock_anal_animation1:
    animation
    "Zero_cock"

    subpixel True
    pos (0.0, 0.0)
    parallel:
        ease 0.2 ypos -0.05
        easeout 0.5 ypos -0.04
        easein 1.5 ypos 0.0
        repeat
    parallel:
        ease 0.2 xpos -0.04
        easeout 0.5 xpos -0.03
        easein 1.5 xpos 0.0
        repeat

image Laura_sex_cock_anal_animation2:
    animation
    "Zero_cock"

    subpixel True
    pos (0.0, 0.0)
    parallel:
        ease 0.2 ypos -0.05
        easeout 0.5 ypos -0.04
        easein 1.5 ypos 0.0
        repeat
    parallel:
        ease 0.2 xpos -0.04
        easeout 0.5 xpos -0.03
        easein 1.5 xpos 0.0
        repeat

image Laura_sex_cock_anal_animation3:
    animation
    "Zero_cock"

    subpixel True
    pos (0.0, 0.0)
    parallel:
        ease 0.2 ypos -0.05
        easeout 0.5 ypos -0.04
        easein 1.5 ypos 0.0
        repeat
    parallel:
        ease 0.2 xpos -0.04
        easeout 0.5 xpos -0.03
        easein 1.5 xpos 0.0
        repeat

layeredimage Laura_sex_cock_animations:
    if Player.cock_Action.type == "sex":
        "Laura_sex_cock_animation[Player.cock_Action.speed]" offset (150, 205) rotate -35 zoom 1.25
    elif Player.cock_Action.type == "anal":
        "Laura_sex_cock_anal_animation[Player.cock_Action.speed]" offset (150, 250) rotate -35 zoom 1.25

image Laura_sprite sex:
    contains:
        ConditionSwitch(
            "Laura in Player.cock_Action.Actors", "Laura_sex_right_hand_animation[Player.cock_Action.speed]",
            "True", "Laura_sex_right_hand_animation0")
    contains:
        ConditionSwitch(
            "Laura in Player.cock_Action.Actors", "Laura_sex_body_animation[Player.cock_Action.speed]",
            "True", "Laura_sex_body_animation0")

    contains:
        ConditionSwitch(
            "Laura in Player.cock_Action.Actors", "Laura_sex_legs_animation[Player.cock_Action.speed]",
            "True", "Laura_sex_legs_animation0")

    # contains:
    #     "Laura_sex_cock_animations"

    contains:
        ConditionSwitch(
            "Laura in Player.cock_Action.Actors", "Laura_sex_feet_animation[Player.cock_Action.speed]",
            "True", "Laura_sex_feet_animation0")

    anchor (0.5, 0.0) offset (1100, 1100) zoom 0.6
