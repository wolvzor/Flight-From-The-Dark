label section010:

    $ passive_heal_check(character.endurance_current, character.endurance)

    "You are sweating and your legs ache. In the middle distance you can see a group of cottages."

    menu:
        "If you wish to enter a cottage and rest for a while, turn to 115.":
            call section115
        "If you wish to press on, turn to 83.":
            call section083

    return