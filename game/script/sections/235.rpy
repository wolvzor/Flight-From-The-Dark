label section235:

    $ passive_heal_check(character.endurance_current, character.endurance)

    "The Prince’s horse is indeed a magnificent animal, fast and sure of foot. You gallop along the twisting track as if it were a straight highway, until the noise of battle has disappeared far behind you."

    "You are hungry and must eat a Meal during your ride."

    $ meal_check()

    "After several miles, the path stops abruptly at a junction. There is a signpost, but it has been hacked down."

    menu:
        "If you wish to use your Kai Discipline of Tracking, turn to 254." if 'Tracking' in character.player_discipline_list:
            call section254
        "If you wish to turn left, go to 32.":
            call section032
        "If you wish to turn right, go to 146.":
            call section146

    return