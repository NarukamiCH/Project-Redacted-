layeredimage Rogue_sprite standing:
    always:
        "characters/Rogue/images/standing/hair_back.webp"

    always:
        "characters/Rogue/images/standing/right_arm[Rogue.arm_pose].webp"

    if Rogue.Clothes["gloves"].string == "black_gloves":
        "characters/Rogue/images/standing/gloves_black_gloves_right[Rogue.arm_pose].webp"

    if Rogue.Clothes["bodysuit"].string:
        "characters/Rogue/images/standing/bodysuit_[Rogue.Clothes[bodysuit].string]_right_sleeve[Rogue.arm_pose].webp"

    if Rogue.Clothes["sleeves"].string:
        "characters/Rogue/images/standing/sleeves_[Rogue.Clothes[sleeves].string]_right[Rogue.arm_pose].webp"

    if Rogue.Clothes["top"].string:
        "characters/Rogue/images/standing/top_[Rogue.Clothes[top].string]_right_sleeve[Rogue.arm_pose].webp"

    if Rogue.Clothes["jacket"].string:
        "characters/Rogue/images/standing/jacket_[Rogue.Clothes[jacket].string]_right_sleeve[Rogue.arm_pose].webp"

    if Rogue.Clothes["gloves"].string == "yellow_gloves":
        "characters/Rogue/images/standing/gloves_yellow_gloves_right[Rogue.arm_pose].webp"

    always:
        "characters/Rogue/images/standing/body.webp"

    if Rogue.tan_lines["bottom"]:
        "characters/Rogue/images/standing/tan_lines_bottom.webp"

    if Rogue.piercings["labia"] in ["barbell", "both"]:
        "characters/Rogue/images/standing/labia_piercings_barbell.webp"

    if Rogue.piercings["labia"] in ["ring", "both"]:
        "characters/Rogue/images/standing/labia_piercings_ring.webp"

    if Rogue.pubes:
        "characters/Rogue/images/standing/pubes_[Rogue.pubes].webp"

    if Rogue.Clothes["socks"].string:
        "characters/Rogue/images/standing/socks_[Rogue.Clothes[socks].string].webp"

    if Rogue.Clothes["underwear"].string:
        "characters/Rogue/images/standing/underwear_[Rogue.Clothes[underwear].string]_[Rogue.Clothes[underwear].state].webp"

    if Rogue.piercings["belly"]:
        "characters/Rogue/images/standing/belly_piercing.webp"

    if Rogue.Clothes["hose"].string:
        "characters/Rogue/images/standing/hose_[Rogue.Clothes[hose].string]_[Rogue.Clothes[hose].state].webp"

    always:
        "characters/Rogue/images/standing/breasts.webp"

    if Rogue.tan_lines["top"]:
        "characters/Rogue/images/standing/tan_lines_top.webp"

    if Rogue.piercings["nipple"] in ["barbell", "both"]:
        "characters/Rogue/images/standing/nipple_piercings_barbell.webp"

    if Rogue.piercings["nipple"] in ["ring", "both"]:
        "characters/Rogue/images/standing/nipple_piercings_ring.webp"

    if Rogue.Clothes["bodysuit"].string:
        "characters/Rogue/images/standing/bodysuit_[Rogue.Clothes[bodysuit].string].webp"

    if Rogue.Clothes["pants"].string:
        "characters/Rogue/images/standing/pants_[Rogue.Clothes[pants].string]_[Rogue.Clothes[pants].state].webp"

    if Rogue.Clothes["boots"].string:
        "characters/Rogue/images/standing/boots_[Rogue.Clothes[boots].string].webp"

    if Rogue.Clothes["skirt"].string:
        "characters/Rogue/images/standing/skirt_[Rogue.Clothes[skirt].string]_[Rogue.Clothes[skirt].state].webp"

    if Rogue.Clothes["bra"].string:
        "characters/Rogue/images/standing/bra_[Rogue.Clothes[bra].string]_[Rogue.Clothes[bra].state].webp"

    if Rogue.Clothes["dress"].string:
        "characters/Rogue/images/standing/dress_[Rogue.Clothes[dress].string]_[Rogue.Clothes[dress].state].webp"

    if Rogue.piercings["nipple"] not in ["barbell", "both"]:
        Null()
    elif Rogue.Clothes["dress"].string and Rogue.Clothes["dress"].state == 0:
        "characters/Rogue/images/standing/nipple_piercings_barbell_covered.webp"
    elif Rogue.Clothes["bra"].string and Rogue.Clothes["bra"].state == 0:
        "characters/Rogue/images/standing/nipple_piercings_barbell_covered.webp"
    elif Rogue.Clothes["bodysuit"].string:
        "characters/Rogue/images/standing/nipple_piercings_barbell_covered.webp"

    if Rogue.piercings["nipple"] not in ["ring", "both"]:
        Null()
    elif Rogue.Clothes["dress"].string and Rogue.Clothes["dress"].state == 0:
        "characters/Rogue/images/standing/nipple_piercings_ring_covered.webp"
    elif Rogue.Clothes["bra"].string and Rogue.Clothes["bra"].state == 0:
        "characters/Rogue/images/standing/nipple_piercings_ring_covered.webp"
    elif Rogue.Clothes["bodysuit"].string:
        "characters/Rogue/images/standing/nipple_piercings_ring_covered.webp"

    if Rogue.Clothes["belt"].string:
        "characters/Rogue/images/standing/belt_[Rogue.Clothes[belt].string].webp"

    if Rogue.Clothes["top"].string:
        "characters/Rogue/images/standing/top_[Rogue.Clothes[top].string]_[Rogue.Clothes[top].state].webp"

    if Rogue.Clothes["jacket"].string:
        "characters/Rogue/images/standing/jacket_[Rogue.Clothes[jacket].string]_[Rogue.Clothes[jacket].state].webp"

    if Rogue.Clothes["neck"].string:
        "characters/Rogue/images/standing/neck_[Rogue.Clothes[neck].string].webp"

    always:
        "characters/Rogue/images/standing/head.webp"

    if Rogue.eyes in ["closed", "down", "side", "squint", "up"]:
        "characters/Rogue/images/standing/eyes_[Rogue.eyes].webp"
    else:
        "Rogue_standing_blinking"

    always:
        "characters/Rogue/images/standing/brows_[Rogue.brows].webp"

    if Rogue.Clothes["makeup"].string:
        "characters/Rogue/images/standing/makeup_[Rogue.Clothes[makeup].string].webp"

    always:
        "characters/Rogue/images/standing/mouth_[Rogue.mouth].webp"

    if Rogue.blush:
        "characters/Rogue/images/standing/blush[Rogue.blush].webp"

    if Rogue.Clothes["face_inner_accessory"].string:
        "characters/Rogue/images/standing/face_inner_accessory_[Rogue.Clothes[face_inner_accessory].string].webp"

    if Rogue.wet:
        "characters/Rogue/images/standing/hair_wet.webp"
    else:
        "characters/Rogue/images/standing/hair_[Rogue.Clothes[hair].string].webp"

    always:
        "characters/Rogue/images/standing/left_arm[Rogue.arm_pose].webp"

    if Rogue.Clothes["gloves"].string == "black_gloves":
        "characters/Rogue/images/standing/gloves_black_gloves_left[Rogue.arm_pose].webp"

    if Rogue.Clothes["bodysuit"].string:
        "characters/Rogue/images/standing/bodysuit_[Rogue.Clothes[bodysuit].string]_left_sleeve[Rogue.arm_pose].webp"

    if Rogue.Clothes["sleeves"].string:
        "characters/Rogue/images/standing/sleeves_[Rogue.Clothes[sleeves].string]_left[Rogue.arm_pose].webp"

    if Rogue.Clothes["top"].string:
        "characters/Rogue/images/standing/top_[Rogue.Clothes[top].string]_left_sleeve[Rogue.arm_pose].webp"

    if not Rogue.Clothes["jacket"].string:
        Null()
    elif Rogue.arm_pose == 1:
        "characters/Rogue/images/standing/jacket_[Rogue.Clothes[jacket].string]_left_sleeve1_[Rogue.Clothes[jacket].state].webp"
    else:
        "characters/Rogue/images/standing/jacket_[Rogue.Clothes[jacket].string]_left_sleeve2.webp"

    if Rogue.Clothes["gloves"].string == "yellow_gloves":
        "characters/Rogue/images/standing/gloves_yellow_gloves_left[Rogue.arm_pose].webp"

    anchor (0.5, 0.0) offset (0, 50) zoom 0.62

image Rogue_standing_blinking:
    f"characters/Rogue/images/standing/eyes_{Rogue.eyes}.webp"
    choice:
        4.5
    choice:
        4.0
    choice:
        3.5
    "characters/Rogue/images/standing/eyes_blink1.webp"
    0.023
    "characters/Rogue/images/standing/eyes_blink2.webp"
    0.023
    "characters/Rogue/images/standing/eyes_closed.webp"
    0.054
    "characters/Rogue/images/standing/eyes_blink2.webp"
    0.018
    "characters/Rogue/images/standing/eyes_blink1.webp"
    0.072
    repeat
