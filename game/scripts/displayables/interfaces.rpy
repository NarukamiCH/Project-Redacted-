init python:

    def Girl_color(d):
        if Player.focused_Girl.tag == "Rogue":
            return Rogue_color(d)
        elif Player.focused_Girl.tag == "Kitty":
            return Kitty_color(d)
        elif Player.focused_Girl.tag == "Laura":
            return Laura_color(d)
        elif Player.focused_Girl.tag == "Storm":
            return Storm_color(d)
        elif Player.focused_Girl.tag == "Jean":
            return Jean_color(d)

transform love_color:
    matrixcolor TintMatrix("#c11b17")

transform trust_color:
    matrixcolor TintMatrix("#2554c7")

transform desire_color:
    matrixcolor TintMatrix("#f3a3b3")

transform Rogue_color:
    matrixcolor TintMatrix("#2ca05aff")

transform Kitty_color:
    matrixcolor TintMatrix("#9012d9")

transform Laura_color:
    matrixcolor TintMatrix("#d9bb12")

transform Storm_color:
    matrixcolor TintMatrix("#85f2f9")

transform Jean_color:
    matrixcolor TintMatrix("#d92912")

image exit_hover:
    "images/GUI/icons/exit_hover.webp"

    anchor (0.5, 0.5) pos (0.5, 0.5) zoom 1.0

image exit_idle:
    "images/GUI/icons/exit_idle.webp"

    anchor (0.5, 0.5) pos (0.5, 0.5) zoom 1.0