layeredimage Xavier_sprite:
    always:
        "images/Xavier/body.webp"

    if Xavier.eyes in ["closed", "squint", "up"]:
        "images/Xavier/eyes_[Xavier.eyes].webp"
    else:
        "Xavier_blinking"

    always:
        "images/Xavier/brows_[Xavier.brows].webp"

    always:
        "images/Xavier/mouth_[Xavier.mouth].webp"
        
    if Xavier.psychic:
        "images/Xavier/psychic.webp"

    anchor (0.5, 0.0) offset (0, 500) zoom 0.55

image Xavier_blinking:
    f"images/Xavier/eyes_{Xavier.eyes}.webp"
    choice:
        4.5
    choice:
        4.0
    choice:
        3.5
    "images/Xavier/eyes_blink1.webp"
    0.023
    "images/Xavier/eyes_blink2.webp"
    0.023
    "images/Xavier/eyes_closed.webp"
    0.054
    "images/Xavier/eyes_blink2.webp"
    0.018
    "images/Xavier/eyes_blink1.webp"
    0.072
    repeat