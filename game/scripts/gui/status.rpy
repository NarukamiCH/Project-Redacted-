screen status():
    vbox anchor (0.0, 0.5) pos (0.005, 0.0325):
        spacing 6

        text f"{Player.name}" size 52

        hbox:
            spacing 100

            text f"Level {Player.level}" size 52
            text f"${Player.cash}" size 52

    vbox anchor (1.0, 0.5) pos (0.995, 0.0325):
        spacing 6

        text f"Day {day}, {current_time.capitalize()} ({day_of_week})" size 52

        text f"{location_names[Player.location]}" size 52:
            anchor (1.0, 0.0) pos (1.0, 0.0)

    showif config.developer:
        imagebutton anchor (0.0, 1.0) pos (0.01, 0.99):
            idle "images/GUI/phone/phone_received_icon.webp" hover "images/GUI/phone/phone_send_icon.webp"
            action Function(renpy.call, "cheat_menu", Player.focused_Girl, from_current = True)
            focus_mask True
