init python:
    passive_heal_check()

label section083:

    "You have run about a mile when three soldiers appear from beneath a small footbridge. They demand that you halt and drop your weapons and equipment."

    "They are bloodstained and unshaven. Their leader is wearing the tunic of a soldier of the Toran garrison."

    menu:
        "If you possess the Kai Discipline of Sixth Sense, turn to 45." if 'Sixth Sense' in player_discipline_list:
            call section045
        "If you wish to do as they say, turn to 205.":
            call section205
        "If you wish to prepare to fight them, turn to 180.":
            call section180
        "If you demand to know what they want, turn to 232.":
            call section232

    return