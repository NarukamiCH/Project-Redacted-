layeredimage Daenerys_sprite standing:
    if Daenerys.Clothes["sleeves"].string == "arm_band":
        "characters/Daenerys/images/standing/sleeves_arm_band_right.webp"

    if Daenerys.wet:
        "characters/Daenerys/images/standing/hair_back_wet.webp"
    else:
        "characters/Daenerys/images/standing/hair_back_[Daenerys.Clothes[hair].string].webp"

    always:
        "characters/Daenerys/images/standing/right_arm[Daenerys.arm_pose].webp"

    if Daenerys.Clothes["dress"].string == "war_dress" and Daenerys.Clothes["dress"].state == 0:
        "characters/Daenerys/images/standing/dress_war_dress_right_sleeve[Daenerys.arm_pose].webp"

    always:
        "characters/Daenerys/images/standing/body.webp"

    if Daenerys.tan_lines["bottom"]:
        "characters/Daenerys/images/standing/tan_lines_bottom.webp"

    if Daenerys.piercings["labia"] in ["barbell", "both"]:
        "characters/Daenerys/images/standing/labia_piercings_barbell.webp"

    if Daenerys.piercings["labia"] in ["ring", "both"]:
        "characters/Daenerys/images/standing/labia_piercings_ring.webp"

    if Daenerys.pubes:
        "characters/Daenerys/images/standing/pubes_[Daenerys.pubes].webp"

    always:
        "characters/Daenerys/images/standing/breasts.webp"

    if Daenerys.tan_lines["top"]:
        "characters/Daenerys/images/standing/tan_lines_top.webp"

    if Daenerys.piercings["nipple"] in ["barbell", "both"]:
        "characters/Daenerys/images/standing/nipple_piercings_barbell.webp"

    if Daenerys.piercings["nipple"] in ["ring", "both"]:
        "characters/Daenerys/images/standing/nipple_piercings_ring.webp"

    if Daenerys.Clothes["underwear"].string:
        "characters/Daenerys/images/standing/underwear_[Daenerys.Clothes[underwear].string]_[Daenerys.Clothes[underwear].state].webp"

    if Daenerys.Clothes["bra"].string:
        "characters/Daenerys/images/standing/bra_[Daenerys.Clothes[bra].string]_[Daenerys.Clothes[bra].state].webp"

    if Daenerys.Clothes["dress"].string:
        "characters/Daenerys/images/standing/dress_[Daenerys.Clothes[dress].string]_[Daenerys.Clothes[dress].state].webp"

    if Daenerys.piercings["nipple"] not in ["barbell", "both"]:
        Null()
    elif Daenerys.Clothes["dress"].string and Daenerys.Clothes["dress"].string != "war_dress" and Daenerys.Clothes["dress"].state == 0:
        "characters/Daenerys/images/standing/nipple_piercings_barbell_covered_cloth.webp"
    elif Daenerys.Clothes["bra"].string and Daenerys.Clothes["bra"].state == 0:
        "characters/Daenerys/images/standing/nipple_piercings_barbell_covered_cloth.webp"

    if Daenerys.piercings["nipple"] not in ["ring", "both"]:
        Null()
    elif Daenerys.Clothes["dress"].string and Daenerys.Clothes["dress"].string != "war_dress" and Daenerys.Clothes["dress"].state == 0:
        "characters/Daenerys/images/standing/nipple_piercings_ring_covered_cloth.webp"
    elif Daenerys.Clothes["bra"].string and Daenerys.Clothes["bra"].state == 0:
        "characters/Daenerys/images/standing/nipple_piercings_ring_covered_cloth.webp"

    if not Daenerys.Clothes["top"].string:
        Null()
    elif Daenerys.Clothes["top"].state == 0 or Daenerys.Clothes["top"].string != "towel":
        "characters/Daenerys/images/standing/top_[Daenerys.Clothes[top].string]_[Daenerys.Clothes[top].state].webp"
    elif Daenerys.Clothes["bra"].string and Daenerys.Clothes["bra"].state == 0:
        "characters/Daenerys/images/standing/top_towel_1_[Daenerys.Clothes[bra].string].webp"
    elif Daenerys.Clothes["dress"].string and Daenerys.Clothes["dress"].state == 0:
        "characters/Daenerys/images/standing/top_towel_1_[Daenerys.Clothes[dress].string].webp"

    always:
        "characters/Daenerys/images/standing/left_arm.webp"

    if Daenerys.Clothes["dress"].string == "war_dress" and Daenerys.Clothes["dress"].state == 0:
        "characters/Daenerys/images/standing/dress_war_dress_left_sleeve.webp"

    if not Daenerys.Clothes["sleeves"].string:
        Null()
    elif Daenerys.Clothes["dress"].string == "war_dress" and Daenerys.Clothes["dress"].state == 0:
        "characters/Daenerys/images/standing/sleeves_[Daenerys.Clothes[sleeves].string]_left_above.webp"
    else:
        "characters/Daenerys/images/standing/sleeves_[Daenerys.Clothes[sleeves].string]_left.webp"

    always:
        "characters/Daenerys/images/standing/head.webp"

    if Daenerys.eyes not in ["closed", "down", "side", "squint", "up"]:
        "Daenerys_standing_blinking"
    else:
        "characters/Daenerys/images/standing/eyes_[Daenerys.eyes].webp"

    always:
        "characters/Daenerys/images/standing/brows_[Daenerys.brows].webp"

    always:
        "characters/Daenerys/images/standing/mouth_[Daenerys.mouth].webp"

    if Daenerys.blush:
        "characters/Daenerys/images/standing/blush[Daenerys.blush].webp"

    if Daenerys.wet and Daenerys.Clothes["dress"].string == "war_dress":
        "characters/Daenerys/images/standing/hair_shadow_wet_dark.webp"
    elif Daenerys.wet:
        "characters/Daenerys/images/standing/hair_shadow_wet_warm.webp"
    elif Daenerys.Clothes["dress"].string == "war_dress":
        "characters/Daenerys/images/standing/hair_shadow_[Daenerys.Clothes[hair].string]_dark.webp"
    else:
        "characters/Daenerys/images/standing/hair_shadow_[Daenerys.Clothes[hair].string]_warm.webp"

    if Daenerys.wet:
        "characters/Daenerys/images/standing/hair_wet.webp"
    else:
        "characters/Daenerys/images/standing/hair_[Daenerys.Clothes[hair].string].webp"

    anchor (0.5, 0.0) offset (0, 70) zoom 0.635

image Daenerys_standing_blinking:
    f"characters/Daenerys/images/standing/eyes_{Daenerys.eyes}.webp"
    choice:
        4.5
    choice:
        4.0
    choice:
        3.5
    "characters/Daenerys/images/standing/eyes_blink1.webp"
    0.023
    "characters/Daenerys/images/standing/eyes_blink2.webp"
    0.023
    "characters/Daenerys/images/standing/eyes_closed.webp"
    0.065
    "characters/Daenerys/images/standing/eyes_blink2.webp"
    0.018
    "characters/Daenerys/images/standing/eyes_blink1.webp"
    0.072
    repeat