init python:

    config.name = _("Project [Redacted]")
    config.version = "0.2a"

    build.name = "Project-Redacted-"

    config.screen_width = 3840
    config.screen_height = 2160
    config.default_fullscreen = False

    config.max_fit_size = 12000

    config.developer = True

    config.gl2 = True
    config.cache_surfaces = False
    config.optimize_texture_bounds = True
    config.image_cache_size = 120

    config.allow_underfull_grids = True

    config.narrator_menu = True

    config.has_sound = False
    config.has_music = False
    config.has_voice = False

    preferences.text_cps = 0
    preferences.afm_time = 10

    # config.window_icon = "images/GUI/icon.webp"

    config.save_directory = "Project [Redacted]"

    build.classify("**.md", None)

    build.classify("**.webp", "archive")
    build.classify("**.rpy", "archive")
    build.classify("**.rpyc", "archive")
    build.classify("**.ttf", "archive")

    build.documentation("*.html")
    build.documentation("*.txt")

    config.keymap["rollback"].remove("mousedown_4")
    config.keymap["rollforward"].remove("mousedown_5")

    config.thumbnail_width = 250
    config.thumbnail_height = 141

    config.layers = ["background", "master", "black", "transient", "screens", "overlay"]