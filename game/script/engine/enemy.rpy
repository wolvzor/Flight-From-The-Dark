init python:

    class Enemy:
        def __init__(self, name="Enemy", combat_skill=0, endurance=0):
            self.name = name
            self.combat_skill = combat_skill
            self.combat_skill_current = combat_skill
            self.endurance = endurance
            self.endurance_current = endurance