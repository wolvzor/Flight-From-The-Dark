init python:

    def passive_heal_check(endurance_current, endurance):
        if 'Healing' in character.player_discipline_list and endurance_current > endurance:
            endurance_current += 1
        return endurance_current

    def assign_discipline(discipline_choice):
        if ('Weaponskill' == discipline_choice):
            weapon_choice = renpy.random.choice(character.weaponskill_list)
            character.weaponskill_list = [item for item in character.weaponskill_list if item != weapon_choice]
            discipline_choice += ' (' + weapon_choice + ')'

        character.player_discipline_list.append(discipline_choice)
        character.discipline_list = [item for item in character.discipline_list if item[0] != discipline_choice]
        return discipline_choice