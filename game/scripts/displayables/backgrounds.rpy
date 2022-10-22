image black_screen:
    Solid("#000000")

    on show:
        alpha 0.0
        linear 0.4 alpha 1.0
    on hide:
        alpha 1.0
        linear 0.4 alpha 0.0

image steam_midground:
    "images/effects/steam2.webp"

    subpixel True
    xpos -config.screen_width
    block:
        linear 45.0 xpos config.screen_width
        xpos -config.screen_width
        repeat

image steam_cover:
    "images/effects/steam1.webp"

    subpixel True
    xpos config.screen_width
    block:
        linear 30.0 xpos -config.screen_width
        xpos config.screen_width
        repeat

layeredimage background:
    if Player.location in bedrooms:
        "images/backgrounds/bg_sky_[current_time].webp"

    if Player.location in ["hold", "bg_shop", "bg_hallway"]:
        "black_screen"
    elif Player.location in ["bg_campus", "bg_classroom", "bg_mall", "bg_pool"]:
        "images/backgrounds/[Player.location]_[current_time].webp"
    else:
        "images/backgrounds/[Player.location].webp"

layeredimage midground:
    if Player.location == "bg_classroom":
        "images/backgrounds/bg_classroom_[current_time]_podium.webp"
    elif Player.location == "bg_mall" and current_time != "night":
        "images/backgrounds/bg_mall_[current_time]_people.webp"
    elif Player.location == "bg_pool":
        AlphaMask("images/backgrounds/bg_pool_[current_time].webp", "images/backgrounds/bg_pool_mask.webp")
    elif Player.location == "bg_shower":
        "steam_midground"

layeredimage foreground:
    if Player.location == "bg_classroom" and time_index < 2 and weekday < 5 and clock >= 30:
        "images/backgrounds/bg_classroom_students.webp"

layeredimage cover:
    if Player.location == "bg_shower":
        "steam_cover" alpha 0.8
