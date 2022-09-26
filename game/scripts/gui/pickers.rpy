screen Girl_picker():
    if not renpy.get_screen("say") and not renpy.get_screen("Action_menu"):
        for G in active_Girls:
            if renpy.showing(f"{G.tag}_sprite"):
                button:
                    background None
                    anchor (0.5, 0.5) pos (G.sprite_location, 0.6) xysize (500, 1800)
                    action Function(renpy.call, "chat_menu", G, from_current = True)

screen Wardrobe_picker(Girl):
    window anchor (0.5, 0.5) pos (0.5, 0.5) xysize (int(6.2*512), 1600):
        vpgrid:
            cols 6
            spacing 0

            mousewheel True
            draggable True

            side_yfill True

            imagebutton anchor (0.5, 0.5) pos (0.5, 0.5) xysize (512, 512):
                auto "exit_%s"
                action Return("quit")

            for Clothing in Girl.Wardrobe.Clothes.values():
                imagebutton anchor (0.5, 0.5) pos (0.5, 0.5) xysize (512, 512):
                    idle "images/GUI/phone/phone_received_icon.png" hover "images/GUI/phone/phone_send_icon.png"
                    action Return(Clothing)

screen shopping_picker(Girl):
    window anchor (0.5, 0.5) pos (0.5, 0.5) xysize (int(6.2*512), 1600):
        vpgrid:
            cols 6
            spacing 0

            mousewheel True
            draggable True

            side_yfill True

            imagebutton anchor (0.5, 0.5) pos (0.5, 0.5) xysize (512, 512):
                auto "exit_%s"
                action Return("quit")

            for Clothing in register_Clothes(Girl):
                if Clothing.name not in Girl.Wardrobe.Clothes.keys():
                    imagebutton anchor (0.5, 0.5) pos (0.5, 0.5) xysize (512, 512):
                        idle "images/GUI/phone/phone_received_icon.png" hover "images/GUI/phone/phone_send_icon.png"
                        action Return(Clothing)
