layeredimage Zero_doggy_cock:
    # always:
    #     "characters/Zero/images/doggy/cock_shadow.webp"
        
    always:
        "characters/Zero/images/doggy/cock_[Player.skin_color].webp"

    if Player.grool:
        "characters/Zero/images/doggy/grool.webp"
        
image Zero_doggy_right_arm_shadow:
    "characters/Zero/images/doggy/right_arm_[Player.skin_color]_shadow.webp"

layeredimage Zero_doggy_right_arm:
    always:
        "characters/Zero/images/doggy/right_arm_shadow_body.webp"

    always:
        "characters/Zero/images/doggy/right_arm_[Player.skin_color].webp"
        
image Zero_doggy_left_arm:
    "characters/Zero/images/doggy/left_arm_[Player.skin_color].webp"

image Zero_doggy_cock_animation0:
    "Zero_doggy_cock"

    subpixel True
    pos (0.002, 0.3)

image Zero_doggy_cock_animation1:
    "Zero_doggy_cock"

    subpixel True
    pos (0.005, 0.2)
    block:
        ease 0.8 ypos 0.15
        pause 0.8
        ease 0.8 ypos 0.2
        repeat

image Zero_doggy_cock_animation2:
    "Zero_doggy_cock"

    subpixel True
    pos (0.002, 0.15)
    block:
        ease 0.6 ypos -0.05
        pause 0.1
        ease 0.6 ypos 0.15
        repeat

image Zero_doggy_cock_animation3:
    "Zero_doggy_cock"

    subpixel True
    pos (0.002, 0.05)
    block:
        ease 0.4 ypos -0.11
        pause 0.05
        ease 0.4 ypos 0.05
        repeat

image Zero_doggy_cock_anal_animation0:
    "Zero_doggy_cock"

    subpixel True
    pos (0.006, 0.2)

image Zero_doggy_cock_anal_animation1:
    "Zero_doggy_cock"

    subpixel True
    pos (0.005, 0.11)
    block:
        ease 0.8 ypos 0.02
        pause 0.8
        ease 0.8 ypos 0.11
        repeat

image Zero_doggy_cock_anal_animation2:
    "Zero_doggy_cock"

    subpixel True
    pos (0.002, 0.05)
    block:
        ease 0.6 ypos -0.1
        pause 0.1
        ease 0.6 ypos 0.05
        repeat

image Zero_doggy_cock_anal_animation3:
    "Zero_doggy_cock"

    subpixel True
    pos (0.002, -0.05)
    block:
        ease 0.4 ypos -0.2
        pause 0.05
        ease 0.4 ypos -0.05
        repeat
    
image Zero_doggy_right_arm_shadow_animation0:
    "Zero_doggy_right_arm_shadow"

image Zero_doggy_right_arm_shadow_animation1:
    "Zero_doggy_right_arm_shadow"

image Zero_doggy_right_arm_shadow_animation2:
    "Zero_doggy_right_arm_shadow"

image Zero_doggy_right_arm_shadow_animation3:
    "Zero_doggy_right_arm_shadow"
    
image Zero_doggy_right_arm_animation0:
    "Zero_doggy_right_arm"

image Zero_doggy_right_arm_animation1:
    "Zero_doggy_right_arm"

image Zero_doggy_right_arm_animation2:
    "Zero_doggy_right_arm"

image Zero_doggy_right_arm_animation3:
    "Zero_doggy_right_arm"

image Zero_doggy_left_arm_animation0:
    "Zero_doggy_left_arm"

image Zero_doggy_left_arm_animation1:
    "Zero_doggy_left_arm"

image Zero_doggy_left_arm_animation2:
    "Zero_doggy_left_arm"

image Zero_doggy_left_arm_animation3:
    "Zero_doggy_left_arm"

layeredimage Zero_doggy_cock_animations:
    if Player.cock_Action.type == "sex":
        "Zero_doggy_cock_animation[Player.cock_Action.speed]"
    elif Player.cock_Action.type == "anal":
        "Zero_doggy_cock_anal_animation[Player.cock_Action.speed]"
    else:
        "Zero_doggy_cock_animation0"