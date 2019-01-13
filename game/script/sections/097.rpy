init python:
    passive_heal_check()

label section097:

    # TODO This has a picture! https://www.projectaon.org/en/xhtml/lw/01fftd/sect97.htm

    "Ahead of you, you can see a fierce battle raging across a stone bridge. The clash of steel and the cries of men and beasts echo through the forest."
    "In the midst of the fighting, you see Prince Pelathar, the King’s son. He is in combat with a large grey Gourgaz who is wielding a black axe above his scaly head. Suddenly, the Prince falls wounded—a black arrow in his side."

    menu:
        "If you wish to defend the fallen Prince, turn to 255.":
            call section255
        "If you wish to run into the forest, turn to 306.":
            call section306

    return