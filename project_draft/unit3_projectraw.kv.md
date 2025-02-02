#:kivy 2.0.0

Screen:

    MDLabel:
        text: "Hello World!"
        halign: "center"
        font_size: "36sp"
        pos_hint: {"center_x": 0.5, "center_y": 0.7}

    MDChip:
        text: "Click me!"
        icon_left: "avatar.png"
        icon_right: "close-circle-outline"
        pos_hint: {"center_x": 0.5, "center_y": 0.5}
