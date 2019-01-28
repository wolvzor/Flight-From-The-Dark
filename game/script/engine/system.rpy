init python:

    def meal_check():
        if 'Hunting' in character.player_discipline_list:
            renpy.say(None, "With your Hunting skill, you hunt enough meat to count as a Meal. You eat well.")
            return
        elif 'Meal' in character.player_backpack_items:
            character.player_backpack_items.remove('Meal')
            renpy.say(None, "You remove a Meal from your backpack and eat it. You feel sated for now.")
            return
        elif character.endurance > 3:
            character.endurance = character.endurance - 3
            renpy.say(None, "You rummage in your backpack, but find no Meals available. Your stomach grumbles in protest. Lose three ENDURANCE points.")
            return
        else:
            renpy.say(None, "Without a proper meal or the requisite skills to hunt, your weak and frail body succumbs to starvation.")
            renpy.call("gameover")

    def combat(enemy_name, enemy_combat_skill, enemy_endurance):
        sample_combat_result_table = [(12,0),(3,5),(4,4),(5,4),(6,3),(7,2),(8,2),(9,1),(10,0),(11,0)]
        renpy.say(None, "The combat begins!")
        combat_skill = character.combat_skill
        combat_ratio = combat_skill - enemy_combat_skill
        renpy.say(None, "Your current COMBAT SKILL is [combat_skill]. [enemy_name]'s COMBAT SKILL is [enemy_combat_skill]. The Combat Ratio is [combat_ratio].")
        while(character.endurance > 0 and enemy_endurance > 0):
            random_number = renpy.random.randint(0,9)
            renpy.say(None, "The random number chosen for this round was [random_number].")
            combat_result = sample_combat_result_table[random_number]
            renpy.say(None, "[enemy_name] takes [combat_result[0]] damage.")
            enemy.endurance = enemy_endurance - combat_result[0]
            renpy.say(None, "Lone Wolf takes [combat_result[1]] damage.")
            character.endurance = character.endurance - combat_result[1]
        renpy.say(None, "The combat is over!")
        renpy.say(None, "Enemy endurance points: [enemy_endurance]")
        renpy.say(None, "Lone Wolf endurance points: [character.endurance]")
        return

