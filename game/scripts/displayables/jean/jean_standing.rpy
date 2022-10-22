layeredimage Jean_sprite standing:
    always:
        "images/Jean_standing/Jean_standing_right_arm[Jean.arm_pose].webp"

    always:
        "images/Jean_standing/Jean_standing_body.webp"

    if Jean.pubes:
        "images/Jean_standing/Jean_standing_pubes_[Jean.pubes].webp"

    always:
        "images/Jean_standing/Jean_standing_breasts.webp"

    always:
        "images/Jean_standing/Jean_standing_left_arm.webp"

    anchor (0.5, 0.0) offset (0, -80) zoom 0.6

image Jean_standing_blinking:
    "images/Jean_standing/Jean_standing_eyes_[Jean.eyes].webp"
    choice:
        3.5
    choice:
        3.25
    choice:
        3
    "images/Jean_standing/Jean_standing_eyes_half_blink.webp"
    0.05
    "images/Jean_standing/Jean_standing_eyes_closed.webp"
    0.15
    "images/Jean_standing/Jean_standing_eyes_half_blink.webp"
    0.05
    repeat
