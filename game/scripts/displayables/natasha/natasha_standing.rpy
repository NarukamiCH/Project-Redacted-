layeredimage Natasha_sprite standing:
    always:
        "images/Natasha_standing/Natasha_standing_body.png"

    if Natasha.pubes:
        "images/Natasha_standing/Natasha_standing_pubes_[Natasha.pubes].png"

    always:
        "images/Natasha_standing/Natasha_standing_breasts.png"

    always:
        "images/Natasha_standing/Natasha_standing_left_arm[Natasha.arm_pose].png"

    always:
        "images/Natasha_standing/Natasha_standing_right_arm.png"

    anchor (0.5, 0.0) offset (0, -70) zoom 0.58

image Natasha_standing_blinking:
    "images/Natasha_standing/Natasha_standing_eyes_[Natasha.eyes].png"
    choice:
        3.5
    choice:
        3.25
    choice:
        3
    "images/Natasha_standing/Natasha_standing_eyes_half_blink.png"
    0.05
    "images/Natasha_standing/Natasha_standing_eyes_closed.png"
    0.15
    "images/Natasha_standing/Natasha_standing_eyes_half_blink.png"
    0.05
    repeat
