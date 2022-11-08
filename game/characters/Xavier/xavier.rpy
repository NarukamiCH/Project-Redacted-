init -1:
    
    define ch_xavier = Character("[Xavier.name]", who_color = "#1b867d", image = "Xavier_sprite")
    define ch_xavier_tele = Character("[Xavier.name]", who_color = "#1b867d", what_italic = True)

init python:

    def create_Xavier():
        Xavier = NPCClass("Xavier", voice = ch_xavier)

        Xavier.psychic = False

        Professors.append(Xavier)

        return Xavier