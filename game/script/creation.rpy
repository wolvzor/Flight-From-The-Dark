label creation:

    "During your training as a Kai Lord you have developed fighting prowess—COMBAT SKILL and physical stamina—ENDURANCE."

    $ combat_score = renpy.random.randint(10,19)
    $ combat_score_current = combat_score
    $ endurance = renpy.random.randint(20,29)
    $ endurance_current = endurance

    "You have the following starting values for your COMBAT SKILL and ENDURANCE: %(combat_score)d and %(endurance)d."

    "When you fight, your COMBAT SKILL will be pitted against that of your enemy. A high score in this section is therefore very desirable."

    "If you are wounded in combat you will lose ENDURANCE points. If at any time your ENDURANCE points fall to zero or below, you are dead and the adventure is over."

    "Lost ENDURANCE points can be regained during the course of the adventure, but your number of ENDURANCE points can never go above the number with which you start your adventure."

    "Over the centuries, the Kai monks have mastered the skills of the warrior. These skills are known as the Kai Disciplines, and they are taught to all Kai Lords."

    "You have learnt only five of the skills. The choice of which five skills these are, is for you to make."

    "As all of the Disciplines may be of use to you at some point on your perilous quest, pick your five with care. The correct use of a Discipline at the right time can save your life."

    # TODO: Make this a function
    # TODO: Add random weaponization to weaponskill
    # TODO: Allow weaponskill to be added multiple times, but not for the same weapon

    "Pick your first discipline."

    $ discipline_list = [('Camouflage','Camouflage'),('Hunting','Hunting'),('Sixth Sense','Sixth Sense'),('Tracking','Tracking'),('Healing','Healing'),('Weaponskill','Weaponskill'),('Mindshield','Mindshield'),('Mindblast','Mindblast'),('Animal Kinship','Animal Kinship'),('Mind Over Matter','Mind Over Matter')]
    $ player_discipline_list = []

    $ first_discipline = renpy.display_menu(discipline_list)
    $ player_discipline_list.append(first_discipline)
    $ discipline_list = [item for item in discipline_list if item[0] != first_discipline]

    "You picked %(first_discipline)s as your first discipline."
    "Pick your second discipline."

    $ second_discipline = renpy.display_menu(discipline_list)
    $ player_discipline_list.append(second_discipline)
    $ discipline_list = [item for item in discipline_list if item[0] != second_discipline]

    "You picked %(second_discipline)s as your second discipline."
    "Pick your third discipline."

    $ third_discipline = renpy.display_menu(discipline_list)
    $ player_discipline_list.append(third_discipline)
    $ discipline_list = [item for item in discipline_list if item[0] != third_discipline]

    "You picked %(third_discipline)s as your third discipline."
    "Pick your fourth discipline."

    $ fourth_discipline = renpy.display_menu(discipline_list)
    $ player_discipline_list.append(fourth_discipline)
    $ discipline_list = [item for item in discipline_list if item[0] != fourth_discipline]

    "You picked %(fourth_discipline)s as your fourth discipline."
    "Pick your fifth discipline."

    $ fifth_discipline = renpy.display_menu(discipline_list)
    $ player_discipline_list.append(fifth_discipline)
    $ discipline_list = [item for item in discipline_list if item[0] != fifth_discipline]
    # TODO: make this more human readable
    $ player_discipline_list_string = ', '.join(player_discipline_list)

    "You picked %(fifth_discipline)s as your fifth discipline."

    "Your total disciplines are %(player_discipline_list_string)s"

    return
