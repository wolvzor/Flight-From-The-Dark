init python:
    combat_score = 0
    endurance_score = 0
    combat_score_current = 0
    endurance_current = 0
    player_weapons = []
    player_backpack_items = []
    player_gold_crowns = 0
    player_special_items = []
    discipline_list = [('Camouflage','Camouflage'),('Hunting','Hunting'),('Sixth Sense','Sixth Sense'),('Tracking','Tracking'),('Healing','Healing'),('Weaponskill','Weaponskill'),('Mindshield','Mindshield'),('Mindblast','Mindblast'),('Animal Kinship','Animal Kinship'),('Mind Over Matter','Mind Over Matter')]
    player_discipline_list = []

    # TODO: Track deficits when items are lost in gameplay
    def random_item(random_int):
        statement = ''
        if (random_int == 1):
            global player_weapons
            player_weapons.append("Sword");
            statement = "a Sword"
        elif (random_int == 2):
            global player_special_items
            player_special_items.append("Helmet");
            global endurance_score
            endurance_score = endurance_score + 2;
            global endurance_current
            endurance_current = endurance_current + 2;
            statement = "a Helmet"
        elif (random_int == 3):
            global player_backpack_items
            player_backpack_items.append("Meal");
            player_backpack_items.append("Meal");
            statement = "two Meals"
        elif (random_int == 4):
            global player_special_items
            player_special_items.append("Chainmail Waistcoat");
            global endurance_score
            endurance_score = endurance_score + 4;
            global endurance_current
            endurance_current = endurance_current + 4;
            statement = "a Chainmail Waistcoat"
        elif (random_int == 5):
            global player_weapons
            player_weapons.append("Mace");
            statement = "a Mace"
        elif (random_int == 6):
            global player_backpack_items
            player_backpack_items.append("Healing Potion");
            statement = "a Healing Potion"
        elif (random_int == 7):
            global player_weapons
            player_weapons.append("Quarterstaff");
            statement = "a Quarterstaff"
        elif (random_int == 8):
            global player_weapons
            player_weapons.append("Spear");
            statement = "a Spear"
        elif (random_int == 9):
            global player_gold_crowns
            player_gold_crowns += 12;
            statement = "twelve Gold Crowns"
        else:
            global player_weapons
            player_weapons.append("Broadsword");
            statement = "a Broadsword"
        return statement


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

    "You are dressed in the green tunic and cloak of a Kai initiate. You have little with you to arm yourself for survival."

    # TODO: Consider enums for objects?
    $ player_weapons = ['Axe']
    $ player_backpack_items = ['Meal']

    "All you possess is an Axe, and a Backpack containing 1 Meal."

    $ player_gold_crowns = renpy.random.randint(0,9)

    "Hanging from your waist is a leather pouch containing %(player_gold_crowns)d Gold Crowns."

    $ player_special_items = ['Map of Sommerlund']

    "You discover amongst the smoking ruins of the monastery, a Map of Sommerlund showing the capital city of Holmgard and the land of Durenor, far to the east. You place the Map inside your tunic for safety."

    $ random_item_num = renpy.random.randint(0,9)
    $ statement = random_item(random_item_num)

    "You also found one of the following: %(statement)s."

    menu:

        "Would you like an explanation of how much of each item you can carry?"

        "Yes":
            call tutorial_carrying

        "No":
            pass

    menu:

        "Would you like an explanation on how equipment is used in the game?"

        "Yes":
            call tutorial_equipment

        "No":
            pass

    menu:

        "Would you like to see the rules for combat?"

        "Yes":
            call tutorial_combat

        "No":
            pass

    menu:

        "Would you like to learn about the levels of kai training?"

        "Yes":
            call tutorial_training

        "No":
            pass

    #Kai Wisdom
    "Your mission will be one of great danger, for the Darklords and their servants are a cruel and fierce enemy who give and expect no mercy."
    "Use the map to help you steer a correct course for the capital. Make notes as you progress through the story, for they will be of great help in future adventures."
    "Many things that you find will aid you during the adventure."
    "Some Special Items will be of use in future Lone Wolf adventures and others may be red herrings of no real use at all, so be selective in what you decide to keep."
    "There are many routes to the King, but only one involves a minimum of danger."
    "With a wise choice of Kai Disciplines and a great deal of courage, any player should be able to complete the mission, no matter how weak their initial COMBAT SKILL or ENDURANCE points score."
    "The honour and memory of the Kai Lords will go with you on your perilous journey."
    "Good luck!"

    call section1
