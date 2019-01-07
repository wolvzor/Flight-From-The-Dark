label section222:

    "As you go on you discover a forest path that divides at the point you join it."

    menu:
        "If you wish to use your Kai Discipline of Tracking, turn to 67." if 'Tracking' in player_discipline_list:
            call section067
        "If you wish to take the south fork, turn to 140.":
            call section140
        "If you wish to take the east fork, turn to 252.":
            call section252

    return