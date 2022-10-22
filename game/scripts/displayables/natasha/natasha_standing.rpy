layeredimage Natasha_sprite standing:
    always:
        "images/Natasha_standing/Natasha_standing_body.webp"

    if Natasha.pubes:
        "images/Natasha_standing/Natasha_standing_pubes_[Natasha.pubes].webp"

    always:
        "images/Natasha_standing/Natasha_standing_breasts.webp"

    always:
        "images/Natasha_standing/Natasha_standing_left_arm[Natasha.arm_pose].webp"

    always:
        "images/Natasha_standing/Natasha_standing_right_arm.webp"

    anchor (0.5, 0.0) offset (0, -70) zoom 0.58

image Natasha_standing_blinking:
    "images/Natasha_standing/Natasha_standing_eyes_[Natasha.eyes].webp"
    choice:
        3.5
    choice:
        3.25
    choice:
        3
    "images/Natasha_standing/Natasha_standing_eyes_half_blink.webp"
    0.05
    "images/Natasha_standing/Natasha_standing_eyes_closed.webp"
    0.15
    "images/Natasha_standing/Natasha_standing_eyes_half_blink.webp"
    0.05
    repeat
