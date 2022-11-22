layeredimage Laura_sprite standing:
    if Laura.Clothes["face_outer_accessory"].string:
        "characters/Laura/images/standing/hair_back_mask.webp"
    else:
        "characters/Laura/images/standing/hair_back.webp"

    if Laura.claws:
        "characters/Laura/images/standing/right_claws.webp"

    always:
        "characters/Laura/images/standing/right_arm.webp"

    if Laura.Clothes["gloves"].string:
        "characters/Laura/images/standing/gloves_[Laura.Clothes[gloves].string]_right.webp"

    if Laura.Clothes["bodysuit"].string in ["blackyellow_Wolverine_suit", "blueyellow_Wolverine_suit"]:
        "characters/Laura/images/standing/bodysuit_[Laura.Clothes[bodysuit].string]_right_sleeve.webp"

    if Laura.Clothes["jacket"].string:
        "characters/Laura/images/standing/jacket_[Laura.Clothes[jacket].string]_right_sleeve.webp"

    always:
        "characters/Laura/images/standing/body.webp"

    if Laura.tan_lines["bottom"]:
        "characters/Laura/images/standing/tan_lines_bottom.webp"

    if Laura.piercings["labia"] in ["barbell", "both"]:
        "characters/Laura/images/standing/labia_piercings_barbell.webp"

    if Laura.piercings["labia"] in ["ring", "both"]:
        "characters/Laura/images/standing/labia_piercings_ring.webp"

    if Laura.pubes:
        "characters/Laura/images/standing/pubes_[Laura.pubes].webp"

    always:
        "characters/Laura/images/standing/breasts.webp"

    if Laura.tan_lines["top"]:
        "characters/Laura/images/standing/tan_lines_top.webp"

    if Laura.piercings["nipple"] in ["barbell", "both"]:
        "characters/Laura/images/standing/nipple_piercings_barbell.webp"

    if Laura.piercings["nipple"] in ["ring", "both"]:
        "characters/Laura/images/standing/nipple_piercings_ring.webp"

    if Laura.Clothes["socks"].string:
        "characters/Laura/images/standing/bodysuit_[Laura.Clothes[socks].string].webp"

    if Laura.Clothes["underwear"].string:
        "characters/Laura/images/standing/underwear_[Laura.Clothes[underwear].string]_[Laura.Clothes[underwear].state].webp"

    if Laura.piercings["labia"] not in ["barbell", "both"]:
        Null()
    elif Laura.Clothes["underwear"].string == "grey_panties" and Laura.Clothes["underwear"].state == 0:
        "characters/Laura/images/standing/labia_piercings_barbell_covered_grey_panties.webp"

    if Laura.piercings["labia"] not in ["ring", "both"]:
        Null()
    elif Laura.Clothes["underwear"].string == "grey_panties" and Laura.Clothes["underwear"].state == 0:
        "characters/Laura/images/standing/labia_piercings_ring_covered_grey_panties.webp"

    if Laura.Clothes["hose"].string:
        "characters/Laura/images/standing/bodysuit_[Laura.Clothes[hose].string].webp"

    if Laura.Clothes["bodysuit"].string:
        "characters/Laura/images/standing/bodysuit_[Laura.Clothes[bodysuit].string]_[Laura.Clothes[bodysuit].state].webp"

    if Laura.Clothes["pants"].string:
        "characters/Laura/images/standing/pants_[Laura.Clothes[pants].string]_[Laura.Clothes[pants].state].webp"

    if Laura.Clothes["boots"].string:
        "characters/Laura/images/standing/boots_[Laura.Clothes[boots].string].webp"

    if Laura.Clothes["skirt"].string:
        "characters/Laura/images/standing/skirt_[Laura.Clothes[skirt].string]_[Laura.Clothes[skirt].state].webp"

    if not Laura.Clothes["belt"].string:
        Null()
    elif Laura.Clothes["bodysuit"].string in ["blackyellow_Wolverine_suit", "blueyellow_Wolverine_suit"]:
        "characters/Laura/images/standing/belt_[Laura.Clothes[belt].string]_high.webp"
    else:
        "characters/Laura/images/standing/belt_[Laura.Clothes[belt].string]_low.webp"

    if Laura.Clothes["bra"].string:
        "characters/Laura/images/standing/bra_[Laura.Clothes[bra].string]_[Laura.Clothes[bra].state].webp"

    if Laura.Clothes["dress"].string:
        "characters/Laura/images/standing/dress_[Laura.Clothes[dress].string]_[Laura.Clothes[dress].state].webp"

    if Laura.piercings["nipple"] not in ["barbell", "both"]:
        Null()
    elif Laura.Clothes["dress"].string and Laura.Clothes["dress"].state == 0:
        "characters/Laura/images/standing/nipple_piercings_barbell_covered_[Laura.Clothes[dress].string].webp"
    elif Laura.Clothes["bra"].string in ["black_lace_bra", "white_tanktop"] and Laura.Clothes["bra"].state == 0:
        "characters/Laura/images/standing/nipple_piercings_barbell_covered_[Laura.Clothes[bra].string].webp"
    elif Laura.Clothes["bodysuit"].string and Laura.Clothes["bodysuit"].state == 0:
        "characters/Laura/images/standing/nipple_piercings_barbell_covered_[Laura.Clothes[bodysuit].string].webp"

    if Laura.piercings["nipple"] not in ["ring", "both"]:
        Null()
    elif Laura.Clothes["dress"].string == "black_dress" and Laura.Clothes["dress"].state == 0:
        "characters/Laura/images/standing/nipple_piercings_ring_covered_[Laura.Clothes[dress].string].webp"
    elif Laura.Clothes["bra"].string in ["black_lace_bra", "white_tanktop"] and Laura.Clothes["bra"].state == 0:
        "characters/Laura/images/standing/nipple_piercings_ring_covered_[Laura.Clothes[bra].string].webp"
    elif Laura.Clothes["bodysuit"].string and Laura.Clothes["bodysuit"].state == 0:
        "characters/Laura/images/standing/nipple_piercings_ring_covered_[Laura.Clothes[bodysuit].string].webp"

    if Laura.Clothes["neck"].string:
        "characters/Laura/images/standing/neck_[Laura.Clothes[neck].string].webp"

    if Laura.Clothes["jacket"].string:
        "characters/Laura/images/standing/jacket_[Laura.Clothes[jacket].string].webp"

    if Laura.arm_pose == 1:
        "characters/Laura/images/standing/left_arm1.webp"

    if Laura.arm_pose == 1 and Laura.Clothes["gloves"].string:
        "characters/Laura/images/standing/gloves_[Laura.Clothes[gloves].string]_left1.webp"

    if Laura.arm_pose == 1 and Laura.Clothes["bodysuit"].string in ["blackyellow_Wolverine_suit", "blueyellow_Wolverine_suit"]:
        "characters/Laura/images/standing/bodysuit_[Laura.Clothes[bodysuit].string]_left_sleeve1.webp"

    if Laura.arm_pose == 1 and Laura.Clothes["jacket"].string:
        "characters/Laura/images/standing/jacket_[Laura.Clothes[jacket].string]_left_sleeve1.webp"

    if Laura.arm_pose == 1 and Laura.claws:
        "characters/Laura/images/standing/left_claws1.webp"

    always:
        "characters/Laura/images/standing/head.webp"

    if Laura.Clothes["face_outer_accessory"].string:
        "characters/Laura/images/standing/hair_mask.webp"

    if Laura.eyes in ["closed", "down", "side", "squint", "up"]:
        "characters/Laura/images/standing/eyes_[Laura.eyes].webp"
    else:
        "Laura_standing_blinking"

    always:
        "characters/Laura/images/standing/brows_[Laura.brows].webp"

    always:
        "characters/Laura/images/standing/mouth_[Laura.mouth].webp"

    if Laura.blush:
        "characters/Laura/images/standing/blush[Laura.blush].webp"

    if Laura.Clothes["face_outer_accessory"].string:
        Null()
    elif Laura.wet:
        "characters/Laura/images/standing/hair_shadow_wet.webp"
    else:
        "characters/Laura/images/standing/hair_shadow_[Laura.Clothes[hair].string].webp"

    if Laura.Clothes["face_outer_accessory"].string:
        Null()
    elif Laura.wet:
        "characters/Laura/images/standing/hair_wet.webp"
    else:
        "characters/Laura/images/standing/hair_[Laura.Clothes[hair].string].webp"

    if not Laura.Clothes["face_outer_accessory"].string:
        Null()
    elif Laura.mouth in ["agape", "open", "tongue"]:
        "characters/Laura/images/standing/face_outer_accessory_[Laura.Clothes[face_outer_accessory].string]_open.webp"
    else:
        "characters/Laura/images/standing/face_outer_accessory_[Laura.Clothes[face_outer_accessory].string].webp"

    if Laura.arm_pose == 2:
        "characters/Laura/images/standing/left_arm2.webp"

    if Laura.arm_pose == 2 and Laura.Clothes["gloves"].string:
        "characters/Laura/images/standing/gloves_[Laura.Clothes[gloves].string]_left2.webp"

    if Laura.arm_pose == 2 and Laura.Clothes["bodysuit"].string in ["blackyellow_Wolverine_suit", "blueyellow_Wolverine_suit"]:
        "characters/Laura/images/standing/bodysuit_[Laura.Clothes[bodysuit].string]_left_sleeve2.webp"

    if Laura.arm_pose == 2 and Laura.Clothes["jacket"].string:
        "characters/Laura/images/standing/jacket_[Laura.Clothes[jacket].string]_left_sleeve2.webp"

    if Laura.arm_pose == 2 and Laura.claws:
        "characters/Laura/images/standing/left_claws2.webp"

    anchor (0.5, 0.0) offset (0, 20) zoom 0.62

image Laura_standing_blinking:
    f"characters/Laura/images/standing/eyes_{Laura.eyes}.webp"
    choice:
        4.5
    choice:
        4.0
    choice:
        3.5
    "characters/Laura/images/standing/eyes_blink1.webp"
    0.027
    "characters/Laura/images/standing/eyes_blink2.webp"
    0.027
    "characters/Laura/images/standing/eyes_closed.webp"
    0.054
    "characters/Laura/images/standing/eyes_blink2.webp"
    0.018
    "characters/Laura/images/standing/eyes_blink1.webp"
    0.072
    repeat
