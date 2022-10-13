layeredimage Laura_sprite standing:
    if Laura.Clothes["face_inner_accessory"].string:
        "images/Laura_standing/Laura_standing_hair_back_mask.png"
    else:
        "images/Laura_standing/Laura_standing_hair_back.png"

    always:
        "images/Laura_standing/Laura_standing_right_arm.png"

    # if Laura.claws:
    #     "images/Laura_standing/Laura_standing_right_claws.png"

    if Laura.Clothes["bodysuit"].string in ["blackyellow_Wolverine_suit", "blueyellow_Wolverine_suit"]:
        "images/Laura_standing/Laura_standing_bodysuit_[Laura.Clothes[bodysuit].string]_right_sleeve.png"

    if Laura.Clothes["jacket"].string:
        "images/Laura_standing/Laura_standing_jacket_[Laura.Clothes[jacket].string]_right_sleeve.png"

    always:
        "images/Laura_standing/Laura_standing_body.png"

    if Laura.pubes:
        "images/Laura_standing/Laura_standing_pubes_[Laura.pubes].png"

    always:
        "images/Laura_standing/Laura_standing_breasts.png"

    if Laura.Clothes["underwear"].string:
        "images/Laura_standing/Laura_standing_underwear_[Laura.Clothes[underwear].string]_[Laura.Clothes[underwear].state].png"

    if Laura.Clothes["bodysuit"].string:
        "images/Laura_standing/Laura_standing_bodysuit_[Laura.Clothes[bodysuit].string]_[Laura.Clothes[bodysuit].state].png"

    if Laura.Clothes["pants"].string:
        "images/Laura_standing/Laura_standing_pants_[Laura.Clothes[pants].string]_[Laura.Clothes[pants].state].png"

    if Laura.Clothes["belt"].string:
        "images/Laura_standing/Laura_standing_belt_[Laura.Clothes[belt].string].png"

    if Laura.Clothes["bra"].string:
        "images/Laura_standing/Laura_standing_bra_[Laura.Clothes[bra].string]_[Laura.Clothes[bra].state].png"

    if Laura.Clothes["top"].string:
        "images/Laura_standing/Laura_standing_top_[Laura.Clothes[top].string]_[Laura.Clothes[top].state].png"

    if not Laura.Clothes["jacket"].string:
        Null()
    elif Laura.Clothes["top"].string:
        "images/Laura_standing/Laura_standing_jacket_[Laura.Clothes[jacket].string]_[Laura.Clothes[top].string].png"
    else:
        "images/Laura_standing/Laura_standing_jacket_[Laura.Clothes[jacket].string].png"

    always:
        "images/Laura_standing/Laura_standing_head.png"

    if Laura.eyes in ["closed", "down", "side", "squint"]:
        "images/Laura_standing/Laura_standing_eyes_[Laura.eyes].png"
    else:
        "Laura_standing_blinking"

    always:
        "images/Laura_standing/Laura_standing_brows_[Laura.brows].png"

    always:
        "images/Laura_standing/Laura_standing_mouth_[Laura.mouth].png"

    if Laura.blush:
        "images/Laura_standing/Laura_standing_blush_[Laura.blush].png"

    if not Laura.Clothes["face_inner_accessory"].string:
        Null()
    elif Laura.mouth in ["sucking", "surprised", "tongue"]:
        "images/Laura_standing/Laura_standing_face_inner_accessory_[Laura.Clothes[face_inner_accessory].string]_open.png"
    else:
        "images/Laura_standing/Laura_standing_face_inner_accessory_[Laura.Clothes[face_inner_accessory].string].png"

    if Laura.Clothes["face_inner_accessory"].string:
        Null()
    elif Laura.wet:
        "images/Laura_standing/Laura_standing_hair_messy_hair.png"
    else:
        "images/Laura_standing/Laura_standing_hair_[Laura.Clothes[hair].string].png"

    always:
        "images/Laura_standing/Laura_standing_left_arm[Laura.arm_pose].png"

    if Laura.Clothes["bodysuit"].string in ["blackyellow_Wolverine_suit", "blueyellow_Wolverine_suit"]:
        "images/Laura_standing/Laura_standing_bodysuit[Laura.arm_pose]_[Laura.Clothes[bodysuit].string]_left_sleeve.png"

    if Laura.Clothes["jacket"].string:
        "images/Laura_standing/Laura_standing_jacket[Laura.arm_pose]_[Laura.Clothes[jacket].string]_left_sleeve.png"

    if Laura.claws:
        "images/Laura_standing/Laura_standing_left_claws[Laura.arm_pose].png"

    anchor (0.5, 0.0) offset (0, -10) zoom 0.6

image Laura_standing_blinking:
    "images/Laura_standing/Laura_standing_eyes_[Laura.eyes].png"
    choice:
        3.5
    choice:
        3.25
    choice:
        3
    "images/Laura_standing/Laura_standing_eyes_closed.png"
    0.05
    "images/Laura_standing/Laura_standing_eyes_closed.png"
    0.15
    "images/Laura_standing/Laura_standing_eyes_closed.png"
    0.05
    repeat
