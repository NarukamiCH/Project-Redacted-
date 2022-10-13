layeredimage Storm_sprite standing:
    if Storm.arm_pose == 2:
        "images/Storm_standing/Storm_standing_right_arm_[Storm.arm_pose].png"

    always:
        "images/Storm_standing/Storm_standing_body.png"

    if Storm.tan["bottom"]:
        "images/Storm_standing/Storm_standing_tan_lines_bottom.png"

    if Storm.pubes:
        "images/Storm_standing/Storm_standing_pubes_[Storm.pubes].png"

    always:
        "images/Storm_standing/Storm_standing_breasts.png"

    if Storm.tan["top"]:
        "images/Storm_standing/Storm_standing_tan_lines_top.png"

    if Storm.arm_pose == 1:
        "images/Storm_standing/Storm_standing_right_arm[Storm.arm_pose].png"

    always:
        "images/Storm_standing/Storm_standing_left_arm.png"

    anchor (0.5, 0.0) offset (0, -95) zoom 0.6

image Storm_standing_blinking:
    "images/Storm_standing/Storm_standing_eyes_[Storm.eyes].png"
    choice:
        3.5
    choice:
        3.25
    choice:
        3
    "images/Storm_standing/Storm_standing_eyes_half_blink.png"
    0.05
    "images/Storm_standing/Storm_standing_eyes_closed.png"
    0.15
    "images/Storm_standing/Storm_standing_eyes_half_blink.png"
    0.05
    repeat
