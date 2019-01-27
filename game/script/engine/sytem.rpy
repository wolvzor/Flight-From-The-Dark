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