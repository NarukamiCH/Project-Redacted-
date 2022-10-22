layeredimage Xavier_sprite old:
    always:
        "images/Xavier/Xavier_body.webp"

    if Xavier.eyes in ["closed", "squint", "up"]:
        "images/Xavier/Xavier_eyes_[Xavier.eyes].webp"
    else:
        "Xavier_blinking"

    always:
        "images/Xavier/Xavier_brows_[Xavier.brows].webp"

    always:
        "images/Xavier/Xavier_mouth_[Xavier.mouth].webp"
        
    if Xavier.psychic:
        "images/Xavier/Xavier_psychic.webp"

    anchor (0.5, 0.0) offset (0, 500) zoom 0.55

image Xavier_blinking:
    "images/Xavier/Xavier_eyes_[Xavier.eyes].webp"
    choice:
        3.5
    choice:
        3.25
    choice:
        3
    "images/Xavier/Xavier_eyes_half_blink.webp"
    0.05
    "images/Xavier/Xavier_eyes_closed.webp"
    0.07
    "images/Xavier/Xavier_eyes_half_blink.webp"
    0.15
    repeat