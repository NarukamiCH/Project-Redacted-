layeredimage Xavier_sprite:
    always:
        "characters/Xavier/images/body.webp"

    if Xavier.eyes in ["closed", "squint", "up"]:
        "characters/Xavier/images/eyes_[Xavier.eyes].webp"
    else:
        "Xavier_blinking"

    always:
        "characters/Xavier/images/brows_[Xavier.brows].webp"

    always:
        "characters/Xavier/images/mouth_[Xavier.mouth].webp"
        
    if Xavier.psychic:
        "characters/Xavier/images/psychic.webp"

    anchor (0.5, 0.0) offset (0, 500) zoom 0.55

image Xavier_blinking:
    f"characters/Xavier/images/eyes_{Xavier.eyes}.webp"
    choice:
        4.5
    choice:
        4.0
    choice:
        3.5
    "characters/Xavier/images/eyes_blink1.webp"
    0.023
    "characters/Xavier/images/eyes_blink2.webp"
    0.023
    "characters/Xavier/images/eyes_closed.webp"
    0.054
    "characters/Xavier/images/eyes_blink2.webp"
    0.018
    "characters/Xavier/images/eyes_blink1.webp"
    0.072
    repeat