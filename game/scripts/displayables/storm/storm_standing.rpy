layeredimage Storm_sprite standing:
    if Storm.arm_pose == 2:
        "images/Storm_standing/Storm_standing_right_arm_[Storm.arm_pose].webp"

    always:
        "images/Storm_standing/Storm_standing_body.webp"

    if Storm.tan["bottom"]:
        "images/Storm_standing/Storm_standing_tan_lines_bottom.webp"

    if Storm.pubes:
        "images/Storm_standing/Storm_standing_pubes_[Storm.pubes].webp"

    always:
        "images/Storm_standing/Storm_standing_breasts.webp"

    if Storm.tan["top"]:
        "images/Storm_standing/Storm_standing_tan_lines_top.webp"

    if Storm.arm_pose == 1:
        "images/Storm_standing/Storm_standing_right_arm[Storm.arm_pose].webp"

    always:
        "images/Storm_standing/Storm_standing_left_arm.webp"

    anchor (0.5, 0.0) offset (0, -95) zoom 0.6

image Storm_standing_blinking:
    "images/Storm_standing/Storm_standing_eyes_[Storm.eyes].webp"
    choice:
        3.5
    choice:
        3.25
    choice:
        3
    "images/Storm_standing/Storm_standing_eyes_half_blink.webp"
    0.05
    "images/Storm_standing/Storm_standing_eyes_closed.webp"
    0.15
    "images/Storm_standing/Storm_standing_eyes_half_blink.webp"
    0.05
    repeat
