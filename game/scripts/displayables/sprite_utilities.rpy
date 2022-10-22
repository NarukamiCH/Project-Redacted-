init python:

    def get_transition(location):
        if location in ["bg_jean", "bg_laura", "bg_player", "bg_pool", "bg_shower"]:
            entrance_transition = easeinleft
            exit_transition = easeoutleft
        else:
            if renpy.random.randint(0, 1):
                entrance_transition = easeinleft
                exit_transition = easeoutleft
            else:
                entrance_transition = easeinright
                exit_transition = easeoutright

        return entrance_transition, exit_transition

    def get_color_transform(location):
        if location in ["bg_campus", "bg_classroom", "bg_mall", "bg_pool"] and time_index == 0:
            color_transform = morning
        elif location in ["bg_campus", "bg_classroom", "bg_mall", "bg_pool"] and time_index == 1:
            color_transform = daylight
        elif location in ["bg_campus", "bg_classroom", "bg_mall", "bg_pool"] and time_index == 2:
            color_transform = sunset
        elif location in ["bg_campus", "bg_classroom", "bg_mall", "bg_pool"] and time_index > 2:
            color_transform = moonlight
        elif time_index == 4:
            color_transform = lights_off
        elif location == "bg_movies":
            color_transform = theater
        else:
            color_transform = indoors

        return color_transform

transform sprite_location(x_position = stage_right, y_position = 0):
    anchor (0.5, 0.0) pos (x_position, y_position)

transform silhouette:
    matrixcolor TintMatrix(Color(rgb = (0.3, 0.4, 0.4)))*OpacityMatrix(0.95)*BrightnessMatrix(-0.9)

transform morning:
    matrixcolor TintMatrix(Color(rgb = (1.0, 0.95, 0.9)))*BrightnessMatrix(0.02)

transform daylight:
    matrixcolor TintMatrix(Color(rgb = (1.0, 1.0, 1.0)))*BrightnessMatrix(0.02)

transform sunset:
    matrixcolor TintMatrix(Color(rgb = (1.0, 0.8, 0.65)))*BrightnessMatrix(0.01)

transform moonlight:
    matrixcolor TintMatrix(Color(rgb = (0.5, 0.6, 1.0)))*BrightnessMatrix(0.0)

transform indoors:
    matrixcolor TintMatrix(Color(rgb = (1.0, 1.0, 1.0)))*BrightnessMatrix(0.0)

transform lights_off:
    matrixcolor TintMatrix(Color(rgb = (0.45, 0.45, 0.65)))*BrightnessMatrix(-0.07)

transform candlelit:
    matrixcolor TintMatrix(Color(rgb = (1.0, 0.95, 0.95)))*BrightnessMatrix(-0.1)

transform theater:
    matrixcolor TintMatrix(Color(rgb = (0.45, 0.45, 0.65)))*BrightnessMatrix(-0.05)

transform reset_zoom:
    ease 0.75 offset (0, 0) xzoom 1.0 yzoom 1.0 zoom 1.0

transform reset_zoom_instantly:
    offset (0, 0) xzoom 1.0 yzoom 1.0 zoom 1.0

transform null:
    alpha 1.0

label show_Character(Character, x_position = None, y_position = None, sprite_layer = None, color_transform = None, animation_transform = None, transition = None):
    python:
        if Character in all_Girls:
            # renpy.start_predict(f"images/{Character.tag}_standing/*.webp")
            renpy.stop_predict(f"images/{Character.tag}_blowjob/*.webp")
            renpy.stop_predict(f"images/{Character.tag}_sex/*.webp")
            renpy.stop_predict(f"images/{Character.tag}_doggy/*.webp")

        if x_position:
            Character.sprite_location = x_position

        if not y_position:
            y_position = 0

        if sprite_layer:
            Character.sprite_layer = sprite_layer

        transform_list = [sprite_location(Character.sprite_location, y_position)]

        if color_transform:
            transform_list.append(color_transform)

        if animation_transform:
            transform_list.append(animation_transform)

        if Character in all_Girls:
            renpy.show(f"{Character.tag}_sprite standing", at_list = transform_list, zorder = Character.sprite_layer, tag = f"{Character.tag}_sprite")
        else:
            renpy.show(f"{Character.tag}_sprite", at_list = transform_list, zorder = Character.sprite_layer, tag = f"{Character.tag}_sprite")

        if transition:
            renpy.with_statement(transition)

    return

