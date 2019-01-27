label section001:

    $ passive_heal_check(character.endurance_current, character.endurance)

    "You must make haste for you sense it is not safe to linger by the smoking remains of the ruined monastery. The black-winged beasts could return at any moment."
    "You must set out for the Sommlending capital of Holmgard and tell the King the terrible news of the massacre: that the whole élite of Kai warriors, save yourself, have been slaughtered."
    "Without the Kai Lords to lead her armies, Sommerlund will be at the mercy of their ancient enemy, the Darklords."

    "Fighting back tears, you bid farewell to your dead kinsmen. Silently, you promise that their deaths will be avenged. You turn away from the ruins and carefully descend the steep track."

    "At the foot of the hill, the path splits into two directions, both leading into a large wood."

    menu:
        "If you wish to use your Kai Discipline of Sixth Sense, turn to 141" if 'Sixth Sense' in character.player_discipline_list:
            call section141
        "If you wish to take the right path into the wood, turn to 85.":
            call section085
        "If you wish to follow the left track, turn to 275.":
            call section275

    return