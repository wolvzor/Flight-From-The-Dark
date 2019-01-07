label section070:

    # TODO This has a picture! https://www.projectaon.org/en/xhtml/lw/01fftd/sect70.htm
    "You have reached a small bridge. A track follows the stream towards the east. A much narrower path disappears into thick forest towards the south."

    menu:
        "If you wish to use the Kai Discipline of Sixth Sense, turn to 8." if 'Sixth Sense' in player_discipline_list:
            call section008
        "If you wish to go east, turn to 28.":
            call section028
        "If you wish to go south, turn to 157.":
            call section157

    return