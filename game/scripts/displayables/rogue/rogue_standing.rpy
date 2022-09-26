layeredimage Rogue_sprite standing:
    always:
        "images/Rogue_standing/Rogue_standing_body.png"

    if Rogue.pubes:
        "images/Rogue_standing/Rogue_standing_pubes_[Rogue.pubes].png"

    always:
        "images/Rogue_standing/Rogue_standing_breasts.png"

    always:
        "images/Rogue_standing/Rogue_standing_left_arm_[Rogue.arm_pose].png"

    always:
        "images/Rogue_standing/Rogue_standing_right_arm.png"

    anchor (0.5, 0.0) offset (0, 10) zoom 0.8

image Rogue_standing_blinking:
    "images/Rogue_standing/Rogue_standing_eyes_[Rogue.eyes].png"
    choice:
        3.5
    choice:
        3.25
    choice:
        3
    "images/Rogue_standing/Rogue_standing_eyes_half_blink.png"
    0.05
    "images/Rogue_standing/Rogue_standing_eyes_closed.png"
    0.15
    "images/Rogue_standing/Rogue_standing_eyes_half_blink.png"
    0.05
    repeat
