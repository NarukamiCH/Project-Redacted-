layeredimage Zero_doggy_cock:
    always:
        "characters/Zero/images/doggy/cock_shadow.webp"
        
    always:
        "characters/Zero/images/doggy/cock_[Player.skin_color].webp"

    if Player.grool:
        "characters/Zero/images/doggy/grool.webp"

layeredimage Zero_doggy_right_arm:
    always:
        "characters/Zero/images/doggy/right_arm_[Player.skin_color]_shadow.webp"

    always:
        "characters/Zero/images/doggy/right_arm_[Player.skin_color].webp"
        
image Zero_doggy_left_arm:
    "characters/Zero/images/doggy/left_arm_[Player.skin_color].webp"

image Zero_doggy_cock_animation0:
    "Zero_doggy_cock"

image Zero_doggy_cock_animation1:
    "Zero_doggy_cock"

image Zero_doggy_cock_animation2:
    "Zero_doggy_cock"

image Zero_doggy_cock_animation3:
    "Zero_doggy_cock"

image Zero_doggy_cock_anal_animation0:
    "Zero_doggy_cock"

image Zero_doggy_cock_anal_animation1:
    "Zero_doggy_cock"

image Zero_doggy_cock_anal_animation2:
    "Zero_doggy_cock"

image Zero_doggy_cock_anal_animation3:
    "Zero_doggy_cock"
    
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
        "Zero_doggy_cock_animation[Player.cock_Action.speed]" offset (0, 0) zoom 1.0
    elif Player.cock_Action.type == "anal":
        "Zero_doggy_cock_anal_animation[Player.cock_Action.speed]" offset (0, 0) zoom 1.0
    else:
        "Zero_doggy_cock_animation0" offset (0, 0) zoom 1.0