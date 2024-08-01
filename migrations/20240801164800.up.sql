ALTER TABLE places ADD COLUMN commune VARCHAR(255);

INSERT INTO
    places (id, name, commune)
VALUES (
        1,
        'Disneyland',
        'Marne-la-Vallée'
    ),
    (2, 'Musée du Louvre', 'Paris'),
    (
        3,
        'Château de Versailles',
        'Versailles'
    ),
    (4, 'Tour Eiffel', 'Paris'),
    (5, 'Centre Pompidou', 'Paris'),
    (6, 'Musée d Orsay', 'Paris'),
    (
        7,
        'Cité des sciences et de l industrie de La Villette',
        'Paris'
    ),
    (
        8,
        'Le Puy du Fou',
        'Les Épesses'
    ),
    (
        9,
        'Cité médiévale',
        'Carcassonne'
    ),
    (10, 'Parc Astérix', 'Plailly'),
    (
        11,
        'Parc du Futuroscope',
        'Chasseneuil-du-Poitou'
    ),
    (
        12,
        'Château des Ducs de Bretagne',
        'Nantes'
    ),
    (
        13,
        'Zoo parc de Beauval',
        'Saint-Aignan'
    ),
    (
        14,
        'Cathédrale de Reims',
        'Reims'
    ),
    (
        15,
        'Cimetière américain d Omaha',
        'Colleville-sur-Mer'
    );