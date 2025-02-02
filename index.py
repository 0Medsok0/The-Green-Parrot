from flask import Flask, render_template, redirect, url_for, request, send_from_directory
from flask_sqlalchemy import SQLAlchemy
from wtforms import Form, BooleanField, StringField, PasswordField, validators, SelectField
from flask_wtf import FlaskForm
from parameters import *
from mod import db, City, Sport, Section, Parameter, init_db
from sqlalchemy import text

app = Flask(__name__)
app.config['SECRET_KEY'] = 'your-secret-key'
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///site.db'
# Инициализируем модели
init_db(app)


@app.route('/')
def home():
    cities = City.query.all()
    return render_template('home.html', cities=cities)

@app.route('/search', methods=['GET', 'POST'])
def search():
    form = SearchForm()
    cities = City.query.all()
    if form.validate_on_submit():
        print(form.data)
        sections = Section.query.filter_by(city_id=form.city.data, sport_id=form.sport.data)
        selected_parameters = [
            form.physical_fitness.data,
            form.schedule.data,
            form.location.data,
            f"{form.cost.data}",
            form.coach_reputation.data,
            form.atmosphere.data,
            form.club_achievements.data,
            form.development_opportunities.data,
        ]
        for parameter_value in selected_parameters:
            sections = sections.filter(Section.parameters.any(Parameter.value.like(f"%{parameter_value}%")))
        sections = sections.all()

        if sections:
            return render_template('search.html', form=form, sections=sections, cities=cities, title="Search")
        else:
            return render_template('search.html', form=form, no_results=True, cities=cities, title="Search")

    return render_template('search.html', form=form, cities=cities, title="Search")

@app.route('/section/<int:id>')
def section(id):
    section = Section.query.get_or_404(id)
    cities = City.query.all()
    return render_template('section.html', section=section, cities=cities, title=section.name)

@app.route('/page1')
def page1():
    cities = City.query.all()
    return render_template('page1.html', cities=cities, title="Новости спорта")

@app.route('/page2')
def page2():
    cities = City.query.all()
    return render_template('page2.html', cities=cities, title="Спортивное питание")

@app.route('/page3')
def page3():
    cities = City.query.all()
    return render_template('page3.html', cities=cities, title="Спортивная одежда")

@app.route('/page4')
def page4():
    cities = City.query.all()
    return render_template('page4.html', cities=cities, title="Page 1")

@app.route('/page5')
def page5():
    cities = City.query.all()
    return render_template('page5.html', cities=cities, title="Page 2")

@app.route('/page6')
def page6():
    cities = City.query.all()
    return render_template('page6.html', cities=cities, title="Page 3")



