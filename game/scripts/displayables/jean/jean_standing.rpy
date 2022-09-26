layeredimage Jean_sprite standing:
    always:
        "images/Jean_standing/Jean_standing_right_arm_[Jean.arm_pose].png"

    always:
        "images/Jean_standing/Jean_standing_body.png"

    if Jean.pubes:
        "images/Jean_standing/Jean_standing_pubes_[Jean.pubes].png"

    always:
        "images/Jean_standing/Jean_standing_breasts.png"

    always:
        "images/Jean_standing/Jean_standing_left_arm.png"

    anchor (0.5, 0.0) offset (0, -10) zoom 0.84

image Jean_standing_blinking:
    "images/Jean_standing/Jean_standing_eyes_[Jean.eyes].png"
    choice:
        3.5
    choice:
        3.25
    choice:
        3
    "images/Jean_standing/Jean_standing_eyes_half_blink.png"
    0.05
    "images/Jean_standing/Jean_standing_eyes_closed.png"
    0.15
    "images/Jean_standing/Jean_standing_eyes_half_blink.png"
    0.05
    repeat
