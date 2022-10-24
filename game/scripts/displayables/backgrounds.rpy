image black_screen:
    Solid("#000000")

    on show:
        alpha 0.0
        linear 0.4 alpha 1.0
    on hide:
        linear 0.4 alpha 0.0

image steam_midground:
    "images/effects/steam2.webp"

    subpixel True
    xpos 0
    block:
        linear 45.0 xpos config.screen_width
        xpos 0
        repeat

image steam_cover:
    "images/effects/steam1.webp"

    subpixel True
    alpha 0.8
    xpos config.screen_width
    block:
        linear 30.0 xpos 0
        xpos config.screen_width
        repeat

image background = Composite(
    (config.screen_width, config.screen_height),

    (0, 0), ConditionSwitch(
        "Player.location in bedrooms", "images/backgrounds/bg_sky_[current_time].webp",
        "True", Null()),

    (0, 0), ConditionSwitch(
        "Player.location in ['hold', 'bg_shop', 'bg_hallway']", "black_screen",
        "Player.location in ['bg_campus', 'bg_classroom', 'bg_mall', 'bg_pool']", "images/backgrounds/[Player.location]_[current_time].webp",
        "True", "images/backgrounds/[Player.location].webp"))

image midground = ConditionSwitch(
    "Player.location == 'bg_shower'", "steam_midground",
    "True", Null())

image foreground = Composite(
    (config.screen_width, config.screen_height),

    (0, 0), ConditionSwitch(
        "Player.location == 'bg_classroom'", "images/backgrounds/bg_classroom_[current_time]_podium.webp",
        "Player.location == 'bg_mall' and time_index < 3", "images/backgrounds/bg_mall_[current_time]_people.webp",
        "Player.location == 'bg_pool'", AlphaMask("images/backgrounds/bg_pool_[current_time].webp", "images/backgrounds/bg_pool_mask.webp"),
        "True", Null()),
        
    (0, 0), ConditionSwitch(
        "Player.location == 'bg_classroom' and time_index < 2 and weekday < 5 and clock >= 30", "images/backgrounds/bg_classroom_students.webp",
        "True", Null()))

image cover = ConditionSwitch(
    "Player.location == 'bg_shower'", "steam_cover",
    "True", Null())
