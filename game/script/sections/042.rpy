label section042:

    $ passive_heal_check(character.endurance_current, character.endurance)

    "You follow the track for nearly an hour when you come to a crossroads."

    menu:
        "If you wish to continue east, turn to 86.":
            call section086
        "If you would rather head north, turn to 238.":
            call section238
        "If you decide to venture south, turn to 157.":
            call section157
        "Or if you prefer to go west, turn to 147.":
            call section147

    return