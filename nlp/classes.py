MULTIPLE_INDEX = 101

CLASSES = {
    0: 'accident',
    1: 'thief',
    2: 'burglary',
    3: 'violence',
    4: 'press',
    5: 'harrasment',
    6: 'natural',
    7: 'vandalism',
    8: 'drugs',
    9: 'demo',
    10: 'witness',
    11: 'prison',
    100: 'other',
    MULTIPLE_INDEX: 'multiple'
}

WORDS = {
    # accident
    0: ['unfall', 'autounfall', 'verkehrsunfall', 'crash', 'stoß', 'fahrbahn', 'unfallflucht', 'trunkenheit',
        'verkehrsunfallflucht', 'angefahren', 'unfäll', 'umgefahren'],
    # thief
    1: ['diebstahl', 'dieb', 'diebe', 'geklaut', 'überfall', 'ueberfall', 'raub', 'raubüberfall', 'stehlen',
        'gestohlen',
        'aufbrüche', 'aufbruch', 'entwendet', 'enkeltrick', 'bestiehlt', 'taschendieb', 'autotieb', 'räuber',
        'bestohlen'],
    # burblary
    2: ['einbruch', 'aufgebrochen', 'einbrecher', 'einbrechen', 'einbrüche', 'erbeuten', 'aufbrecher', 'überfall',
        'ueberfall', 'einbrueche',
        ],
    # violence
    3: ['schlägerei', 'messer', 'pistole', 'schießerei', 'kampf', 'faust', 'körperverletzung', 'erpressung', 'mord',
        'tötungsdelikt', 'greift',
        'angegriffen', 'beworfen', 'schlaegerei', 'geschlagen', 'tötung', 'töten', 'koerperlich', 'koerperverletzung',
        'toetung', 'toeten'],
    # bp pressemeldung
    4: ['wochenendmeldung', 'presse'],
    # harrassment
    5: ['beleidigung', 'beschimpfen', 'spucken', 'beleidigte', 'beleidigt', 'beschimpfte', 'beschimpfungen',
        'beschimpfung', 'belästigt', 'belaestigt', 'belästigung', 'sex', 'belaestigung'],
    # natural
    6: ['blitzeinschlag', 'blitz', 'gewitter', 'donner', 'sturm', 'feuer', 'brennen', 'küchenbrand', 'brand',
        'ausgebrannt'],
    # vandalism
    7: ['sachbeschädigung', 'vandalismus', 'randaliert', 'graffiti', 'sprayer', 'beschmiert', 'graffitisprayer',
        'sachbeschaedigung', 'randale', 'randal', 'zerkratzt', 'beschädigt', 'zerstochen', 'beschaedigt',
        'beschäd',
        ],
    # drugs
    8: ['alkohol', 'drogen', 'marijuhana', 'lsd', 'trunkenheit', 'berauscht', 'promille', 'trunken', 'btm'],
    # demonstration
    9: ['demonstration'],
    10: ['zeugenaufruf'],
    11: ['festnahme']}
