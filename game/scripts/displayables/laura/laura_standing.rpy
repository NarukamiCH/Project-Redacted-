layeredimage Laura_sprite standing:
    if Laura.Clothes["face_inner_accessory"].string:
        "images/Laura_standing/hair_back_mask.webp"
    else:
        "images/Laura_standing/hair_back.webp"

    if Laura.claws:
        "images/Laura_standing/right_claws.webp"

    always:
        "images/Laura_standing/right_arm.webp"

    if Laura.Clothes["gloves"].string:
        "images/Laura_standing/gloves_[Laura.Clothes[gloves].string]_right.webp"

    if Laura.Clothes["bodysuit"].string in ["blackyellow_Wolverine_suit", "blueyellow_Wolverine_suit"]:
        "images/Laura_standing/bodysuit_[Laura.Clothes[bodysuit].string]_right_sleeve.webp"

    if Laura.Clothes["jacket"].string:
        "images/Laura_standing/jacket_[Laura.Clothes[jacket].string]_right_sleeve.webp"

    always:
        "images/Laura_standing/body.webp"

    if Laura.tan_lines["bottom"]:
        "images/Laura_standing/tan_lines_bottom.webp"

    if Laura.piercings["labia"] in ["barbell", "both"]:
        "images/Laura_standing/labia_piercings_barbell.webp"

    if Laura.piercings["labia"] in ["ring", "both"]:
        "images/Laura_standing/labia_piercings_ring.webp"

    if Laura.pubes:
        "images/Laura_standing/pubes_[Laura.pubes].webp"

    always:
        "images/Laura_standing/breasts.webp"

    if Laura.tan_lines["top"]:
        "images/Laura_standing/tan_lines_top.webp"

    if Laura.piercings["nipple"] in ["barbell", "both"]:
        "images/Laura_standing/nipple_piercings_barbell.webp"

    if Laura.piercings["nipple"] in ["ring", "both"]:
        "images/Laura_standing/nipple_piercings_ring.webp"

    if Laura.Clothes["underwear"].string:
        "images/Laura_standing/underwear_[Laura.Clothes[underwear].string]_[Laura.Clothes[underwear].state].webp"

    if Laura.piercings["labia"] not in ["barbell", "both"]:
        Null()
    elif Laura.Clothes["underwear"].string == "grey_panties" and Laura.Clothes["underwear"].state == 0:
        "images/Laura_standing/labia_piercings_barbell_covered_grey_panties.webp"

    if Laura.piercings["labia"] not in ["ring", "both"]:
        Null()
    elif Laura.Clothes["underwear"].string == "grey_panties" and Laura.Clothes["underwear"].state == 0:
        "images/Laura_standing/labia_piercings_ring_covered_grey_panties.webp"

    if Laura.Clothes["socks"].string:
        "images/Laura_standing/bodysuit_[Laura.Clothes[socks].string].webp"

    if Laura.Clothes["hose"].string:
        "images/Laura_standing/bodysuit_[Laura.Clothes[hose].string].webp"

    if Laura.Clothes["bodysuit"].string:
        "images/Laura_standing/bodysuit_[Laura.Clothes[bodysuit].string]_[Laura.Clothes[bodysuit].state].webp"

    if Laura.Clothes["pants"].string:
        "images/Laura_standing/pants_[Laura.Clothes[pants].string]_[Laura.Clothes[pants].state].webp"

    if Laura.Clothes["boots"].string:
        "images/Laura_standing/boots_[Laura.Clothes[boots].string].webp"

    if Laura.Clothes["skirt"].string:
        "images/Laura_standing/skirt_[Laura.Clothes[skirt].string]_[Laura.Clothes[skirt].state].webp"

    if not Laura.Clothes["belt"].string:
        Null()
    elif Laura.Clothes["bodysuit"].string in ["blackyellow_Wolverine_suit", "blueyellow_Wolverine_suit"]:
        "images/Laura_standing/belt_[Laura.Clothes[belt].string]_high.webp"
    else:
        "images/Laura_standing/belt_[Laura.Clothes[belt].string]_low.webp"

    if Laura.Clothes["bra"].string:
        "images/Laura_standing/bra_[Laura.Clothes[bra].string]_[Laura.Clothes[bra].state].webp"

    if Laura.Clothes["dress"].string:
        "images/Laura_standing/dress_[Laura.Clothes[dress].string]_[Laura.Clothes[dress].state].webp"

    if Laura.piercings["nipple"] not in ["barbell", "both"]:
        Null()
    elif Laura.Clothes["dress"].string and Laura.Clothes["dress"].state == 0:
        "images/Laura_standing/nipple_piercings_barbell_covered_[Laura.Clothes[dress].string].webp"
    elif Laura.Clothes["bra"].string in ["black_lace_bra", "white_tanktop"] and Laura.Clothes["bra"].state == 0:
        "images/Laura_standing/nipple_piercings_barbell_covered_[Laura.Clothes[bra].string].webp"
    elif Laura.Clothes["bodysuit"].string and Laura.Clothes["bodysuit"].state == 0:
        "images/Laura_standing/nipple_piercings_barbell_covered_[Laura.Clothes[bodysuit].string].webp"

    if Laura.piercings["nipple"] not in ["ring", "both"]:
        Null()
    elif Laura.Clothes["dress"].string and Laura.Clothes["dress"].state == 0:
        "images/Laura_standing/nipple_piercings_ring_covered_[Laura.Clothes[dress].string].webp"
    elif Laura.Clothes["bra"].string in ["black_lace_bra", "white_tanktop"] and Laura.Clothes["bra"].state == 0:
        "images/Laura_standing/nipple_piercings_ring_covered_[Laura.Clothes[bra].string].webp"
    elif Laura.Clothes["bodysuit"].string and Laura.Clothes["bodysuit"].state == 0:
        "images/Laura_standing/nipple_piercings_ring_covered_[Laura.Clothes[bodysuit].string].webp"

    if Laura.Clothes["top"].string:
        "images/Laura_standing/top_[Laura.Clothes[top].string]_[Laura.Clothes[top].state].webp"

    if Laura.Clothes["jacket"].string:
        "images/Laura_standing/jacket_[Laura.Clothes[jacket].string].webp"

    if Laura.Clothes["neck"].string:
        "images/Laura_standing/neck_[Laura.Clothes[neck].string].webp"

    always:
        "images/Laura_standing/head.webp"

    if Laura.Clothes["face_inner_accessory"].string:
        "images/Laura_standing/hair_mask.webp"

    if Laura.eyes in ["closed", "down", "side", "squint", "up"]:
        "images/Laura_standing/eyes_[Laura.eyes].webp"
    else:
        "Laura_standing_blinking"

    always:
        "images/Laura_standing/brows_[Laura.brows].webp"

    always:
        "images/Laura_standing/mouth_[Laura.mouth].webp"

    if Laura.blush:
        "images/Laura_standing/blush[Laura.blush].webp"

    if Laura.Clothes["face_inner_accessory"].string:
        Null()
    elif Laura.wet:
        "images/Laura_standing/hair_shadow_wet.webp"
    else:
        "images/Laura_standing/hair_shadow_[Laura.Clothes[hair].string].webp"

    if Laura.Clothes["face_inner_accessory"].string:
        Null()
    elif Laura.wet:
        "images/Laura_standing/hair_wet.webp"
    else:
        "images/Laura_standing/hair_[Laura.Clothes[hair].string].webp"

    if not Laura.Clothes["face_inner_accessory"].string:
        Null()
    elif Laura.mouth in ["agape", "open", "tongue"]:
        "images/Laura_standing/face_inner_accessory_[Laura.Clothes[face_inner_accessory].string]_open.webp"
    else:
        "images/Laura_standing/face_inner_accessory_[Laura.Clothes[face_inner_accessory].string].webp"

    always:
        "images/Laura_standing/left_arm[Laura.arm_pose].webp"

    if Laura.Clothes["gloves"].string:
        "images/Laura_standing/gloves_[Laura.Clothes[gloves].string]_left[Laura.arm_pose].webp"

    if Laura.Clothes["bodysuit"].string in ["blackyellow_Wolverine_suit", "blueyellow_Wolverine_suit"]:
        "images/Laura_standing/bodysuit_[Laura.Clothes[bodysuit].string]_left_sleeve[Laura.arm_pose].webp"

    if Laura.Clothes["jacket"].string:
        "images/Laura_standing/jacket_[Laura.Clothes[jacket].string]_left_sleeve[Laura.arm_pose].webp"

    if Laura.claws:
        "images/Laura_standing/left_claws[Laura.arm_pose].webp"

    anchor (0.5, 0.0) offset (0, -10) zoom 0.6

image Laura_standing_blinking:
    f"images/Laura_standing/eyes_{Laura.eyes}.webp"
    choice:
        4.5
    choice:
        4.0
    choice:
        3.5
    "images/Laura_standing/eyes_blink1.webp"
    0.023
    "images/Laura_standing/eyes_blink2.webp"
    0.023
    "images/Laura_standing/eyes_closed.webp"
    0.054
    "images/Laura_standing/eyes_blink2.webp"
    0.018
    "images/Laura_standing/eyes_blink1.webp"
    0.072
    repeat
