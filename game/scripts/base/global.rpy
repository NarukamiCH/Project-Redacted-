init -1:

    define ch_player = Character("[Player.name]", who_color = "#0a84b4")
    define ch_player_nvl = Character("[Player.name]", kind = nvl)

    define ch_rogue = Character("[Rogue.name]", who_color = "#2ca05aff", image = "Rogue_sprite")
    define ch_rogue_nvl = Character("[Rogue.name]", kind = nvl)

    define ch_kitty = Character("[Kitty.name]", who_color = "#9012d9", image = "Kitty_sprite")
    define ch_kitty_nvl = Character("[Kitty.name]", kind = nvl)

    define ch_laura = Character("[Laura.name]", who_color = "#d9bb12", image = "Laura_sprite")
    define ch_laura_nvl = Character("[Laura.name]", kind = nvl)

    define ch_storm = Character("[Storm.name]", who_color = "#85f2f9", image = "Storm_sprite")
    define ch_storm_nvl = Character("[Storm.name]", kind = nvl)

    define ch_jean = Character("[Jean.name]", who_color = "#d92912", image = "Jean_sprite")
    define ch_jean_nvl = Character("[Jean.name]", kind = nvl)
    define ch_jean_tele = Character("[Jean.name]", who_color = "#d92912", what_italic = True)

    define ch_xavier = Character("[Xavier.name]", who_color = "#1b867d", image = "Xavier_sprite")
    define ch_xavier_tele = Character("[Xavier.name]", who_color = "#1b867d", what_italic = True)

    define ch_reporter = Character("Reporter", who_color = "#000000")
    define ch_farouk = Character("[Farouk.name]", who_color = "#592c99")
    define ch_farouk_tele = Character("[Farouk.name]", who_color = "#592c99", what_italic = True)

    default chapter = 0

    default stack_depth = 0

    default day = 1
    default clock = 100
    default time_options = ["morning", "midday", "evening", "night", "late night"]
    default time_index = 2
    default current_time = time_options[time_index]
    default week = ["Mon", "Tue", "Wed", "Thu", "Fri", "Sat", "Sun"]
    default weekday = 6
    default day_of_week = week[weekday]

    default Present = []
    default Nearby = []
    default Students = []
    default Staff = []
    default Professors = []
    default active_Girls = []
    default all_Girls = []
    default all_Characters = []

    default bedrooms = ["bg_player"]

    define stage_far_far_left = 0.15
    define stage_far_left = 0.25
    define stage_left = 0.35
    define stage_center = 0.5
    define stage_right = 0.65
    define stage_far_right = 0.75
    define stage_far_far_right = 0.85

    define location_names = {
        "bg_campus": "Campus",
        "bg_classroom": "Classroom",
        "bg_dangerroom": "Danger Room",
        "bg_entrance": "Main Entrance",
        "bg_hallway": "Hallway",
        "bg_jean": "[Jean.name]'s Bedroom",
        "bg_kitty": "[Kitty.name]'s Bedroom",
        "bg_laura": "[Laura.name]'s Bedroom",
        "bg_mall": "Bayville Mall",
        "bg_movies": "Movie Theater",
        "bg_player": "[Player.name]'s Bedroom",
        "bg_pool": "Pool",
        "bg_rogue": "[Rogue.name]'s Bedroom",
        "bg_shop": "Urban Big-Titter's",
        "bg_shower": "Showers",
        "hold": ""}

    define all_Clothing_types = ["face_tattoos", "face_piercings", "makeup", "gag",
        "face_inner_accessory", "hair", "face_outer_accessory",
        "body_tattoos", "body_piercings", "buttplug",
        "nipple_accessories", "underwear", "hose",
        "bodysuit", "rope",
        "socks", "pants", "skirt", "boots",
        "bra", "dress", "top",
        "neck", "gloves", "sleeves", "belt", "suspenders",
        "jacket", "cloak"]

    define intrinsic_Clothing_types = ["face_tattoos", "face_piercings",
        "body_tattoos", "body_piercings"]

    define removable_Clothing_types = ["makeup", "gag",
        "face_inner_accessory", "face_outer_accessory",
        "buttplug",
        "nipple_accessories", "underwear", "hose",
        "bodysuit", "rope",
        "socks", "pants", "skirt", "boots",
        "bra", "dress", "top",
        "neck", "gloves", "sleeves", "belt", "suspenders",
        "jacket", "cloak"]

    define bra_hiding_Clothing_types = ["dress", "top", "jacket"]
    define breast_hiding_Clothing_types = ["bodysuit", "bra", "dress", "top", "jacket"]
    define underwear_hiding_Clothing_types = ["bodysuit", "pants", "skirt", "dress", "top", "belt", "jacket"]
    define pussy_hiding_Clothing_types = ["underwear", "bodysuit", "pants", "skirt", "dress", "belt"]
    define thigh_covering_Clothing_types = ["bodysuit", "hose", "pants", "skirt", "boots", "dress"]
    define feet_covering_Clothing_types = ["hose", "socks", "boots"]

    define Clothing_coverage = {"face_tattoos": [],
        "face_piercings": [],
        "makeup": [],
        "gag": [],
        "face_inner_accessory": [],
        "hair": [],
        "face_outer_accessory": [],
        "body_tattoos": [],
        "body_piercings": [],
        "buttplug": ["underwear"],
        "nipple_accessories": ["bodysuit", "bra", "dress", "top"],
        "underwear": ["hose", "bodysuit", "pants", "belt", "suspenders", "boots"],
        "hose": ["bodysuit", "pants", "socks", "boots"],
        "bodysuit": ["bra", "dress", "top", "jacket", "cloak", "socks", "pants", "skirt", "boots"],
        "rope": ["bra", "dress", "top", "jacket", "cloak", "socks", "pants", "skirt", "boots"],
        "socks": ["boots"],
        "pants": ["boots", "belt", "suspenders"],
        "skirt": ["boots", "belt", "suspenders"],
        "boots": [],
        "bra": ["dress", "top", "suspenders", "jacket", "cloak"],
        "dress": ["top", "belt", "suspenders", "jacket", "cloak", "boots"],
        "top": ["belt", "suspenders", "jacket", "cloak"],
        "neck": [],
        "gloves": [],
        "sleeves": ["jacket"],
        "belt": ["suspenders"],
        "suspenders": ["jacket", "cloak"],
        "jacket": ["cloak"],
        "cloak": []}

    define fondle_Action_types = []
    define job_Action_types = ["blowjob"]
    define sex_Action_types = ["sex", "anal"]

    define finger_Action_types = []
    define hand_Action_types = []
    define mouth_Action_types = ["kiss", "blowjob"]
    define dildo_Action_types = []
    define cock_Action_types = ["blowjob", "sex", "anal"]
    define breast_Action_types = []
    define pussy_Action_types = ["sex"]
    define ass_Action_types = ["anal"]

    define contact_Action_types = ["kiss", "blowjob", "sex", "anal"]
    define below_Action_types = ["sex", "anal"]
    define insertion_Action_types = ["sex", "anal"]
    define anal_insertion_Action_types = ["anal"]
    define kinky_Action_types = ["anal"]

    define active_Action_types = ["kiss", "sex", "anal"]
    define passive_Action_types = ["blowjob"]

    define all_Action_types = [
        "kiss",
        "blowjob",
        "sex", "anal"]

    define rumble = Move((0, 4), (0, -4), 0.05, bounce = True, repeat = True, delay = 3.5)

    define Emma_harden = ImageDissolve("images/wipes/Emma_harden.png", 0.5, 8)
    define Mystique_dissolve = ImageDissolve("images/wipes/Mystique_dissolve.png", 1.0, 8)

    default EventScheduler = EventSchedulerClass()
