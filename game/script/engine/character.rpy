init python:

    class Character:
        def __init__(self):
            self.player_weapons = []
            self.player_backpack_items = []
            self.player_gold_crowns = 0
            self.player_special_items = []
            self.discipline_list = [('Camouflage','Camouflage'),('Hunting','Hunting'),('Sixth Sense','Sixth Sense'),('Tracking','Tracking'),('Healing','Healing'),('Weaponskill','Weaponskill'),('Mindshield','Mindshield'),('Mindblast','Mindblast'),('Animal Kinship','Animal Kinship'),('Mind Over Matter','Mind Over Matter')]
            self.player_discipline_list = []
            self.combat_score = 15
            self.combat_score_current = 15
            self.endurance = 15
            self.endurance_current = 15