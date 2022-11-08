init -1:
    
    define ch_player = Character("[Player.name]", who_color = "#0a84b4")
    define ch_player_nvl = Character("[Player.name]", kind = nvl)

init python:

    def create_Player():
        Player = PlayerClass(
            name,
            voice = ch_player, text = ch_player_nvl,
            skin_color = color)
            
        return Player