init python:
    passive_heal_check()

label section115:

    "You stumble into the first building and fall to the floor exhausted."
    "You can smell cooked meat. You notice a small cauldron hanging over the embers of a dying fire, and a large oak table that has been set for a meal. Whoever lived here must have left in a great hurry this very morning."
    "There is water in a jug and a loaf of fresh bread on the table."

    menu:
        "If you decide to take a quick Meal, turn to 150.":
            call section150
        "If you decide to search the building, turn to 177.":
            call section177
        "If you would rather leave now and continue your run, turn to 83.":
            call section083

    return