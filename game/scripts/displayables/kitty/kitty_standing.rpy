layeredimage Kitty_sprite standing:
    always:
        "images/Kitty_standing/Kitty_standing_body.png"

    if Kitty.pubes:
        "images/Kitty_standing/Kitty_standing_pubes_[Kitty.pubes].png"

    always:
        "images/Kitty_standing/Kitty_standing_breasts.png"

    always:
        "images/Kitty_standing/Kitty_standing_left_arm.png"

    always:
        "images/Kitty_standing/Kitty_standing_right_arm[Kitty.arm_pose].png"

    anchor (0.5, 0.0) offset (0, -220) zoom 0.67

image Kitty_standing_blinking:
    "images/Kitty_standing/Kitty_standing_eyes_[Kitty.eyes].png"
    choice:
        3.5
    choice:
        3.25
    choice:
        3
    "images/Kitty_standing/Kitty_standing_eyes_half_blink.png"
    0.05
    "images/Kitty_standing/Kitty_standing_eyes_closed.png"
    0.15
    "images/Kitty_standing/Kitty_standing_eyes_half_blink.png"
    0.05
    repeat
