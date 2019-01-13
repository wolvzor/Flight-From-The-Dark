init python:
    passive_heal_check()

label section252:

    "In the centre of a small clearing you see a group of humans talking excitedly and gesturing wildly with their hands. There are two children, three men, and a woman."
    "Their belongings are wrapped in bundles which they carry slung over their shoulders. Their clothes look well made and expensive but they are dirty and torn."

    menu:
        "If you wish to approach them and ask who they are, turn to 155.":
            call section155
        "If you wish to avoid them and continue onwards on your mission, turn to 70.":
            call section070

    return