if __name__ == '__main__':
    with (app.app_context()):
        db.create_all()
        # db.session.execute(text('ALTER TABLE city ADD COLUMN image VARCHAR(200)'))
        # db.session.commit()

        def add_section_if_not_exists(name, description, city, sport, parameters):

            ufa_city = City.query.filter_by(name='Ufa').first()
            dancing_sport = Sport.query.filter_by(name='Dancing').first()
            basket_sport = Sport.query.filter_by(name='Basketball').first()
            swimming_sport = Sport.query.filter_by(name='Swimming').first()

            existing_section = Section.query.filter_by(name=name).first()
            if existing_section:
                return existing_section

            # UFA
            new_section = add_section_if_not_exists('Dancing Section',
                                                    'A fun and energetic dancing section for all levels.',
                                                    ufa_city,
                                                    dancing_sport,
                                                    get_parameters("Dansing Section"))

            new_section2 = add_section_if_not_exists('Dancing Section 2',
                                                     'A friendly and supportive dancing section for beginners.',
                                                     ufa_city,
                                                     dancing_sport,
                                                     get_parameters('Dansing Section 2'))

            new_section3 = add_section_if_not_exists('Basketball Section',
                                                     'A friendly and supportive dancing section for beginners.',
                                                     ufa_city,
                                                     basket_sport,
                                                     get_parameters('Basketball Section'))

            new_section4 = add_section_if_not_exists('Swimming Section',
                                                     'A friendly and supportive dancing section for beginners.',
                                                     ufa_city,
                                                     swimming_sport,
                                                     get_parameters('Swimming Section'))

            for param in get_parameters('Dancing Section'):
                new_section.parameters.append(
                    Parameter(name=param['name'], value=param['value'], category=param['category']))

            for param in get_parameters('Dancing Section 2'):
                new_section2.parameters.append(
                    Parameter(name=param['name'], value=param['value'], category=param['category']))

            for param in get_parameters('Basketball Section'):
                new_section3.parameters.append(
                    Parameter(name=param['name'], value=param['value'], category=param['category']))

            for param in get_parameters('Swimming Section'):
                new_section4.parameters.append(
                    Parameter(name=param['name'], value=param['value'], category=param['category']))

            db.session.add_all([new_section, new_section2, new_section3, new_section4])
            db.session.commit()

            return new_section, new_section2, new_section3, new_section4


        def add_section_if_not_exists_barn(name, description, city, sport, parameters):
            barn_city = City.query.filter_by(name='Barnaul').first()
            football_sport = Sport.query.filter_by(name='Football').first()
            tennis_sport = Sport.query.filter_by(name='Tennis').first()
            basket_sport = Sport.query.filter_by(name='Basketball').first()
            swimming_sport = Sport.query.filter_by(name='Swimming').first()

            existing_section = Section.query.filter_by(name=name).first()
            if existing_section:
                return existing_section

            # Barnaul
            new_section = add_section_if_not_exists_barn('Football Section',
                                                         'Football is a team sport with a ball,'
                                                         ' where players strive to score a goal against an opponent.'
                                                         ' It includes two halves of 45 minutes each,'
                                                         ' and the game is played by 11 players on each side.',
                                                         barn_city,
                                                         football_sport,
                                                         get_parameters_barnaul("Football Section"))

            new_section2 = add_section_if_not_exists_barn('Tennis Section',
                                                          'Tennis is an individual or pair sport where players'
                                                          ' throw the ball over the net using rackets.'
                                                          ' The game consists of sets,'
                                                          'each of which is won by the first one'
                                                          ' to score a certain number of points (usually 6)',
                                                          barn_city,
                                                          tennis_sport,
                                                          get_parameters_barnaul('Tennis Section'))

            new_section3 = add_section_if_not_exists_barn('Basketball Section',
                                                          'The section invites everyone of any age and level of '
                                                          'training'
                                                          'Individual approach to each participant'
                                                          'Many years of coaching experience'
                                                          'A unique atmosphere for each player',
                                                          barn_city,
                                                          basket_sport,
                                                          get_parameters_barnaul('Basketball Section'))

            new_section4 = add_section_if_not_exists_barn('Swimming Section',
                                                          'The section is open to everyone who wants to improve their '
                                                          'swimming skills'
                                                          'Experienced coaches will help you master different '
                                                          'swimming styles'
                                                          'Group and individual lessons'
                                                          'Health, fitness and new achievements',
                                                          barn_city,
                                                          swimming_sport,
                                                          get_parameters_barnaul('Swimming Section'))

            for param in get_parameters_barnaul('Football Section'):
                new_section.parameters.append(
                    Parameter(name=param['name'], value=param['value'], category=param['category']))

            for param in get_parameters_barnaul('Tennis Section'):
                new_section2.parameters.append(
                    Parameter(name=param['name'], value=param['value'], category=param['category']))

            for param in get_parameters_barnaul('Basketball Section'):
                new_section3.parameters.append(
                    Parameter(name=param['name'], value=param['value'], category=param['category']))

            for param in get_parameters_barnaul('Swimming Section'):
                new_section4.parameters.append(
                    Parameter(name=param['name'], value=param['value'], category=param['category']))

            db.session.add_all([new_section, new_section2, new_section3, new_section4])
            db.session.commit()

            return new_section, new_section2, new_section3, new_section4


        def add_section_if_not_exists_chsk(name, description, city, sport, parameters):
            chsk_city = City.query.filter_by(name='Chelyabinsk').first()
            football_sport = Sport.query.filter_by(name='Football').first()
            tennis_sport = Sport.query.filter_by(name='Tennis').first()
            basket_sport = Sport.query.filter_by(name='Basketball').first()
            swimming_sport = Sport.query.filter_by(name='Swimming').first()
            cycling_sport = Sport.query.filter_by(name='Cycling').first()
            dancing_sport = Sport.query.filter_by(name='Dancing').first()

            existing_section = Section.query.filter_by(name=name).first()
            if existing_section:
                return existing_section

            # Chelyabinsk
            new_section = add_section_if_not_exists_chsk('Football Section',
                                                         'Football is a team sport with a ball,'
                                                         ' where players strive to score a goal against an opponent.'
                                                         ' It includes two halves of 45 minutes each,'
                                                         ' and the game is played by 11 players on each side.',
                                                         chsk_city,
                                                         football_sport,
                                                         get_parameters_chelyabinsk("Football Section"))

            new_section2 = add_section_if_not_exists_chsk('Tennis Section',
                                                          'Tennis is an individual or pair sport where players'
                                                          ' throw the ball over the net using rackets.'
                                                          ' The game consists of sets,'
                                                          'each of which is won by the first one'
                                                          ' to score a certain number of points (usually 6)',
                                                          chsk_city,
                                                          tennis_sport,
                                                          get_parameters_chelyabinsk('Tennis Section'))

            new_section3 = add_section_if_not_exists_chsk('Basketball Section',
                                                          'The section invites everyone of any age and level of '
                                                          'training'
                                                          'Individual approach to each participant'
                                                          'Many years of coaching experience'
                                                          'A unique atmosphere for each player',
                                                          chsk_city,
                                                          basket_sport,
                                                          get_parameters_chelyabinsk('Basketball Section'))

            new_section4 = add_section_if_not_exists_chsk('Swimming Section',
                                                          'The section is open to everyone who wants to improve their '
                                                          'swimming skills'
                                                          'Experienced coaches will help you master different '
                                                          'swimming styles'
                                                          'Group and individual lessons'
                                                          'Health, fitness and new achievements',
                                                          chsk_city,
                                                          swimming_sport,
                                                          get_parameters_chelyabinsk('Swimming Section'))

            new_section5 = add_section_if_not_exists_chsk('Cycling Section',
                                                          'The section invites cycling enthusiasts of any level of '
                                                          'training'
                                                          'Improving cycling skills'
                                                          'Group trips and competitions'
                                                          'Training on different types of trails'
                                                          'Exciting adventures',
                                                          chsk_city,
                                                          cycling_sport,
                                                          get_parameters_chelyabinsk('Cycling Section'))

            new_section6 = add_section_if_not_exists_chsk('Dancing Section',
                                                          'A wide range of dance styles for adults and children'
                                                          'Modern, classical and folk dances'
                                                          'Experienced teachers'
                                                          'Friendly and creative atmosphere'
                                                          'Unlocking potential and expressing emotions through movement',
                                                          chsk_city,
                                                          dancing_sport,
                                                          get_parameters_chelyabinsk('Dancing Section'))

            for param in get_parameters_chelyabinsk('Football Section'):
                new_section.parameters.append(
                    Parameter(name=param['name'], value=param['value'], category=param['category']))

            for param in get_parameters_chelyabinsk('Tennis Section'):
                new_section2.parameters.append(
                    Parameter(name=param['name'], value=param['value'], category=param['category']))

            for param in get_parameters_chelyabinsk('Basketball Section'):
                new_section3.parameters.append(
                    Parameter(name=param['name'], value=param['value'], category=param['category']))

            for param in get_parameters_chelyabinsk('Swimming Section'):
                new_section4.parameters.append(
                    Parameter(name=param['name'], value=param['value'], category=param['category']))

            for param in get_parameters_chelyabinsk('Cycling Section'):
                new_section5.parameters.append(
                    Parameter(name=param['name'], value=param['value'], category=param['category']))

            for param in get_parameters_chelyabinsk('Dancing Section'):
                new_section6.parameters.append(
                    Parameter(name=param['name'], value=param['value'], category=param['category']))

            db.session.add_all([new_section, new_section2, new_section3, new_section4, new_section5, new_section6])
            db.session.commit()

            return new_section, new_section2, new_section3, new_section4, new_section5, new_section6


        def add_section_if_not_exists_kazan(name, description, city, sport, parameters):
            kazan_city = City.query.filter_by(name='Kazan').first()
            football_sport = Sport.query.filter_by(name='Football').first()
            tennis_sport = Sport.query.filter_by(name='Tennis').first()
            basket_sport = Sport.query.filter_by(name='Basketball').first()
            swimming_sport = Sport.query.filter_by(name='Swimming').first()

            existing_section = Section.query.filter_by(name=name).first()
            if existing_section:
                return existing_section

            # Kazan
            new_section = add_section_if_not_exists_kazan('Football Section',
                                                          'Football is a team sport with a ball,'
                                                          ' where players strive to score a goal against an opponent.'
                                                          ' It includes two halves of 45 minutes each,'
                                                          ' and the game is played by 11 players on each side.',
                                                          kazan_city,
                                                          football_sport,
                                                          get_parameters_kazan("Football Section"))

            new_section2 = add_section_if_not_exists_kazan('Tennis Section',
                                                           'Tennis is an individual or pair sport where players'
                                                           ' throw the ball over the net using rackets.'
                                                           ' The game consists of sets,'
                                                           'each of which is won by the first one'
                                                           ' to score a certain number of points (usually 6)',
                                                           kazan_city,
                                                           tennis_sport,
                                                           get_parameters_kazan('Tennis Section'))

            new_section3 = add_section_if_not_exists_kazan('Basketball Section',
                                                           'The section invites everyone of any age and level of '
                                                           'training'
                                                           'Individual approach to each participant'
                                                           'Many years of coaching experience'
                                                           'A unique atmosphere for each player',
                                                           kazan_city,
                                                           basket_sport,
                                                           get_parameters_kazan('Basketball Section'))

            new_section4 = add_section_if_not_exists_kazan('Swimming Section',
                                                           'The section is open to everyone who wants to improve their '
                                                           'swimming skills'
                                                           'Experienced coaches will help you master different '
                                                           'swimming styles'
                                                           'Group and individual lessons'
                                                           'Health, fitness and new achievements',
                                                           kazan_city,
                                                           swimming_sport,
                                                           get_parameters_kazan('Swimming Section'))

            for param in get_parameters_kazan('Football Section'):
                new_section.parameters.append(
                    Parameter(name=param['name'], value=param['value'], category=param['category']))

            for param in get_parameters_kazan('Tennis Section'):
                new_section2.parameters.append(
                    Parameter(name=param['name'], value=param['value'], category=param['category']))

            for param in get_parameters_kazan('Basketball Section'):
                new_section3.parameters.append(
                    Parameter(name=param['name'], value=param['value'], category=param['category']))

            for param in get_parameters_kazan('Swimming Section'):
                new_section4.parameters.append(
                    Parameter(name=param['name'], value=param['value'], category=param['category']))

            db.session.add_all([new_section, new_section2, new_section3, new_section4])
            db.session.commit()

            return new_section, new_section2, new_section3, new_section4


        def add_section_if_not_exists_kemo(name, description, city, sport, parameters):
            kemerovo_city = City.query.filter_by(name='Kemerovo').first()
            football_sport = Sport.query.filter_by(name='Football').first()
            tennis_sport = Sport.query.filter_by(name='Tennis').first()
            basket_sport = Sport.query.filter_by(name='Basketball').first()
            swimming_sport = Sport.query.filter_by(name='Swimming').first()

            existing_section = Section.query.filter_by(name=name).first()
            if existing_section:
                return existing_section

            # Kemerovo
            new_section = add_section_if_not_exists_kemo('Football Section',
                                                         'Football is a team sport with a ball,'
                                                         ' where players strive to score a goal against an opponent.'
                                                         ' It includes two halves of 45 minutes each,'
                                                         ' and the game is played by 11 players on each side.',
                                                         kemerovo_city,
                                                         football_sport,
                                                         get_parameters_kemerovo("Football Section"))

            new_section2 = add_section_if_not_exists_kemo('Tennis Section',
                                                          'Tennis is an individual or pair sport where players'
                                                          ' throw the ball over the net using rackets.'
                                                          ' The game consists of sets,'
                                                          'each of which is won by the first one'
                                                          ' to score a certain number of points (usually 6)',
                                                          kemerovo_city,
                                                          tennis_sport,
                                                          get_parameters_kemerovo('Tennis Section'))

            new_section3 = add_section_if_not_exists_kemo('Basketball Section',
                                                          'The section invites everyone of any age and level of '
                                                          'training'
                                                          'Individual approach to each participant'
                                                          'Many years of coaching experience'
                                                          'A unique atmosphere for each player',
                                                          kemerovo_city,
                                                          basket_sport,
                                                          get_parameters_kemerovo('Basketball Section'))

            new_section4 = add_section_if_not_exists_kemo('Swimming Section',
                                                          'The section is open to everyone who wants to improve their '
                                                          'swimming skills'
                                                          'Experienced coaches will help you master different '
                                                          'swimming styles'
                                                          'Group and individual lessons'
                                                          'Health, fitness and new achievements',
                                                          kemerovo_city,
                                                          swimming_sport,
                                                          get_parameters_kemerovo('Swimming Section'))

            for param in get_parameters_kemerovo('Football Section'):
                new_section.parameters.append(
                    Parameter(name=param['name'], value=param['value'], category=param['category']))

            for param in get_parameters_kemerovo('Tennis Section'):
                new_section2.parameters.append(
                    Parameter(name=param['name'], value=param['value'], category=param['category']))

            for param in get_parameters_kemerovo('Basketball Section'):
                new_section3.parameters.append(
                    Parameter(name=param['name'], value=param['value'], category=param['category']))

            for param in get_parameters_kemerovo('Swimming Section'):
                new_section4.parameters.append(
                    Parameter(name=param['name'], value=param['value'], category=param['category']))

            db.session.add_all([new_section, new_section2, new_section3, new_section4])
            db.session.commit()

            return new_section, new_section2, new_section3, new_section4


        def add_section_if_not_exists_tomsk(name, description, city, sport, parameters):
            tomsk_city = City.query.filter_by(name='Kemerovo').first()
            football_sport = Sport.query.filter_by(name='Football').first()
            tennis_sport = Sport.query.filter_by(name='Tennis').first()
            volleyball_sport = Sport.query.filter_by(name='Volleyball').first()
            yoga_sport = Sport.query.filter_by(name='Yoga').first()

            existing_section = Section.query.filter_by(name=name).first()
            if existing_section:
                return existing_section

            # Tomsk
            new_section = add_section_if_not_exists_tomsk('Football Section',
                                                          'Football is a team sport with a ball,'
                                                          ' where players strive to score a goal against an opponent.'
                                                          ' It includes two halves of 45 minutes each,'
                                                          ' and the game is played by 11 players on each side.',
                                                          tomsk_city,
                                                          football_sport,
                                                          get_parameters_tsk("Football Section"))

            new_section2 = add_section_if_not_exists_tomsk('Tennis Section',
                                                           'Tennis is an individual or pair sport where players'
                                                           ' throw the ball over the net using rackets.'
                                                           ' The game consists of sets,'
                                                           'each of which is won by the first one'
                                                           ' to score a certain number of points (usually 6)',
                                                           tomsk_city,
                                                           tennis_sport,
                                                           get_parameters_tsk('Tennis Section'))

            new_section3 = add_section_if_not_exists_tomsk('Volleyball Section',
                                                           'Develop team spirit and physical fitness with us! '
                                                           'Volleyball training will help you improve coordination, '
                                                           'speed and impact strength. Everyone will find their dream '
                                                           'team here!',
                                                           tomsk_city,
                                                           volleyball_sport,
                                                           get_parameters_tsk('Basketball Section'))

            new_section4 = add_section_if_not_exists_tomsk('Yoga Section',
                                                           'Find a balance between body and spirit through yoga. Our '
                                                           'classes are aimed at developing flexibility, '
                                                           'strengthening muscles and reducing stress. Yoga will help '
                                                           'you find inner harmony and peace. Join us and start your '
                                                           'journey to self-improvement!',
                                                           tomsk_city,
                                                           yoga_sport,
                                                           get_parameters_tsk('Swimming Section'))

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

            return new_section, new_section2, new_section3, new_section4


        def add_section_if_not_exists_novosibirsk(name, description, city, sport, parameters):
            nsk_city = City.query.filter_by(name='Novosibirsk').first()
            football_sport = Sport.query.filter_by(name='Football').first()
            tennis_sport = Sport.query.filter_by(name='Tennis').first()
            volleyball_sport = Sport.query.filter_by(name='Volleyball').first()
            yoga_sport = Sport.query.filter_by(name='Yoga').first()
            basket_sport = Sport.query.filter_by(name='Basketball').first()
            swimming_sport = Sport.query.filter_by(name='Swimming').first()

            existing_section = Section.query.filter_by(name=name).first()
            if existing_section:
                return existing_section

            # Novosibirsk
            new_section = add_section_if_not_exists_novosibirsk('Football Section',
                                                                'Football is a team sport with a ball,'
                                                                'where players strive to score a goal against an '
                                                                'opponent.'
                                                                ' It includes two halves of 45 minutes each,'
                                                                ' and the game is played by 11 players on each side.',
                                                                nsk_city,
                                                                football_sport,
                                                                get_parameters_nsk("Football Section"))

            new_section2 = add_section_if_not_exists_novosibirsk('Tennis Section',
                                                                 'Tennis is an individual or pair sport where players'
                                                                 ' throw the ball over the net using rackets.'
                                                                 ' The game consists of sets,'
                                                                 'each of which is won by the first one'
                                                                 ' to score a certain number of points (usually 6)',
                                                                 nsk_city,
                                                                 tennis_sport,
                                                                 get_parameters_nsk('Tennis Section'))

            new_section3 = add_section_if_not_exists_novosibirsk('Volleyball Section',
                                                                 'Develop team spirit and physical fitness with us! '
                                                                 'Volleyball training will help you improve '
                                                                 'coordination,'
                                                                 'speed and impact strength. Everyone will find their '
                                                                 'dream'
                                                                 'team here!',
                                                                 nsk_city,
                                                                 volleyball_sport,
                                                                 get_parameters_nsk('Basketball Section'))

            new_section4 = add_section_if_not_exists_novosibirsk('Yoga Section',
                                                                 'Find a balance between body and spirit through '
                                                                 'yoga. Our'
                                                                 'classes are aimed at developing flexibility, '
                                                                 'strengthening muscles and reducing stress. Yoga '
                                                                 'will help'
                                                                 'you find inner harmony and peace. Join us and start '
                                                                 'your'
                                                                 'journey to self-improvement!',
                                                                 nsk_city,
                                                                 yoga_sport,
                                                                 get_parameters_nsk('Swimming Section'))

            new_section5 = add_section_if_not_exists_novosibirsk('Basketball Section',
                                                                 'The section invites everyone of any age and level of '
                                                                 'training'
                                                                 'Individual approach to each participant'
                                                                 'Many years of coaching experience'
                                                                 'A unique atmosphere for each player',
                                                                 nsk_city,
                                                                 basket_sport,
                                                                 get_parameters_nsk('Basketball Section'))

            new_section6 = add_section_if_not_exists_novosibirsk('Swimming Section',
                                                                 'The section is open to everyone who wants to '
                                                                 'improve their'
                                                                 'swimming skills'
                                                                 'Experienced coaches will help you master different '
                                                                 'swimming styles'
                                                                 'Group and individual lessons'
                                                                 'Health, fitness and new achievements',
                                                                 nsk_city,
                                                                 swimming_sport,
                                                                 get_parameters_nsk('Swimming Section'))

            for param in get_parameters_nsk('Football Section'):
                new_section.parameters.append(
                    Parameter(name=param['name'], value=param['value'], category=param['category']))

            for param in get_parameters_nsk('Tennis Section'):
                new_section2.parameters.append(
                    Parameter(name=param['name'], value=param['value'], category=param['category']))

            for param in get_parameters_nsk('Volleyball Section'):
                new_section3.parameters.append(
                    Parameter(name=param['name'], value=param['value'], category=param['category']))

            for param in get_parameters_nsk('Yoga Section'):
                new_section4.parameters.append(
                    Parameter(name=param['name'], value=param['value'], category=param['category']))

            for param in get_parameters_nsk('Basketball Section'):
                new_section5.parameters.append(
                    Parameter(name=param['name'], value=param['value'], category=param['category']))

            for param in get_parameters_nsk('Swimming Section'):
                new_section6.parameters.append(
                    Parameter(name=param['name'], value=param['value'], category=param['category']))

            db.session.add_all([new_section, new_section2, new_section3, new_section4, new_section5, new_section6])
            db.session.commit()

            return new_section, new_section2, new_section3, new_section4, new_section5, new_section6


        def add_section_if_not_exists_moscow(name, description, city, sport, parameters):
            msk_city = City.query.filter_by(name='Moscow').first()
            football_sport = Sport.query.filter_by(name='Football').first()
            tennis_sport = Sport.query.filter_by(name='Tennis').first()
            volleyball_sport = Sport.query.filter_by(name='Volleyball').first()
            yoga_sport = Sport.query.filter_by(name='Yoga').first()
            basket_sport = Sport.query.filter_by(name='Basketball').first()
            swimming_sport = Sport.query.filter_by(name='Swimming').first()
            running_sport = Sport.query.filter_by(name='Running').first()
            gymnastics_sport = Sport.query.filter_by(name='Gymnastics').first()
            cycling_sport = Sport.query.filter_by(name='Cycling').first()
            dancing_sport = Sport.query.filter_by(name='Dancing').first()

            existing_section = Section.query.filter_by(name=name).first()
            if existing_section:
                return existing_section

            # Moscow
            new_section = add_section_if_not_exists_moscow('Football Section',
                                                           'Football is a team sport with a ball,'
                                                           'where players strive to score a goal against an '
                                                           'opponent.'
                                                           ' It includes two halves of 45 minutes each,'
                                                           ' and the game is played by 11 players on each side.',
                                                           msk_city,
                                                           football_sport,
                                                           get_parameters_msc("Football Section"))

            new_section2 = add_section_if_not_exists_moscow('Tennis Section',
                                                            'Tennis is an individual or pair sport where players'
                                                            ' throw the ball over the net using rackets.'
                                                            ' The game consists of sets,'
                                                            'each of which is won by the first one'
                                                            ' to score a certain number of points (usually 6)',
                                                            msk_city,
                                                            tennis_sport,
                                                            get_parameters_msc('Tennis Section'))

            new_section3 = add_section_if_not_exists_moscow('Volleyball Section',
                                                            'Develop team spirit and physical fitness with us! '
                                                            'Volleyball training will help you improve '
                                                            'coordination,'
                                                            'speed and impact strength. Everyone will find their '
                                                            'dream'
                                                            'team here!',
                                                            msk_city,
                                                            volleyball_sport,
                                                            get_parameters_msc('Basketball Section'))

            new_section4 = add_section_if_not_exists_moscow('Yoga Section',
                                                            'Find a balance between body and spirit through '
                                                            'yoga. Our'
                                                            'classes are aimed at developing flexibility, '
                                                            'strengthening muscles and reducing stress. Yoga '
                                                            'will help'
                                                            'you find inner harmony and peace. Join us and start '
                                                            'your'
                                                            'journey to self-improvement!',
                                                            msk_city,
                                                            yoga_sport,
                                                            get_parameters_msc('Swimming Section'))

            new_section5 = add_section_if_not_exists_moscow('Basketball Section',
                                                            'The section invites everyone of any age and level of '
                                                            'training'
                                                            'Individual approach to each participant'
                                                            'Many years of coaching experience'
                                                            'A unique atmosphere for each player',
                                                            msk_city,
                                                            basket_sport,
                                                            get_parameters_msc('Basketball Section'))

            new_section6 = add_section_if_not_exists_moscow('Swimming Section',
                                                            'The section is open to everyone who wants to '
                                                            'improve their'
                                                            'swimming skills'
                                                            'Experienced coaches will help you master different '
                                                            'swimming styles'
                                                            'Group and individual lessons'
                                                            'Health, fitness and new achievements',
                                                            msk_city,
                                                            swimming_sport,
                                                            get_parameters_msc('Swimming Section'))

            new_section7 = add_section_if_not_exists_moscow('Running Section',
                                                            'A section for improving physical fitness and '
                                                            'running technique, with individual plans and '
                                                            'competitions.',
                                                            msk_city,
                                                            running_sport,
                                                            get_parameters_msc('Running Section'))

            new_section8 = add_section_if_not_exists_moscow('Gymnastics Section',
                                                            'The development of flexibility, strength and '
                                                            'coordination through working with various '
                                                            'projectiles. Suitable for children and adults',
                                                            msk_city,
                                                            gymnastics_sport,
                                                            get_parameters_msc('Gymnastics Section'))

            new_section9 = add_section_if_not_exists_moscow('Cycling Section',
                                                            'Training in riding skills, bike maintenance and '
                                                            'participation in competitions. Group and individual '
                                                            'training sessions.',
                                                            msk_city,
                                                            cycling_sport,
                                                            get_parameters_msc('Cycling Section'))

            new_section10 = add_section_if_not_exists_moscow('Dancing Section',
                                                             'A variety of styles, from classical to modern. '
                                                             'Improving plasticity and a sense of rhythm, '
                                                             'getting to know culture through dance.',
                                                             msk_city,
                                                             dancing_sport,
                                                             get_parameters_msc('Dancing Section'))

            for param in get_parameters_msc('Football Section'):
                new_section.parameters.append(
                    Parameter(name=param['name'], value=param['value'], category=param['category']))

            for param in get_parameters_msc('Tennis Section'):
                new_section2.parameters.append(
                    Parameter(name=param['name'], value=param['value'], category=param['category']))

            for param in get_parameters_msc('Volleyball Section'):
                new_section3.parameters.append(
                    Parameter(name=param['name'], value=param['value'], category=param['category']))

            for param in get_parameters_msc('Yoga Section'):
                new_section4.parameters.append(
                    Parameter(name=param['name'], value=param['value'], category=param['category']))

            for param in get_parameters_msc('Basketball Section'):
                new_section5.parameters.append(
                    Parameter(name=param['name'], value=param['value'], category=param['category']))

            for param in get_parameters_msc('Swimming Section'):
                new_section6.parameters.append(
                    Parameter(name=param['name'], value=param['value'], category=param['category']))

            for param in get_parameters_msc('Running Section'):
                new_section7.parameters.append(
                    Parameter(name=param['name'], value=param['value'], category=param['category']))

            for param in get_parameters_msc('Gymnastics Section'):
                new_section8.parameters.append(
                    Parameter(name=param['name'], value=param['value'], category=param['category']))

            for param in get_parameters_msc('Cycling Section'):
                new_section9.parameters.append(
                    Parameter(name=param['name'], value=param['value'], category=param['category']))

            for param in get_parameters_msc('Dancing Section'):
                new_section10.parameters.append(
                    Parameter(name=param['name'], value=param['value'], category=param['category']))

            db.session.add_all([new_section, new_section2, new_section3, new_section4, new_section5, new_section6,
                                new_section7, new_section8, new_section9, new_section10])
            db.session.commit()

            return new_section, new_section2, new_section3, new_section4, new_section5, new_section6, new_section7, new_section8, new_section9, new_section10


        def add_section_if_not_exists_saint_petersburg(name, description, city, sport, parameters):
            stp_city = City.query.filter_by(name='Saint Petersburg').first()
            football_sport = Sport.query.filter_by(name='Football').first()
            tennis_sport = Sport.query.filter_by(name='Tennis').first()
            volleyball_sport = Sport.query.filter_by(name='Volleyball').first()
            yoga_sport = Sport.query.filter_by(name='Yoga').first()
            basket_sport = Sport.query.filter_by(name='Basketball').first()
            swimming_sport = Sport.query.filter_by(name='Swimming').first()
            running_sport = Sport.query.filter_by(name='Running').first()
            gymnastics_sport = Sport.query.filter_by(name='Gymnastics').first()
            cycling_sport = Sport.query.filter_by(name='Cycling').first()
            dancing_sport = Sport.query.filter_by(name='Dancing').first()

            existing_section = Section.query.filter_by(name=name).first()
            if existing_section:
                return existing_section

            # Saint Petersburg
            new_section = add_section_if_not_exists_saint_petersburg('Football Section',
                                                                     'Football is a team sport with a ball,'
                                                                     'where players strive to score a goal against an '
                                                                     'opponent.'
                                                                     ' It includes two halves of 45 minutes each,'
                                                                     ' and the game is played by 11 players on each side.',
                                                                     stp_city,
                                                                     football_sport,
                                                                     get_parameters_stp("Football Section"))

            new_section2 = add_section_if_not_exists_saint_petersburg('Tennis Section',
                                                                      'Tennis is an individual or pair sport where '
                                                                      'players'
                                                                      ' throw the ball over the net using rackets.'
                                                                      ' The game consists of sets,'
                                                                      'each of which is won by the first one'
                                                                      ' to score a certain number of points (usually 6)',
                                                                      stp_city,
                                                                      tennis_sport,
                                                                      get_parameters_stp('Tennis Section'))

            new_section3 = add_section_if_not_exists_saint_petersburg('Volleyball Section',
                                                                      'Develop team spirit and physical fitness with us! '
                                                                      'Volleyball training will help you improve '
                                                                      'coordination,'
                                                                      'speed and impact strength. Everyone will find their '
                                                                      'dream'
                                                                      'team here!',
                                                                      stp_city,
                                                                      volleyball_sport,
                                                                      get_parameters_stp('Basketball Section'))

            new_section4 = add_section_if_not_exists_saint_petersburg('Yoga Section',
                                                                      'Find a balance between body and spirit through '
                                                                      'yoga. Our'
                                                                      'classes are aimed at developing flexibility, '
                                                                      'strengthening muscles and reducing stress. Yoga '
                                                                      'will help'
                                                                      'you find inner harmony and peace. Join us and start '
                                                                      'your'
                                                                      'journey to self-improvement!',
                                                                      stp_city,
                                                                      yoga_sport,
                                                                      get_parameters_stp('Swimming Section'))

            new_section5 = add_section_if_not_exists_saint_petersburg('Basketball Section',
                                                                      'The section invites everyone of any age and level of '
                                                                      'training'
                                                                      'Individual approach to each participant'
                                                                      'Many years of coaching experience'
                                                                      'A unique atmosphere for each player',
                                                                      stp_city,
                                                                      basket_sport,
                                                                      get_parameters_stp('Basketball Section'))

            new_section6 = add_section_if_not_exists_saint_petersburg('Swimming Section',
                                                                      'The section is open to everyone who wants to '
                                                                      'improve their'
                                                                      'swimming skills'
                                                                      'Experienced coaches will help you master different '
                                                                      'swimming styles'
                                                                      'Group and individual lessons'
                                                                      'Health, fitness and new achievements',
                                                                      stp_city,
                                                                      swimming_sport,
                                                                      get_parameters_stp('Swimming Section'))

            new_section7 = add_section_if_not_exists_saint_petersburg('Running Section',
                                                                      'A section for improving physical fitness and '
                                                                      'running technique, with individual plans and '
                                                                      'competitions.',
                                                                      stp_city,
                                                                      running_sport,
                                                                      get_parameters_stp('Running Section'))

            new_section8 = add_section_if_not_exists_saint_petersburg('Gymnastics Section',
                                                                      'The development of flexibility, strength and '
                                                                      'coordination through working with various '
                                                                      'projectiles. Suitable for children and adults',
                                                                      stp_city,
                                                                      gymnastics_sport,
                                                                      get_parameters_stp('Gymnastics Section'))

            new_section9 = add_section_if_not_exists_saint_petersburg('Cycling Section',
                                                                      'Training in riding skills, bike maintenance and '
                                                                      'participation in competitions. Group and individual '
                                                                      'training sessions.',
                                                                      stp_city,
                                                                      cycling_sport,
                                                                      get_parameters_stp('Cycling Section'))

            new_section10 = add_section_if_not_exists_saint_petersburg('Dancing Section',
                                                                       'A variety of styles, from classical to modern. '
                                                                       'Improving plasticity and a sense of rhythm, '
                                                                       'getting to know culture through dance.',
                                                                       stp_city,
                                                                       dancing_sport,
                                                                       get_parameters_stp('Dancing Section'))

            for param in get_parameters_stp('Football Section'):
                new_section.parameters.append(
                    Parameter(name=param['name'], value=param['value'], category=param['category']))

            for param in get_parameters_stp('Tennis Section'):
                new_section2.parameters.append(
                    Parameter(name=param['name'], value=param['value'], category=param['category']))

            for param in get_parameters_stp('Volleyball Section'):
                new_section3.parameters.append(
                    Parameter(name=param['name'], value=param['value'], category=param['category']))

            for param in get_parameters_stp('Yoga Section'):
                new_section4.parameters.append(
                    Parameter(name=param['name'], value=param['value'], category=param['category']))

            for param in get_parameters_stp('Basketball Section'):
                new_section5.parameters.append(
                    Parameter(name=param['name'], value=param['value'], category=param['category']))

            for param in get_parameters_stp('Swimming Section'):
                new_section6.parameters.append(
                    Parameter(name=param['name'], value=param['value'], category=param['category']))

            for param in get_parameters_stp('Running Section'):
                new_section7.parameters.append(
                    Parameter(name=param['name'], value=param['value'], category=param['category']))

            for param in get_parameters_stp('Gymnastics Section'):
                new_section8.parameters.append(
                    Parameter(name=param['name'], value=param['value'], category=param['category']))

            for param in get_parameters_stp('Cycling Section'):
                new_section9.parameters.append(
                    Parameter(name=param['name'], value=param['value'], category=param['category']))

            for param in get_parameters_stp('Dancing Section'):
                new_section10.parameters.append(
                    Parameter(name=param['name'], value=param['value'], category=param['category']))

            db.session.add_all([new_section, new_section2, new_section3, new_section4, new_section5, new_section6,
                                new_section7, new_section8, new_section9, new_section10])
            db.session.commit()

            return new_section, new_section2, new_section3, new_section4, new_section5, new_section6, new_section7, new_section8, new_section9, new_section10


        def add_section_if_not_exists_ekaterinburg(name, description, city, sport, parameters):
            ekb_city = City.query.filter_by(name='Saint Petersburg').first()
            football_sport = Sport.query.filter_by(name='Football').first()
            tennis_sport = Sport.query.filter_by(name='Tennis').first()
            volleyball_sport = Sport.query.filter_by(name='Volleyball').first()
            yoga_sport = Sport.query.filter_by(name='Yoga').first()
            basket_sport = Sport.query.filter_by(name='Basketball').first()
            swimming_sport = Sport.query.filter_by(name='Swimming').first()
            running_sport = Sport.query.filter_by(name='Running').first()
            gymnastics_sport = Sport.query.filter_by(name='Gymnastics').first()
            cycling_sport = Sport.query.filter_by(name='Cycling').first()
            dancing_sport = Sport.query.filter_by(name='Dancing').first()

            existing_section = Section.query.filter_by(name=name).first()
            if existing_section:
                return existing_section

            # Saint Petersburg
            new_section = add_section_if_not_exists_ekaterinburg('Football Section',
                                                                 'Football is a team sport with a ball,'
                                                                 'where players strive to score a goal against an '
                                                                 'opponent.'
                                                                 ' It includes two halves of 45 minutes each,'
                                                                 ' and the game is played by 11 players on each side.',
                                                                 ekb_city,
                                                                 football_sport,
                                                                 get_parameters_ekb("Football Section"))

            new_section2 = add_section_if_not_exists_ekaterinburg('Tennis Section',
                                                                  'Tennis is an individual or pair sport where '
                                                                  'players'
                                                                  ' throw the ball over the net using rackets.'
                                                                  ' The game consists of sets,'
                                                                  'each of which is won by the first one'
                                                                  ' to score a certain number of points (usually 6)',
                                                                  ekb_city,
                                                                  tennis_sport,
                                                                  get_parameters_ekb('Tennis Section'))

            new_section3 = add_section_if_not_exists_ekaterinburg('Volleyball Section',
                                                                  'Develop team spirit and physical fitness with us! '
                                                                  'Volleyball training will help you improve '
                                                                  'coordination,'
                                                                  'speed and impact strength. Everyone will find their '
                                                                  'dream'
                                                                  'team here!',
                                                                  ekb_city,
                                                                  volleyball_sport,
                                                                  get_parameters_ekb('Basketball Section'))

            new_section4 = add_section_if_not_exists_ekaterinburg('Yoga Section',
                                                                  'Find a balance between body and spirit through '
                                                                  'yoga. Our'
                                                                  'classes are aimed at developing flexibility, '
                                                                  'strengthening muscles and reducing stress. Yoga '
                                                                  'will help'
                                                                  'you find inner harmony and peace. Join us and start '
                                                                  'your'
                                                                  'journey to self-improvement!',
                                                                  ekb_city,
                                                                  yoga_sport,
                                                                  get_parameters_ekb('Swimming Section'))

            new_section5 = add_section_if_not_exists_ekaterinburg('Basketball Section',
                                                                  'The section invites everyone of any age and level of '
                                                                  'training'
                                                                  'Individual approach to each participant'
                                                                  'Many years of coaching experience'
                                                                  'A unique atmosphere for each player',
                                                                  ekb_city,
                                                                  basket_sport,
                                                                  get_parameters_ekb('Basketball Section'))

            new_section6 = add_section_if_not_exists_ekaterinburg('Swimming Section',
                                                                  'The section is open to everyone who wants to '
                                                                  'improve their'
                                                                  'swimming skills'
                                                                  'Experienced coaches will help you master different '
                                                                  'swimming styles'
                                                                  'Group and individual lessons'
                                                                  'Health, fitness and new achievements',
                                                                  ekb_city,
                                                                  swimming_sport,
                                                                  get_parameters_ekb('Swimming Section'))

            new_section7 = add_section_if_not_exists_ekaterinburg('Running Section',
                                                                  'A section for improving physical fitness and '
                                                                  'running technique, with individual plans and '
                                                                  'competitions.',
                                                                  ekb_city,
                                                                  running_sport,
                                                                  get_parameters_ekb('Running Section'))

            new_section8 = add_section_if_not_exists_ekaterinburg('Gymnastics Section',
                                                                  'The development of flexibility, strength and '
                                                                  'coordination through working with various '
                                                                  'projectiles. Suitable for children and adults',
                                                                  ekb_city,
                                                                  gymnastics_sport,
                                                                  get_parameters_ekb('Gymnastics Section'))

            new_section9 = add_section_if_not_exists_ekaterinburg('Cycling Section',
                                                                  'Training in riding skills, bike maintenance and '
                                                                  'participation in competitions. Group and individual '
                                                                  'training sessions.',
                                                                  ekb_city,
                                                                  cycling_sport,
                                                                  get_parameters_ekb('Cycling Section'))

            new_section10 = add_section_if_not_exists_ekaterinburg('Dancing Section',
                                                                   'A variety of styles, from classical to modern. '
                                                                   'Improving plasticity and a sense of rhythm, '
                                                                   'getting to know culture through dance.',
                                                                   ekb_city,
                                                                   dancing_sport,
                                                                   get_parameters_ekb('Dancing Section'))

            for param in get_parameters_ekb('Football Section'):
                new_section.parameters.append(
                    Parameter(name=param['name'], value=param['value'], category=param['category']))

            for param in get_parameters_ekb('Tennis Section'):
                new_section2.parameters.append(
                    Parameter(name=param['name'], value=param['value'], category=param['category']))

            for param in get_parameters_ekb('Volleyball Section'):
                new_section3.parameters.append(
                    Parameter(name=param['name'], value=param['value'], category=param['category']))

            for param in get_parameters_ekb('Yoga Section'):
                new_section4.parameters.append(
                    Parameter(name=param['name'], value=param['value'], category=param['category']))

            for param in get_parameters_ekb('Basketball Section'):
                new_section5.parameters.append(
                    Parameter(name=param['name'], value=param['value'], category=param['category']))

            for param in get_parameters_ekb('Swimming Section'):
                new_section6.parameters.append(
                    Parameter(name=param['name'], value=param['value'], category=param['category']))

            for param in get_parameters_ekb('Running Section'):
                new_section7.parameters.append(
                    Parameter(name=param['name'], value=param['value'], category=param['category']))

            for param in get_parameters_ekb('Gymnastics Section'):
                new_section8.parameters.append(
                    Parameter(name=param['name'], value=param['value'], category=param['category']))

            for param in get_parameters_ekb('Cycling Section'):
                new_section9.parameters.append(
                    Parameter(name=param['name'], value=param['value'], category=param['category']))

            for param in get_parameters_ekb('Dancing Section'):
                new_section10.parameters.append(
                    Parameter(name=param['name'], value=param['value'], category=param['category']))

            db.session.add_all([new_section, new_section2, new_section3, new_section4, new_section5, new_section6,
                                new_section7, new_section8, new_section9, new_section10])
            db.session.commit()

            return new_section, new_section2, new_section3, new_section4, new_section5, new_section6, new_section7, new_section8, new_section9, new_section10


        class SearchForm(FlaskForm):
            city = SelectField('City', coerce=int,
                               choices=[(city.id, city.name) for city in City.query.order_by('name')])

            sport = SelectField('Sport', coerce=int,
                                choices=[(sport.id, sport.name) for sport in Sport.query.order_by('name')])

            physical_fitness = SelectField('Physical Fitness', coerce=str,
                                           choices=[("Средняя подготовка", "Средняя подготовка"),
                                                    ("Максимальная подготовка", "Максимальная подготовка"),
                                                    ("Минимальная подготовка", "Минимальная подготовка")])

            schedule = SelectField('Schedule', coerce=str, choices=[("8:00-12:00", "8:00-12:00"),
                                                                    ("12:00-16:00", "12:00-16:00"),
                                                                    ("16:00-20:00", "16:00-20:00")])

            location = SelectField('Location', coerce=str, choices=[("Парк", "Парк"), ("Бассейн", "Бассейн"),
                                                                    ("Крытый стадитон", "Крытый стадитон")])

            cost = SelectField('Cost', coerce=str,
                               choices=[("2500руб", "2500руб"), ("3500руб", "3500руб"), ("4500руб", "4500руб")])

            coach_reputation = SelectField('Coach Reputation', coerce=str,
                                           choices=[("5", "5"), ("4.5", "4.5"), ("4.3", "4.3")])

            atmosphere = SelectField('Atmosphere', coerce=str, choices=[("Дружелюбная", "Дружелюбная"),
                                                                        ("Не дружелюбная", "Не дружелюбная")])

            club_achievements = SelectField('Club Achievements', coerce=str,
                                            choices=[("Есть", "Есть"), ("Нету", "Нету")])

            development_opportunities = SelectField('Development Opportunities', coerce=str,
                                                    choices=[("Да", "Да"), ("Нет", "Нет")])

    app.run(debug=True)
