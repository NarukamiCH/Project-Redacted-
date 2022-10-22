layeredimage Kitty_sprite standing:
    always:
        "images/Kitty_standing/Kitty_standing_body.webp"

    if Kitty.pubes:
        "images/Kitty_standing/Kitty_standing_pubes_[Kitty.pubes].webp"

    always:
        "images/Kitty_standing/Kitty_standing_breasts.webp"

    always:
        "images/Kitty_standing/Kitty_standing_left_arm.webp"

    always:
        "images/Kitty_standing/Kitty_standing_right_arm[Kitty.arm_pose].webp"

    anchor (0.5, 0.0) offset (0, -220) zoom 0.67

image Kitty_standing_blinking:
    "images/Kitty_standing/Kitty_standing_eyes_[Kitty.eyes].webp"
    choice:
        3.5
    choice:
        3.25
    choice:
        3
    "images/Kitty_standing/Kitty_standing_eyes_half_blink.webp"
    0.05
    "images/Kitty_standing/Kitty_standing_eyes_closed.webp"
    0.15
    "images/Kitty_standing/Kitty_standing_eyes_half_blink.webp"
    0.05
    repeat
