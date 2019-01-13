label section086:

    $ passive_heal_check(endurance_current, endurance)

    "You soon reach another crossroads."

    menu:
        "If you wish to journey east, turn to 6.":
            call section006
        "If you wish to head north, turn to 35.":
            call section035
        "If you prefer to go south, turn to 167.":
            call section167
        "Or if you wish to turn west, turn to 42.":
            call section042

    return