label hide_Character(Character, transition = None):
    python:
        if transition is None:
            transition = get_transition(Player.location)[1]

        if Character in all_Girls:
            # renpy.stop_predict(f"images/{Character.tag}_standing/*.webp")
            renpy.stop_predict(f"images/{Character.tag}_blowjob/*.webp")
            renpy.stop_predict(f"images/{Character.tag}_sex/*.webp")
            renpy.stop_predict(f"images/{Character.tag}_doggy/*.webp")

        renpy.hide(f"{Character.tag}_sprite")

        if transition:
            renpy.with_statement(transition)

    return

label hide_all(fade = False):
    if fade:
        show black_screen onlayer black

    $ temp_Characters = all_Characters[:]

    while temp_Characters:
        if renpy.showing(f"{temp_Characters[0].tag}_sprite") and temp_Characters[0] not in Player.Party:
            call hide_Character(temp_Characters[0], transition = False)

        $ temp_Characters.remove(temp_Characters[0])

    if fade:
        hide black_screen onlayer black

    return

label add_Characters(Characters, fade = False):
    python:
        if Characters in all_Characters:
            Characters = [Characters]

        for C in Characters:
            C.location = Player.location

            if C in all_Girls and C not in Present:
                Present.append(C)

    call set_the_scene(fade = fade)

    return

label remove_Character(Character, transition = None):
    python:
        if Character in Player.Party:
            Player.Party.remove(Character)

        if Character in Present:
            Present.remove(Character)

        if Character in Nearby:
            Nearby.remove(Character)

        if Character in all_Girls:
            if Character.destination != Character.location:
                Character.location = Character.destination
            elif Player.location in ["bg_campus", "bg_pool"]:
                Nearby.append(Character)

                Character.location = "nearby"
            elif Player.location == Character.home:
                Character.location = "bg_campus"
            else:
                Character.location = Character.home

    call hide_Character(Character, transition = transition)

    if Character in all_Girls:
        $ Character.change_Outfit()

    return

label remove_all(location = None):
    call get_Present(location)

    if Present:
        $ temp_Characters = Present[:]

        while temp_Characters:
            if temp_Characters[0] not in Player.Party:
                call remove_Character(temp_Characters[0])

            $ temp_Characters.remove(temp_Characters[0])

    return

label show_blowjob(Girl, x_position = None, y_position = None, sprite_layer = None):
    python:
        # renpy.stop_predict(f"images/{Girl.tag}_standing/*.webp")
        renpy.start_predict(f"images/{Girl.tag}_blowjob/*.webp")
        renpy.stop_predict(f"images/{Girl.tag}_sex/*.webp")
        renpy.stop_predict(f"images/{Girl.tag}_doggy/*.webp")

        if x_position:
            Girl.sprite_location = x_position

        if not y_position:
            y_position = 0

        if sprite_layer:
            Girl.sprite_layer = sprite_layer

        color_transform = get_color_transform(Player.location)

        transform_list = [sprite_location(Girl.sprite_location, y_position), color_transform]

        renpy.show(f"{Girl.tag}_sprite blowjob", at_list = transform_list, zorder = Girl.sprite_layer, tag = f"{Girl.tag}_sprite")

    return

label show_sex(Girl, x_position = None, y_position = None, sprite_layer = None):
    python:
        # renpy.stop_predict(f"images/{Girl.tag}_standing/*.webp")
        renpy.stop_predict(f"images/{Girl.tag}_blowjob/*.webp")
        renpy.start_predict(f"images/{Girl.tag}_sex/*.webp")
        renpy.stop_predict(f"images/{Girl.tag}_doggy/*.webp")

        if x_position:
            Girl.sprite_location = x_position

        if not y_position:
            y_position = 0

        if sprite_layer:
            Girl.sprite_layer = sprite_layer

        color_transform = get_color_transform(Player.location)

        transform_list = [sprite_location(Girl.sprite_location, y_position), color_transform]

        renpy.show(f"{Girl.tag}_sprite sex", at_list = transform_list, zorder = Girl.sprite_layer, tag = f"{Girl.tag}_sprite")

    return

label show_doggy(Girl, x_position = None, y_position = None, sprite_layer = None):
    python:
        # renpy.stop_predict(f"images/{Girl.tag}_standing/*.webp")
        renpy.stop_predict(f"images/{Girl.tag}_blowjob/*.webp")
        renpy.stop_predict(f"images/{Girl.tag}_sex/*.webp")
        renpy.start_predict(f"images/{Girl.tag}_doggy/*.webp")

        if x_position:
            Girl.sprite_location = x_position

        if not y_position:
            y_position = 0

        if sprite_layer:
            Girl.sprite_layer = sprite_layer

        color_transform = get_color_transform(Player.location)

        transform_list = [sprite_location(Girl.sprite_location, y_position), color_transform]

        renpy.show(f"{Girl.tag}_sprite doggy", at_list = transform_list, zorder = Girl.sprite_layer, tag = f"{Girl.tag}_sprite")

    return
