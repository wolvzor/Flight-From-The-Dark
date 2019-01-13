init python:
    passive_heal_check()

label section254:

    "Your Tracking ability tells you that several trails from the right path lead off in the direction of the left path. They have been made by large wolves. The Darklords use such beasts to scout for their armies. They are vicious creatures and are often ridden by Giaks."
    "The left path leads towards Holmgard, and the right path leads off towards the Durncrag Mountains. The choice of route is yours."

    menu:
        "If you wish to turn left, go to 32.":
            call section032
        "If you wish to turn right, go to 146.":
            call section146

    return