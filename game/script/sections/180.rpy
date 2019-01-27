label section180:

    $ passive_heal_check(character.endurance_current, character.endurance)

    "They see you raise your weapon, and they instantly attack you. If you decide to fight them, you must fight them one at a time."

    # TODO Figure out how we want to evade combat?

    "Leader: COMBAT SKILL 15   ENDURANCE 22"

    "Soldier 1: COMBAT SKILL 13   ENDURANCE 20"

    "Soldier 2: COMBAT SKILL 12   ENDURANCE 20"

    # TODO this is temporary; will be replaced once combat has been added
    menu:
        "If you kill all three of them, turn to 62.":
            call section062
        "If you wish to evade combat, turn to 22.":
            call section022

    return