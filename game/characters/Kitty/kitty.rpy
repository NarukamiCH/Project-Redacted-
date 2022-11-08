init -1:
    
    define ch_kitty = Character("[Kitty.name]", who_color = "#9012d9", image = "Kitty_sprite")
    define ch_kitty_nvl = Character("[Kitty.name]", kind = nvl)

transform Kitty_color:
    matrixcolor TintMatrix("#9012d9")