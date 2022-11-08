init -1:
        
    define ch_farouk = Character("[Farouk.name]", who_color = "#592c99")
    define ch_farouk_tele = Character("[Farouk.name]", who_color = "#592c99", what_italic = True)

init python:

    def create_Farouk():
        Farouk = NPCClass("Farouk", voice = ch_farouk)

        return Farouk