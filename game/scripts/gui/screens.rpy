init -3:

    style default:
        font "dungeon.ttf"
        size 36

    style window:
        background Frame("images/GUI/window.webp", 24, 24)

        left_margin 12
        right_margin 12
        top_margin 12
        bottom_margin 12

        left_padding 50
        right_padding 50
        top_padding 50
        bottom_padding 50

        xminimum 10
        xmaximum 1000
        yminimum 10

    style say_what_window is default:
        background Frame("images/GUI/word_balloon.webp", 100, 100)

        left_padding 50
        right_padding 50
        top_padding 50
        bottom_padding 50

        xminimum 200
        xmaximum 800
        yminimum 0

    style say_who_window:
        background Frame("images/GUI/word_balloon.webp", 60, 60)

        left_padding 40
        right_padding 40
        top_padding 40
        bottom_padding 40

        xminimum 150

    style choice_menu is default

    style choice_menu_window is window:
        background None

    style choice_menu_text is button_text clear:
        size 48

    style choice_menu_button is button:
        xminimum int(config.screen_width*0.2)
        xmaximum int(config.screen_width*0.2)
        yminimum int(config.screen_height*0.04)

    style mm_button:
        size_group "mm"

    style gm_nav_button:
        size_group "gm_nav"

    style pref_frame:
        xfill True
        
        xmargin 10
        top_margin 10

    style pref_vbox:
        xfill True

    style pref_button:        
        xalign 1.0

    style pref_slider:
        xalign 1.0

        xmaximum 384
        
    style quick_button is default:
        background None

        xpadding 10

    style quick_button_text is default:
        size 48

        idle_color "#8888"
        hover_color "#ccc"
        insensitive_color "#4448"

init -1 python hide:
    theme.tv(
        widget = "#6A7183",
        widget_hover = "#1A2B47",
        widget_text = "#C9C9CB",
        widget_selected = "#E3E3E4",
        disabled = "#4448",
        disabled_text = "#4448",
        label = "#39435E",
        frame = "#ADB9CC",

        mm_root = "black_screen",
        gm_root = "black_screen",
        
        rounded_window = False)

screen say(who, what, two_window = False):
    window:
        anchor (0.5, 0.0) pos (0.12, 0.18)

        style "say_what_window"

        text what:
            size 40
            id "what"
            color "#000000"
            font "CRIMFBRG.ttf"
            text_align 0.5

    if who:
        window:
            anchor (0.5, 0.0) pos (0.12, 0.13)

            style "say_who_window"

            text who:
                size 40
                id "who"
                font "CRIMFBRG.ttf"

    use quick_menu

screen choice(items):
    style_prefix "choice_menu"

    fixed anchor (0.5, 0.0) pos (0.12, 0.37) xysize (int(config.screen_width*0.2), int(config.screen_height*0.45)):
        viewport:
            mousewheel True
            draggable True

            side_yfill True

            has vbox:
                spacing 4

            for caption, action, chosen in items:
                if action:
                    if " (locked)" in caption:
                        $ caption = caption.replace(" (locked)", "")

                        button:
                            background "#424242"
                            action None
                            text caption:
                                color "#6E6E6E"
                    else:
                        button:
                            action action
                            text caption
                else:
                    text caption

screen nvl(dialogue, items = None):
    use texting(dialogue, items)

screen input(prompt):
    window:
        anchor (0.5, 1.0) pos (0.5, 0.9)

        style "input_window"

        has vbox:
            xalign 0.5

        text prompt:
            size 48
            xalign 0.5
            style "input_prompt"
            color "#000000"

        input:
            size 60
            xalign 0.5
            id "input"
            style "input_text"
            color "#6e6e6e"

    use quick_menu

screen main_menu():
    tag menu

    window:
        style "mm_root"

    frame:
        background None
        style_group "mm"
        align (0.98, 0.98)

        has vbox:
            spacing 4

        textbutton _("Start Game") action Start() text_size 60
        textbutton _("Load Game") action ShowMenu("load") text_size 60
        textbutton _("Preferences") action ShowMenu("preferences") text_size 60
        textbutton _("Quit") action Quit(confirm = False) text_size 60

screen navigation():
    window:
        style "gm_root"

    frame:
        background None
        style_group "gm_nav"
        align (0.98, 0.98)

        has vbox:
            spacing 4

        textbutton _("Return") action Return() text_size 60
        textbutton _("Preferences") action ShowMenu("preferences") text_size 60
        textbutton _("Save Game") action ShowMenu("save") text_size 60
        textbutton _("Load Game") action ShowMenu("load") text_size 60
        textbutton _("Main Menu") action MainMenu() text_size 60
        textbutton _("Quit") action Quit() text_size 60

screen file_picker():
    frame:
        style "file_picker_frame"
        background None

        has vbox:
            spacing 4

        hbox:
            style_group "file_picker_nav"
            spacing 4

            textbutton _("Previous"):
                action FilePagePrevious()
                text_size 60

            textbutton _("Auto"):
                action FilePage("auto")
                text_size 60

            textbutton _("Quick"):
                action FilePage("quick")
                text_size 60

            for i in range(1, 9):
                textbutton str(i):
                    action FilePage(i)
                    text_size 60

            textbutton _("Next"):
                action FilePageNext()
                text_size 60

        $ columns = 2
        $ rows = 5

        grid columns rows:
            spacing 4
            transpose True
            xfill True
            style_group "file_picker"

            for i in range(1, columns*rows + 1):
                button:
                    action FileAction(i)
                    xfill True
                    ysize 0.145

                    has hbox:
                        spacing 30

                    add FileScreenshot(i):
                        yalign 0.5

                    $ file_name = FileSlotName(i, columns*rows)
                    $ file_time = FileTime(i, empty = _("Empty Slot."))
                    $ save_name = FileSaveName(i)

                    text "[file_name]. [file_time!t]\n[save_name!t]" size 48 yalign 0.5

                    key "save_delete" action FileDelete(i)

screen save():
    tag menu

    use navigation
    use file_picker

screen load():
    tag menu

    use navigation
    use file_picker

screen preferences():
    tag menu

    use navigation

    style_group "pref"

    grid 2 1:        
        xfill True

        vbox:
            frame:
                has vbox

                label _("Display") text_size 60
                textbutton _("Window") action Preference("display", "window") text_size 60
                textbutton _("Fullscreen") action Preference("display", "fullscreen") text_size 60

screen confirm(message, yes_action, no_action):
    modal True

    window:
        style "gm_root"

    frame:
        style_prefix "confirm"
        background None

        xfill True
        xmargin 100
        ypadding 50
        yalign 0.25

        vbox:
            xfill True
            spacing 50

            text _(message):
                text_align 0.5
                xalign 0.5
                size 48

            hbox:
                spacing 200
                xalign 0.5
                textbutton _("Yes") action yes_action text_size 60
                textbutton _("No") action no_action text_size 60

screen quick_menu():
    hbox:
        style_group "quick"

        xalign 1.0
        yalign 1.0

        textbutton _("Back") action Rollback()
        textbutton _("Save") action ShowMenu('save')
        textbutton _("Q.Save") action QuickSave()
        textbutton _("Q.Load") action QuickLoad()
