label section130:

    $ passive_heal_check(character.endurance_current, character.endurance)

    "You soon reach a small clearing in the woods. A bench, carved from a fallen tree is set in the centre of the clearing. You are hungry and must now eat a Meal here."

    # TODO MEAL STUFF

    menu:
        "When you have finished, if you decide to leave the clearing by the south way, turn to 28.":
            call section028
        "Or if you prefer the smaller track that leads eastwards into the forest, turn to 201.":
            call section201

    return