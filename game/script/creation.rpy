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

    menu:
        "Pick your first discipline."
        "Camouflage":
            $ first_discipline = "Camouflage"
        "Hunting":
            $ first_discipline = "Hunting"
        "Sixth Sense":
            $ first_discipline = "Sixth Sense"
        "Tracking":
            $ first_discipline = "Tracking"
        "Healing":
            $ first_discipline = "Healing"
        "Weaponskill":
            $ first_discipline = "Weaponskill"
        "Mindshield":
            $ first_discipline = "Mindshield"
        "Mindblast":
            $ first_discipline = "Mindblast"
        "Animal Kinship":
            $ first_discipline = "Animal Kinship"
        "Mind Over Matter":
            $ first_discipline = "Mind Over Matter"

    "You picked %(first_discipline)s as your first discipline."

    return
