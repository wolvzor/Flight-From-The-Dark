init python:
    passive_heal_check()

label section153:

    # TODO this has a picture! https://www.projectaon.org/en/xhtml/lw/01fftd/sect153.htm
    "Before you are the tall grey-white walls and glimmering spires of Holmgard, the city’s banners fluttering from the battlements in the fresh morning breeze."
    "Stretching out towards the west, the River Eledil traces its course from the mountains of the Durncrag Range to the Holmgulf."
    "But below the mountain peaks you can see a vast black army marching relentlessly on towards the capital."

    "To your right you can see the highway heading off over the rolling plain towards Holmgard. At a gallop you could make the outer fieldworks of the city’s defences in less than an hour, but you would be in the open for most of the time and vulnerable to attack by Kraan."
    "Directly ahead of you, a wide river drifts sluggishly towards the Eledil. If you abandoned your horse, you could swim towards the outer defences under cover of the river banks."
    "Or there is a final alternative. To your left lies the Graveyard of the Ancients. These tombs and crumbling monuments to a forgotten age would conceal your approach but it is a forbidden area. Many are the unnamed horrors that lie there in restless sleep, waiting to consume the unwary trespasser."

    menu:
        "If you will try your luck by the highway, turn to 202.":
            call section202
        "If you feel that you stand a better chance of reaching the capital via the river then turn to 135.":
            call section135
        "Or if you are brave enough to risk the unknown perils of the Graveyard of the Ancients, turn to 329.":
            call section329

    return