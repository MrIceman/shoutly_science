CLASSES = {
    0: 'accident',
    1: 'thief',
    2: 'burglary',
    3: 'violence',
    4: 'collection',
    5: 'harrasment',
    6: 'natural',
    7: 'vandalism',
    8: 'drugs',
    100: 'other',
}

WORDS = {
    # accident
    0: ['unfall', 'autounfall', 'verkehrsunfall', 'crash', 'stoß', 'fahrbahn', 'unfallflucht', 'trunkenheit',
        'verkehrsunfallflucht'],
    # thief
    1: ['diebstahl', 'dieb', 'diebe', 'geklaut', 'überfall', 'raub', 'raubüberfall', 'stehlen', 'gestohlen',
        'aufbrüche', 'aufbruch', 'entwendet', 'enkeltrick', 'bestiehlt', 'taschendieb', 'autotieb'],
    # burlary
    2: ['einbruch', 'aufgebrochen', 'einbrecher', 'einbrechen', 'einbrüche'],
    # violence
    3: ['schlägerei', 'messer', 'pistole', 'schießerei', 'kampf', 'faust', 'körperverletzung', 'erpressung', 'mord', 'tötungsdelikt', 'greift',
        'angegriffen', 'beworfen', 'schlaegerei', 'geschlagen'],
    # bp pressemeldung
    4: ['pressemeldung', 'pressemeldungen'],
    # harrassment
    5: ['beleidigung', 'beschimpfen', 'spucken', 'beleidigte', 'beleidigt', 'beschimpfte', 'beschimpfungen',
        'beschimpfung', 'belästigt', 'belaestigt'],
    # natural
    6: ['blitzeinschlag', 'blitz', 'gewitter', 'donner', 'sturm', 'feuer', 'brennen'],
    # vandalism
    7: ['sachbeschädigung', 'vandalismus', 'randaliert', 'graffiti', 'sprayer', 'beschmiert', 'graffitisprayer'],
    # drugs
    8: ['alkohol', 'drogen', 'marijuhana', 'lsd']
}
