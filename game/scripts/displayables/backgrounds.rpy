image black_screen:
    Solid("#000000")

    on show:
        alpha 0.0
        linear 0.4 alpha 1.0
    on hide:
        alpha 1.0
        linear 0.4 alpha 0.0

image steam_midground:
    "images/backgrounds/steam2.png"

    subpixel True
    xpos -config.screen_width
    block:
        linear 45.0 xpos config.screen_width
        xpos -config.screen_width
        repeat

image steam_cover:
    "images/backgrounds/steam1.png"

    subpixel True
    xpos config.screen_width
    block:
        linear 30.0 xpos -config.screen_width
        xpos config.screen_width
        repeat

layeredimage background:
    always:
        "images/backgrounds/sky_[current_time].png"

    if Player.location in ["hold", "bg_mall", "bg_shop", "bg_hallway"]:
        "black_screen"
    elif Player.location in ["bg_campus", "bg_classroom", "bg_pool"]:
        "images/backgrounds/[Player.location]_[current_time].png"
    else:
        "images/backgrounds/[Player.location].png"

layeredimage midground:
    if Player.location == "bg_classroom":
        "images/backgrounds/[Player.location]_[current_time]_podium.png"

    if Player.location == "bg_shower":
        "steam_midground"

    if Player.location == "bg_pool":
        AlphaMask("images/backgrounds/bg_pool_[current_time].png", "images/backgrounds/bg_pool_mask.png")

layeredimage foreground:
    if Player.location == "bg_classroom" and time_index < 2 and weekday < 5 and clock >= 30:
        "images/backgrounds/[Player.location]_[current_time]_students.png"

layeredimage cover:
    if Player.location == "bg_shower":
        "steam_cover" alpha 0.8
