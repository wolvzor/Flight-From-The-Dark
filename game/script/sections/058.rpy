init python:
    passive_heal_check()

label section058:

    "Bracing yourself for the run, you head off down the ridge at a steady pace. To the west, the army of the Darklords looks like a giant pot of black ink that has been spilled between the mountains and is spreading into the land below."

    "You have been running for twenty minutes when you catch sight of a pack of Doomwolves lining a shallow ridge to your right."

    menu:
        "If you decide to flatten yourself against the rocks along the side of the road and wait until they pass, turn to 251.":
            call section251
        "If you decide to carry on running, but draw your weapon just in case they attack, turn to 160.":
            call section160

    return