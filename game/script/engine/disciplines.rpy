init python:

    def passive_heal_check():
        if 'Healing' in player_discipline_list and endurance_current > endurance_score:
            endurance_current += 1
        return