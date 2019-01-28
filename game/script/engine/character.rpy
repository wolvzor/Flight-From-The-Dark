init python:

    class Character:
        def __init__(self):
            self.player_weapons = []
            self.player_backpack_items = []
            self.player_gold_crowns = 0
            self.player_special_items = []
            self.discipline_list = [('Camouflage','Camouflage'),('Hunting','Hunting'),('Sixth Sense','Sixth Sense'),('Tracking','Tracking'),('Healing','Healing'),('Weaponskill','Weaponskill'),('Mindshield','Mindshield'),('Mindblast','Mindblast'),('Animal Kinship','Animal Kinship'),('Mind Over Matter','Mind Over Matter')]
            self.player_discipline_list = []
            self.weaponskill_list = ['Dagger','Spear','Mace','Short Sword','Warhammer','Sword','Axe','Sword','Quarterstaff','Broadsword']
            self.player_weaponskill_list = []
            self.combat_skill = 1
            self.combat_skill_current = 1
            self.endurance = 1
            self.endurance_current = 1