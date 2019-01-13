init python:
    passive_heal_check()

label section006:

    # TODO This has a picture! https://www.projectaon.org/en/xhtml/lw/01fftd/sect6.htm
    "In the distance you can hear the sound of horses galloping nearer. You crouch behind a tree and wait as the riders come closer. They are the cavalry of the King’s Guard wearing the white uniforms of His Majesty’s army."

    menu:
        "If you wish to call them, turn to 183.":
            call section183
        "If you wish to let them pass and then continue on your way through the forest, turn to 200.":
            call section200

    return