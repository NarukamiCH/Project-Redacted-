image Rogue_doggy_arms:
    "characters/Rogue/images/doggy/arms.webp"
    
layeredimage Rogue_doggy_head:
    always:
        "characters/Rogue/images/doggy/head.webp"

    always:
        "Rogue_doggy_blinking"

layeredimage Rogue_doggy_torso:
    always:
        "characters/Rogue/images/doggy/torso.webp"

    if Rogue.tan_lines["top"]:
        "characters/Rogue/images/doggy/tan_lines_top.webp"

layeredimage Rogue_doggy_hair:
    always:
        "characters/Rogue/images/doggy/hair_shadow.webp"

    always:
        "characters/Rogue/images/doggy/hair.webp"

image Rogue_doggy_legs:
    "characters/Rogue/images/doggy/legs.webp"

layeredimage Rogue_doggy_ass:
    always:
        "characters/Rogue/images/doggy/ass.webp"

    if Rogue.piercings["labia"] in ["ring", "both"]:
        "characters/Rogue/images/doggy/labia_piercings_ring.webp"

    if Rogue.pussy_Action.type == "sex":
        "Rogue_doggy_pussy_animation[Rogue.pussy_Action.speed]" pos (0.0, 0.0)
    else:
        "Rogue_doggy_pussy_closed"

    if Rogue.ass_Action.type == "anal":
        "Rogue_doggy_anus_animation[Rogue.ass_Action.speed]" pos (0.0, 0.0)
    else:
        "Rogue_doggy_anus_closed"

    if Rogue.tan_lines["bottom"]:
        "characters/Rogue/images/doggy/tan_lines_bottom.webp"

    if not Rogue.creampie["pussy"]:
        Null()
    elif Rogue.pussy_Action.speed > 1:
        "characters/Rogue/images/doggy/creampie_pussy_agape.webp"
    elif Rogue.pussy_Action.speed == 1:
        "characters/Rogue/images/doggy/creampie_pussy_open.webp"
    else:
        "characters/Rogue/images/doggy/creampie_pussy_closed.webp"

    if not Rogue.creampie["anus"]:
        Null()
    elif Rogue.anus_Action.speed > 1:
        "characters/Rogue/images/doggy/creampie_anus_agape.webp"
    elif Rogue.anus_Action.speed == 1:
        "characters/Rogue/images/doggy/creampie_anus_open.webp"
    else:
        "characters/Rogue/images/doggy/creampie_anus_closed.webp"

image Rogue_doggy_pussy_closed:
    "characters/Rogue/images/doggy/pussy_closed.webp"

image Rogue_doggy_pussy_open:
    "characters/Rogue/images/doggy/pussy_open.webp"

image Rogue_doggy_pussy_agape:
    "characters/Rogue/images/doggy/pussy_agape.webp"

image Rogue_doggy_anus_closed:
    "characters/Rogue/images/doggy/anus_closed.webp"

image Rogue_doggy_anus_open:
    "characters/Rogue/images/doggy/anus_open.webp"

image Rogue_doggy_anus_agape:
    "characters/Rogue/images/doggy/anus_agape.webp"

image Rogue_doggy_mask_pussy_open:
    "characters/Rogue/images/doggy/mask_pussy_open.webp"

image Rogue_doggy_mask_pussy_agape:
    "characters/Rogue/images/doggy/mask_pussy_agape.webp"

image Rogue_doggy_mask_anus_open:
    "characters/Rogue/images/doggy/mask_anus_open.webp"

image Rogue_doggy_mask_anus_agape:
    "characters/Rogue/images/doggy/mask_anus_agape.webp"

image Rogue_doggy_arms_animation0:
    "Rogue_doggy_arms"

image Rogue_doggy_arms_animation1:
    "Rogue_doggy_arms"

image Rogue_doggy_arms_animation2:
    "Rogue_doggy_arms"

image Rogue_doggy_arms_animation3:
    "Rogue_doggy_arms"

image Rogue_doggy_head_animation0:
    "Rogue_doggy_head"

image Rogue_doggy_head_animation1:
    "Rogue_doggy_head"

image Rogue_doggy_head_animation2:
    "Rogue_doggy_head"

image Rogue_doggy_head_animation3:
    "Rogue_doggy_head"

image Rogue_doggy_torso_animation0:
    "Rogue_doggy_torso"

image Rogue_doggy_torso_animation1:
    "Rogue_doggy_torso"

image Rogue_doggy_torso_animation2:
    "Rogue_doggy_torso"

image Rogue_doggy_torso_animation3:
    "Rogue_doggy_torso"

image Rogue_doggy_hair_animation0:
    "Rogue_doggy_hair"

image Rogue_doggy_hair_animation1:
    "Rogue_doggy_hair"

