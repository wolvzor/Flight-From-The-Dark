init python:

    def passive_heal_check(endurance_current, endurance):
        if 'Healing' in character.player_discipline_list and endurance_current > endurance:
            endurance_current += 1
        return endurance_current