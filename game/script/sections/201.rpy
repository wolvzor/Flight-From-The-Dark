init python:
    passive_heal_check()

label section201:

    "You follow the rough track for nearly an hour when you notice ahead of you another wider path branching off towards the south."

    menu:
        "If you wish to turn south along the new path, turn to 238.":
            call section238
        "But if you wish to head east, turn to 15.":
            call section015
        "Or if you wish to go west, turn to 130.":
            call section130

    return