image Rogue_doggy_hair_animation2:
    "Rogue_doggy_hair"

image Rogue_doggy_hair_animation3:
    "Rogue_doggy_hair"

image Rogue_doggy_legs_animation0:
    "Rogue_doggy_legs"

image Rogue_doggy_legs_animation1:
    "Rogue_doggy_legs"

image Rogue_doggy_legs_animation2:
    "Rogue_doggy_legs"

image Rogue_doggy_legs_animation3:
    "Rogue_doggy_legs"

image Rogue_doggy_ass_animation0:
    "Rogue_doggy_ass"

image Rogue_doggy_ass_animation1:
    "Rogue_doggy_ass"

image Rogue_doggy_ass_animation2:
    "Rogue_doggy_ass"

image Rogue_doggy_ass_animation3:
    "Rogue_doggy_ass"

image Rogue_doggy_pussy_animation0:
    "Rogue_doggy_pussy_closed"

image Rogue_doggy_pussy_animation1:
    "Rogue_doggy_pussy_open"

image Rogue_doggy_pussy_animation2:
    "Rogue_doggy_pussy_agape"

image Rogue_doggy_pussy_animation3:
    "Rogue_doggy_pussy_agape"

image Rogue_doggy_anus_animation0:
    "Rogue_doggy_anus_closed"

image Rogue_doggy_anus_animation1:
    "Rogue_doggy_anus_open"

image Rogue_doggy_anus_animation2:
    "Rogue_doggy_anus_agape"

image Rogue_doggy_anus_animation3:
    "Rogue_doggy_anus_agape"

image Rogue_doggy_mask_pussy_animation1:
    "Rogue_doggy_mask_pussy_open"

image Rogue_doggy_mask_pussy_animation2:
    "Rogue_doggy_mask_pussy_agape"

image Rogue_doggy_mask_pussy_animation3:
    "Rogue_doggy_mask_pussy_agape"

image Rogue_doggy_mask_anus_animation1:
    "Rogue_doggy_mask_anus_open"

image Rogue_doggy_mask_anus_animation2:
    "Rogue_doggy_mask_anus_agape"

image Rogue_doggy_mask_anus_animation3:
    "Rogue_doggy_mask_anus_agape"

image Rogue_sprite doggy:
    contains:
        ConditionSwitch(
            "Rogue in Player.cock_Action.Actors", "Rogue_doggy_arms_animation[Player.cock_Action.speed]",
            "True", "Rogue_doggy_arms_animation0")

    contains:
        ConditionSwitch(
            "Rogue in Player.cock_Action.Actors", "Rogue_doggy_head_animation[Player.cock_Action.speed]",
            "True", "Rogue_doggy_head_animation0")

    contains:
        ConditionSwitch(
            "Rogue in Player.cock_Action.Actors", "Rogue_doggy_torso_animation[Player.cock_Action.speed]",
            "True", "Rogue_doggy_torso_animation0")

    contains:
        ConditionSwitch(
            "Rogue in Player.cock_Action.Actors", "Rogue_doggy_hair_animation[Player.cock_Action.speed]",
            "True", "Rogue_doggy_hair_animation0")

    contains:
        ConditionSwitch(
            "Rogue in Player.cock_Action.Actors", "Rogue_doggy_legs_animation[Player.cock_Action.speed]",
            "True", "Rogue_doggy_legs_animation0")

    contains:
        ConditionSwitch(
            "Rogue in Player.cock_Action.Actors", "Rogue_doggy_ass_animation[Player.cock_Action.speed]",
            "True", "Rogue_doggy_ass_animation0")

    contains:
        "Zero_doggy_cock_animations"

    contains:
        ConditionSwitch(
            "Rogue in Player.cock_Action.Actors", "Zero_doggy_right_arm_animation[Player.cock_Action.speed]",
            "True", "Zero_doggy_right_arm_animation0")

    contains:
        ConditionSwitch(
            "Rogue in Player.cock_Action.Actors", "Zero_doggy_left_arm_animation[Player.cock_Action.speed]",
            "True", "Zero_doggy_left_arm_animation0")
    
    anchor (0.5, 0.5) offset (0, 0) zoom 0.55

image Rogue_doggy_blinking:
    "characters/Rogue/images/doggy/eyes_neutral.webp"
    choice:
        4.5
    choice:
        4.0
    choice:
        3.5
    "characters/Rogue/images/doggy/eyes_blink1.webp"
    0.023
    "characters/Rogue/images/doggy/eyes_blink2.webp"
    0.023
    "characters/Rogue/images/doggy/eyes_closed.webp"
    0.054
    "characters/Rogue/images/doggy/eyes_blink2.webp"
    0.018
    "characters/Rogue/images/doggy/eyes_blink1.webp"
    0.072
    repeat
