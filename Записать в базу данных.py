# Код используется для создания и добавления разделов в базу данных.
"""
        # Записать секцию


        tomsk_city = City.query.filter_by(name='Tomsk').first()
        football_sport = Sport.query.filter_by(name='Football').first()
        tennis_sport = Sport.query.filter_by(name='Tennis').first()
        # basket_sport = Sport.query.filter_by(name='Basketball').first()
        # swimming_sport = Sport.query.filter_by(name='Swimming').first()
        # cycling_sport = Sport.query.filter_by(name='Cycling').first() Volleyball Section
        # dancing_sport = Sport.query.filter_by(name='Dancing').first() Yoga Section
        volleyball_sport = Sport.query.filter_by(name='Volleyball').first()
        yoga_sport = Sport.query.filter_by(name='Yoga').first()

        new_section = Section(name='Football Section',
                              description='Football is a team sport with a ball,'
                                          ' where players strive to score a goal against an opponent.'
                                          ' It includes two halves of 45 minutes each,'
                                          ' and the game is played by 11 players on each side.',
                              city=tomsk_city,
                              sport=football_sport)

        new_section2 = Section(name='Tennis Section',
                               description='Tennis is an individual or pair sport where players'
                                           ' throw the ball over the net using rackets.'
                                           ' The game consists of sets,'
                                           'each of which is won by the first one'
                                           ' to score a certain number of points (usually 6)',
                               city=tomsk_city,
                               sport=tennis_sport)

        '''new_section3 = Section(name='Basketball Section',
                               description='The section invites everyone of any age and level of '
                                           'training'
                                           'Individual approach to each participant'
                                           'Many years of coaching experience'
                                           'A unique atmosphere for each player',
                               city=kemerovo_city,
                               sport=basket_sport)

        new_section4 = Section(name='Swimming Section',
                               description='The section is open to everyone who wants to improve their '
                                           'swimming skills'
                                           'Experienced coaches will help you master different '
                                           'swimming styles'
                                           'Group and individual lessons'
                                           'Health, fitness and new achievements',
                               city=kemerovo_city,
                               sport=swimming_sport)'''

        new_section3 = Section(name='Volleyball Section',
                               description='Develop team spirit and physical fitness with us! '
                                           'Volleyball training will help you improve coordination, '
                                           'speed and impact strength. Everyone will find their dream '
                                           'team here!',
                               city=tomsk_city,
                               sport=volleyball_sport)

        new_section4 = Section(name='Yoga Section',
                               description='Find a balance between body and spirit through yoga. Our '
                                           'classes are aimed at developing flexibility, '
                                           'strengthening muscles and reducing stress. Yoga will help '
                                           'you find inner harmony and peace. Join us and start your '
                                           'journey to self-improvement!',
                               city=tomsk_city,
                               sport=yoga_sport)

        '''        new_section5 = Section(name='Cycling Section',
                               description='The section invites cycling enthusiasts of any level of '
                                           'training'
                                           'Improving cycling skills'
                                           'Group trips and competitions'
                                           'Training on different types of trails'
                                           'Exciting adventures',
                               city=chsk_city,
                               sport=cycling_sport)

        new_section6 = Section(name='Dancing Section',
                               description='A wide range of dance styles for adults and children'
                                           'Modern, classical and folk dances'
                                           'Experienced teachers'
                                           'Friendly and creative atmosphere'
                                           'Unlocking potential and expressing emotions through movement',
                               city=chsk_city,
                               sport=dancing_sport)'''

        for param in get_parameters_tsk('Football Section'):
            new_section.parameters.append(
                Parameter(name=param['name'], value=param['value'], category=param['category']))

        for param in get_parameters_tsk('Tennis Section'):
            new_section2.parameters.append(
                Parameter(name=param['name'], value=param['value'], category=param['category']))

        for param in get_parameters_tsk('Volleyball Section'):
            new_section3.parameters.append(
                Parameter(name=param['name'], value=param['value'], category=param['category']))

        for param in get_parameters_tsk('Yoga Section'):
            new_section4.parameters.append(
                Parameter(name=param['name'], value=param['value'], category=param['category']))

        db.session.add_all([new_section, new_section2, new_section3, new_section4])
        db.session.commit()
"""


# Создает города 10 шт

"""
        # Создает города 10 шт
        
        city_names = ['Barnaul', 'Ufa', 'Tomsk', 'Novosibirsk', 'Kemerovo', 'Moscow', 'Saint Petersburg',
                      'Ekaterinburg', 'Kazan', 'Chelyabinsk']

        existing_city_names = [city.name for city in City.query.all()]

        new_cities = [City(name=city_name) for city_name in city_names if city_name not in existing_city_names]

        db.session.add_all(new_cities)
        db.session.commit() 
"""


# Создаем виды спорта 10 шт

'''
        sport_names = ['Football', 'Basketball', 'Swimming', 'Tennis', 'Volleyball', 'Running', 'Yoga', 'Gymnastics',
                       'Cycling', 'Dancing']
        
        existing_sport_names = [sport.name for sport in Sport.query.all()]

        new_sports = [Sport(name=sport_name) for sport_name in sport_names if sport_name not in existing_sport_names]

        db.session.add_all(new_sports)
        db.session.commit()
        '''
