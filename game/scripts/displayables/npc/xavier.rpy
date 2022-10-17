layeredimage Xavier_sprite:
    always:
        "images/Xavier/Xavier_body.png"

    if Xavier.eyes in ["closed", "squint", "up"]:
        "images/Xavier/Xavier_eyes_[Xavier.eyes].png"
    else:
        "Xavier_blinking"

    always:
        "images/Xavier/Xavier_brows_[Xavier.brows].png"

    always:
        "images/Xavier/Xavier_mouth_[Xavier.mouth].png"
        
    if Xavier.psychic:
        "images/Xavier/Xavier_psychic.png"

    anchor (0.5, 0.0) offset (0, 500) zoom 0.55

image Xavier_blinking:
    "images/Xavier/Xavier_eyes_[Xavier.eyes].png"
    choice:
        3.5
    choice:
        3.25
    choice:
        3
    "images/Xavier/Xavier_eyes_half_blink.png"
    0.05
    "images/Xavier/Xavier_eyes_closed.png"
    0.07
    "images/Xavier/Xavier_eyes_half_blink.png"
    0.15
    repeat