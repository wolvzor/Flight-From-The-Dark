init python:
    passive_heal_check()

label section141:

    "Your Sixth Sense has warned you that some of the creatures that attacked the monastery are searching the two paths for any survivors of their raid, but you can avoid both tracks by making your way through the undergrowth of the woods."

    menu:
        "If you wish to head south, turn to 56.":
            call section056
        "Or if you wish to cut through the heavier foliage towards the northeast, turn to 333.":
            call section333

    return
