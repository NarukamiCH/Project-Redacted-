layeredimage Daenerys_sprite standing:
    if Daenerys.Clothes["sleeves"].string == "arm_band":
        "images/Daenerys_standing/sleeves_arm_band_right.webp"

    if Daenerys.wet:
        "images/Daenerys_standing/hair_back_wet.webp"
    else:
        "images/Daenerys_standing/hair_back_[Daenerys.Clothes[hair].string].webp"

    always:
        "images/Daenerys_standing/right_arm[Daenerys.arm_pose].webp"

    if Daenerys.Clothes["dress"].string == "war_dress" and Daenerys.Clothes["dress"].state == 0:
        "images/Daenerys_standing/dress_war_dress_right_sleeve[Daenerys.arm_pose].webp"

    always:
        "images/Daenerys_standing/body.webp"

    if Daenerys.tan_lines["bottom"]:
        "images/Daenerys_standing/tan_lines_bottom.webp"

    if Daenerys.piercings["labia"] in ["barbell", "both"]:
        "images/Daenerys_standing/labia_piercings_barbell.webp"

    if Daenerys.piercings["labia"] in ["ring", "both"]:
        "images/Daenerys_standing/labia_piercings_ring.webp"

    if Daenerys.pubes:
        "images/Daenerys_standing/pubes_[Daenerys.pubes].webp"

    always:
        "images/Daenerys_standing/breasts.webp"

    if Daenerys.tan_lines["top"]:
        "images/Daenerys_standing/tan_lines_top.webp"

    if Daenerys.piercings["nipple"] in ["barbell", "both"]:
        "images/Daenerys_standing/nipple_piercings_barbell.webp"

    if Daenerys.piercings["nipple"] in ["ring", "both"]:
        "images/Daenerys_standing/nipple_piercings_ring.webp"

    if Daenerys.Clothes["underwear"].string:
        "images/Daenerys_standing/underwear_[Daenerys.Clothes[underwear].string]_[Daenerys.Clothes[underwear].state].webp"

    if Daenerys.Clothes["bra"].string:
        "images/Daenerys_standing/bra_[Daenerys.Clothes[bra].string]_[Daenerys.Clothes[bra].state].webp"

    if Daenerys.Clothes["dress"].string:
        "images/Daenerys_standing/dress_[Daenerys.Clothes[dress].string]_[Daenerys.Clothes[dress].state].webp"

    if Daenerys.piercings["nipple"] in ["barbell", "both"] and (Daenerys.Clothes["bra"].string or Daenerys.Clothes["dress"].string == "cloth_dress"):
        "images/Daenerys_standing/nipple_piercings_barbell_covered.webp"

    if Daenerys.piercings["nipple"] in ["ring", "both"] and (Daenerys.Clothes["bra"].string or Daenerys.Clothes["dress"].string == "cloth_dress"):
        "images/Daenerys_standing/nipple_piercings_ring_covered.webp"

    if not Daenerys.Clothes["top"].string:
        Null()
    elif Daenerys.Clothes["top"].state == 0 or Daenerys.Clothes["top"].string != "towel":
        "images/Daenerys_standing/top_[Daenerys.Clothes[top].string]_[Daenerys.Clothes[top].state].webp"
    elif Daenerys.Clothes["bra"].string and Daenerys.Clothes["bra"].state == 0:
        "images/Daenerys_standing/top_towel_1_[Daenerys.Clothes[bra].string].webp"
    elif Daenerys.Clothes["dress"].string and Daenerys.Clothes["dress"].state == 0:
        "images/Daenerys_standing/top_towel_1_[Daenerys.Clothes[dress].string].webp"

    always:
        "images/Daenerys_standing/left_arm.webp"

    if Daenerys.Clothes["dress"].string == "war_dress" and Daenerys.Clothes["dress"].state == 0:
        "images/Daenerys_standing/dress_war_dress_left_sleeve.webp"

    if not Daenerys.Clothes["sleeves"].string:
        Null()
    elif Daenerys.Clothes["dress"].string == "war_dress" and Daenerys.Clothes["dress"].state == 0:
        "images/Daenerys_standing/sleeves_[Daenerys.Clothes[sleeves].string]_left_above.webp"
    else:
        "images/Daenerys_standing/sleeves_[Daenerys.Clothes[sleeves].string]_left.webp"

    always:
        "images/Daenerys_standing/head.webp"

    always:
        "images/Daenerys_standing/brows_[Daenerys.brows].webp"

    if Daenerys.eyes not in ["closed", "down", "side", "squint", "up"]:
        "Daenerys_standing_blinking"
    else:
        "images/Daenerys_standing/eyes_[Daenerys.eyes].webp"

    always:
        "images/Daenerys_standing/mouth_[Daenerys.mouth].webp"

    if Daenerys.blush:
        "images/Daenerys_standing/blush[Daenerys.blush].webp"

    if Daenerys.wet and Daenerys.Clothes["dress"].string == "war_dress":
        "images/Daenerys_standing/hair_shadow_wet_war_dress.webp"
    elif Daenerys.wet:
        "images/Daenerys_standing/hair_shadow_wet.webp"
    elif Daenerys.Clothes["dress"].string == "war_dress":
        "images/Daenerys_standing/hair_shadow_[Daenerys.Clothes[hair].string]_war_dress.webp"
    else:
        "images/Daenerys_standing/hair_shadow_[Daenerys.Clothes[hair].string].webp"

    if Daenerys.wet:
        "images/Daenerys_standing/hair_wet.webp"
    else:
        "images/Daenerys_standing/hair_[Daenerys.Clothes[hair].string].webp"

    anchor (0.5, 0.0) offset (0, 50) zoom 0.6

image Daenerys_standing_blinking:
    f"images/Daenerys_standing/eyes_{Daenerys.eyes}.webp"
    choice:
        4.5
    choice:
        4.0
    choice:
        3.5
    "images/Daenerys_standing/eyes_blink1.webp"
    0.018
    "images/Daenerys_standing/eyes_blink2.webp"
    0.018
    "images/Daenerys_standing/eyes_closed.webp"
    0.036
    "images/Daenerys_standing/eyes_blink2.webp"
    0.012
    "images/Daenerys_standing/eyes_blink1.webp"
    0.048
    repeat