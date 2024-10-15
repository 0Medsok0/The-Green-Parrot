# parameters.py

# UFA
def get_parameters(section_name):
    if section_name == 'Dancing Section':
        return [
            {'name': 'Physical Fitness', 'value': 'Максимальная подготовка', 'category': 'Physical Fitness'},
            {'name': 'Schedule', 'value': '8:00-12:00', 'category': 'Schedule'},
            {'name': 'Location', 'value': 'Бассейн', 'category': 'Location'},
            {'name': 'Cost', 'value': '2500руб', 'category': 'Cost'},
            {'name': 'Coach Reputation', 'value': '5', 'category': 'Coach Reputation'},
            {'name': 'Atmosphere', 'value': 'Дружелюбная', 'category': 'Atmosphere'},
            {'name': 'Club Achievements', 'value': 'Есть', 'category': 'Club Achievements'},
            {'name': 'Development Opportunities', 'value': 'Да', 'category': 'Development Opportunities'},
        ]
    elif section_name == 'Dancing Section 2':
        return [
            {'name': 'Physical Fitness', 'value': 'Средняя подготовка', 'category': 'Physical Fitness'},
            {'name': 'Schedule', 'value': '12:00-16:00', 'category': 'Schedule'},
            {'name': 'Location', 'value': 'Парк', 'category': 'Location'},
            {'name': 'Cost', 'value': '3500руб', 'category': 'Cost'},
            {'name': 'Coach Reputation', 'value': '5', 'category': 'Coach Reputation'},
            {'name': 'Atmosphere', 'value': 'Дружелюбная', 'category': 'Atmosphere'},
            {'name': 'Club Achievements', 'value': 'Есть', 'category': 'Club Achievements'},
            {'name': 'Development Opportunities', 'value': 'Да', 'category': 'Development Opportunities'},
        ]
    elif section_name == 'Basketball Section':
        return [
            {'name': 'Physical Fitness', 'value': 'Средняя подготовка', 'category': 'Physical Fitness'},
            {'name': 'Schedule', 'value': '12:00-16:00', 'category': 'Schedule'},
            {'name': 'Location', 'value': 'Парк', 'category': 'Location'},
            {'name': 'Cost', 'value': '3500руб', 'category': 'Cost'},
            {'name': 'Coach Reputation', 'value': '5', 'category': 'Coach Reputation'},
            {'name': 'Atmosphere', 'value': 'Дружелюбная', 'category': 'Atmosphere'},
            {'name': 'Club Achievements', 'value': 'Есть', 'category': 'Club Achievements'},
            {'name': 'Development Opportunities', 'value': 'Да', 'category': 'Development Opportunities'},
        ]
    elif section_name == 'Swimming Section':
        return [
            {'name': 'Physical Fitness', 'value': 'Максимальная подготовка', 'category': 'Physical Fitness'},
            {'name': 'Schedule', 'value': '8:00-12:00', 'category': 'Schedule'},
            {'name': 'Location', 'value': 'Бассейн', 'category': 'Location'},
            {'name': 'Cost', 'value': '4500руб', 'category': 'Cost'},
            {'name': 'Coach Reputation', 'value': '5', 'category': 'Coach Reputation'},
            {'name': 'Atmosphere', 'value': 'Дружелюбная', 'category': 'Atmosphere'},
            {'name': 'Club Achievements', 'value': 'Есть', 'category': 'Club Achievements'},
            {'name': 'Development Opportunities', 'value': 'Да', 'category': 'Development Opportunities'},
        ]
    else:
        return []


# Barnaul
def get_parameters_barnaul(section_name):
    if section_name == 'Football Section':
        return [
            {'name': 'Physical Fitness', 'value': 'Максимальная подготовка', 'category': 'Physical Fitness'},
            {'name': 'Schedule', 'value': '8:00-12:00', 'category': 'Schedule'},
            {'name': 'Location', 'value': 'Парк', 'category': 'Location'},
            {'name': 'Cost', 'value': '2500руб', 'category': 'Cost'},
            {'name': 'Coach Reputation', 'value': '5', 'category': 'Coach Reputation'},
            {'name': 'Atmosphere', 'value': 'Дружелюбная', 'category': 'Atmosphere'},
            {'name': 'Club Achievements', 'value': 'Есть', 'category': 'Club Achievements'},
            {'name': 'Development Opportunities', 'value': 'Да', 'category': 'Development Opportunities'},
        ]
    elif section_name == 'Tennis Section':
        return [
            {'name': 'Physical Fitness', 'value': 'Средняя подготовка', 'category': 'Physical Fitness'},
            {'name': 'Schedule', 'value': '12:00-16:00', 'category': 'Schedule'},
            {'name': 'Location', 'value': 'Парк', 'category': 'Location'},
            {'name': 'Cost', 'value': '3500руб', 'category': 'Cost'},
            {'name': 'Coach Reputation', 'value': '5', 'category': 'Coach Reputation'},
            {'name': 'Atmosphere', 'value': 'Дружелюбная', 'category': 'Atmosphere'},
            {'name': 'Club Achievements', 'value': 'Есть', 'category': 'Club Achievements'},
            {'name': 'Development Opportunities', 'value': 'Да', 'category': 'Development Opportunities'},
        ]
    elif section_name == 'Basketball Section':
        return [
            {'name': 'Physical Fitness', 'value': 'Средняя подготовка', 'category': 'Physical Fitness'},
            {'name': 'Schedule', 'value': '12:00-16:00', 'category': 'Schedule'},
            {'name': 'Location', 'value': 'Парк', 'category': 'Location'},
            {'name': 'Cost', 'value': '3500руб', 'category': 'Cost'},
            {'name': 'Coach Reputation', 'value': '5', 'category': 'Coach Reputation'},
            {'name': 'Atmosphere', 'value': 'Дружелюбная', 'category': 'Atmosphere'},
            {'name': 'Club Achievements', 'value': 'Есть', 'category': 'Club Achievements'},
            {'name': 'Development Opportunities', 'value': 'Да', 'category': 'Development Opportunities'},
        ]
    elif section_name == 'Swimming Section':
        return [
            {'name': 'Physical Fitness', 'value': 'Максимальная подготовка', 'category': 'Physical Fitness'},
            {'name': 'Schedule', 'value': '8:00-12:00', 'category': 'Schedule'},
            {'name': 'Location', 'value': 'Бассейн', 'category': 'Location'},
            {'name': 'Cost', 'value': '4500руб', 'category': 'Cost'},
            {'name': 'Coach Reputation', 'value': '5', 'category': 'Coach Reputation'},
            {'name': 'Atmosphere', 'value': 'Дружелюбная', 'category': 'Atmosphere'},
            {'name': 'Club Achievements', 'value': 'Есть', 'category': 'Club Achievements'},
            {'name': 'Development Opportunities', 'value': 'Да', 'category': 'Development Opportunities'},
        ]
    else:
        return []


# Chelyabinsk
def get_parameters_chelyabinsk(section_name):
    if section_name == 'Football Section':
        return [
            {'name': 'Physical Fitness', 'value': 'Максимальная подготовка', 'category': 'Physical Fitness'},
            {'name': 'Schedule', 'value': '8:00-12:00', 'category': 'Schedule'},
            {'name': 'Location', 'value': 'Парк', 'category': 'Location'},
            {'name': 'Cost', 'value': '2500руб', 'category': 'Cost'},
            {'name': 'Coach Reputation', 'value': '5', 'category': 'Coach Reputation'},
            {'name': 'Atmosphere', 'value': 'Дружелюбная', 'category': 'Atmosphere'},
            {'name': 'Club Achievements', 'value': 'Есть', 'category': 'Club Achievements'},
            {'name': 'Development Opportunities', 'value': 'Да', 'category': 'Development Opportunities'},
        ]
    elif section_name == 'Tennis Section':
        return [
            {'name': 'Physical Fitness', 'value': 'Средняя подготовка', 'category': 'Physical Fitness'},
            {'name': 'Schedule', 'value': '12:00-16:00', 'category': 'Schedule'},
            {'name': 'Location', 'value': 'Парк', 'category': 'Location'},
            {'name': 'Cost', 'value': '4500руб', 'category': 'Cost'},
            {'name': 'Coach Reputation', 'value': '5', 'category': 'Coach Reputation'},
            {'name': 'Atmosphere', 'value': 'Дружелюбная', 'category': 'Atmosphere'},
            {'name': 'Club Achievements', 'value': 'Есть', 'category': 'Club Achievements'},
            {'name': 'Development Opportunities', 'value': 'Да', 'category': 'Development Opportunities'},
        ]
    elif section_name == 'Basketball Section':
        return [
            {'name': 'Physical Fitness', 'value': 'Средняя подготовка', 'category': 'Physical Fitness'},
            {'name': 'Schedule', 'value': '12:00-16:00', 'category': 'Schedule'},
            {'name': 'Location', 'value': 'Крытый стадитон', 'category': 'Location'},
            {'name': 'Cost', 'value': '3500руб', 'category': 'Cost'},
            {'name': 'Coach Reputation', 'value': '5', 'category': 'Coach Reputation'},
            {'name': 'Atmosphere', 'value': 'Дружелюбная', 'category': 'Atmosphere'},
            {'name': 'Club Achievements', 'value': 'Есть', 'category': 'Club Achievements'},
            {'name': 'Development Opportunities', 'value': 'Да', 'category': 'Development Opportunities'},
        ]
    elif section_name == 'Swimming Section':
        return [
            {'name': 'Physical Fitness', 'value': 'Максимальная подготовка', 'category': 'Physical Fitness'},
            {'name': 'Schedule', 'value': '8:00-12:00', 'category': 'Schedule'},
            {'name': 'Location', 'value': 'Бассейн', 'category': 'Location'},
            {'name': 'Cost', 'value': '4500руб', 'category': 'Cost'},
            {'name': 'Coach Reputation', 'value': '5', 'category': 'Coach Reputation'},
            {'name': 'Atmosphere', 'value': 'Дружелюбная', 'category': 'Atmosphere'},
            {'name': 'Club Achievements', 'value': 'Есть', 'category': 'Club Achievements'},
            {'name': 'Development Opportunities', 'value': 'Да', 'category': 'Development Opportunities'},
        ]
    elif section_name == 'Cycling Section':
        return [
            {'name': 'Physical Fitness', 'value': 'Максимальная подготовка', 'category': 'Physical Fitness'},
            {'name': 'Schedule', 'value': '12:00-16:00', 'category': 'Schedule'},
            {'name': 'Location', 'value': 'Крытый стадитон', 'category': 'Location'},
            {'name': 'Cost', 'value': '2500руб', 'category': 'Cost'},
            {'name': 'Coach Reputation', 'value': '4.3', 'category': 'Coach Reputation'},
            {'name': 'Atmosphere', 'value': 'Дружелюбная', 'category': 'Atmosphere'},
            {'name': 'Club Achievements', 'value': 'Есть', 'category': 'Club Achievements'},
            {'name': 'Development Opportunities', 'value': 'Да', 'category': 'Development Opportunities'},
        ]
    elif section_name == 'Dancing Section':
        return [
            {'name': 'Physical Fitness', 'value': 'Максимальная подготовка', 'category': 'Physical Fitness'},
            {'name': 'Schedule', 'value': '8:00-12:00', 'category': 'Schedule'},
            {'name': 'Location', 'value': 'Крытый стадитон', 'category': 'Location'},
            {'name': 'Cost', 'value': '3500руб', 'category': 'Cost'},
            {'name': 'Coach Reputation', 'value': '4.3', 'category': 'Coach Reputation'},
            {'name': 'Atmosphere', 'value': 'Дружелюбная', 'category': 'Atmosphere'},
            {'name': 'Club Achievements', 'value': 'Есть', 'category': 'Club Achievements'},
            {'name': 'Development Opportunities', 'value': 'Да', 'category': 'Development Opportunities'},
        ]
    else:
        return []


# Kazan
def get_parameters_kazan(section_name):
    if section_name == 'Football Section':
        return [
            {'name': 'Physical Fitness', 'value': 'Максимальная подготовка', 'category': 'Physical Fitness'},
            {'name': 'Schedule', 'value': '8:00-12:00', 'category': 'Schedule'},
            {'name': 'Location', 'value': 'Парк', 'category': 'Location'},
            {'name': 'Cost', 'value': '3500руб', 'category': 'Cost'},
            {'name': 'Coach Reputation', 'value': '4.5', 'category': 'Coach Reputation'},
            {'name': 'Atmosphere', 'value': 'Дружелюбная', 'category': 'Atmosphere'},
            {'name': 'Club Achievements', 'value': 'Есть', 'category': 'Club Achievements'},
            {'name': 'Development Opportunities', 'value': 'Да', 'category': 'Development Opportunities'},
        ]
    elif section_name == 'Tennis Section':
        return [
            {'name': 'Physical Fitness', 'value': 'Максимальная подготовка', 'category': 'Physical Fitness'},
            {'name': 'Schedule', 'value': '12:00-16:00', 'category': 'Schedule'},
            {'name': 'Location', 'value': 'Крытый стадитон', 'category': 'Location'},
            {'name': 'Cost', 'value': '3500руб', 'category': 'Cost'},
            {'name': 'Coach Reputation', 'value': '4.5', 'category': 'Coach Reputation'},
            {'name': 'Atmosphere', 'value': 'Дружелюбная', 'category': 'Atmosphere'},
            {'name': 'Club Achievements', 'value': 'Есть', 'category': 'Club Achievements'},
            {'name': 'Development Opportunities', 'value': 'Да', 'category': 'Development Opportunities'},
        ]
    elif section_name == 'Basketball Section':
        return [
            {'name': 'Physical Fitness', 'value': 'Средняя подготовка', 'category': 'Physical Fitness'},
            {'name': 'Schedule', 'value': '12:00-16:00', 'category': 'Schedule'},
            {'name': 'Location', 'value': 'Крытый стадитон', 'category': 'Location'},
            {'name': 'Cost', 'value': '3500руб', 'category': 'Cost'},
            {'name': 'Coach Reputation', 'value': '5', 'category': 'Coach Reputation'},
            {'name': 'Atmosphere', 'value': 'Дружелюбная', 'category': 'Atmosphere'},
            {'name': 'Club Achievements', 'value': 'Есть', 'category': 'Club Achievements'},
            {'name': 'Development Opportunities', 'value': 'Да', 'category': 'Development Opportunities'},
        ]
    elif section_name == 'Swimming Section':
        return [
            {'name': 'Physical Fitness', 'value': 'Максимальная подготовка', 'category': 'Physical Fitness'},
            {'name': 'Schedule', 'value': '8:00-12:00', 'category': 'Schedule'},
            {'name': 'Location', 'value': 'Бассейн', 'category': 'Location'},
            {'name': 'Cost', 'value': '4500руб', 'category': 'Cost'},
            {'name': 'Coach Reputation', 'value': '5', 'category': 'Coach Reputation'},
            {'name': 'Atmosphere', 'value': 'Дружелюбная', 'category': 'Atmosphere'},
            {'name': 'Club Achievements', 'value': 'Есть', 'category': 'Club Achievements'},
            {'name': 'Development Opportunities', 'value': 'Да', 'category': 'Development Opportunities'},
        ]
    else:
        return []


# Kemerovo
def get_parameters_kemerovo(section_name):
    if section_name == 'Football Section':
        return [
            {'name': 'Physical Fitness', 'value': 'Максимальная подготовка', 'category': 'Physical Fitness'},
            {'name': 'Schedule', 'value': '16:00-20:00', 'category': 'Schedule'},
            {'name': 'Location', 'value': 'Парк', 'category': 'Location'},
            {'name': 'Cost', 'value': '4500руб', 'category': 'Cost'},
            {'name': 'Coach Reputation', 'value': '5', 'category': 'Coach Reputation'},
            {'name': 'Atmosphere', 'value': 'Дружелюбная', 'category': 'Atmosphere'},
            {'name': 'Club Achievements', 'value': 'Есть', 'category': 'Club Achievements'},
            {'name': 'Development Opportunities', 'value': 'Да', 'category': 'Development Opportunities'},
        ]
    elif section_name == 'Tennis Section':
        return [
            {'name': 'Physical Fitness', 'value': 'Средняя подготовка', 'category': 'Physical Fitness'},
            {'name': 'Schedule', 'value': '16:00-20:00', 'category': 'Schedule'},
            {'name': 'Location', 'value': 'Парк', 'category': 'Location'},
            {'name': 'Cost', 'value': '2500руб', 'category': 'Cost'},
            {'name': 'Coach Reputation', 'value': '4.5', 'category': 'Coach Reputation'},
            {'name': 'Atmosphere', 'value': 'Дружелюбная', 'category': 'Atmosphere'},
            {'name': 'Club Achievements', 'value': 'Есть', 'category': 'Club Achievements'},
            {'name': 'Development Opportunities', 'value': 'Да', 'category': 'Development Opportunities'},
        ]
    elif section_name == 'Basketball Section':
        return [
            {'name': 'Physical Fitness', 'value': 'Средняя подготовка', 'category': 'Physical Fitness'},
            {'name': 'Schedule', 'value': '12:00-16:00', 'category': 'Schedule'},
            {'name': 'Location', 'value': 'Парк', 'category': 'Location'},
            {'name': 'Cost', 'value': '3500руб', 'category': 'Cost'},
            {'name': 'Coach Reputation', 'value': '5', 'category': 'Coach Reputation'},
            {'name': 'Atmosphere', 'value': 'Дружелюбная', 'category': 'Atmosphere'},
            {'name': 'Club Achievements', 'value': 'Есть', 'category': 'Club Achievements'},
            {'name': 'Development Opportunities', 'value': 'Да', 'category': 'Development Opportunities'},
        ]
    elif section_name == 'Swimming Section':
        return [
            {'name': 'Physical Fitness', 'value': 'Максимальная подготовка', 'category': 'Physical Fitness'},
            {'name': 'Schedule', 'value': '8:00-12:00', 'category': 'Schedule'},
            {'name': 'Location', 'value': 'Бассейн', 'category': 'Location'},
            {'name': 'Cost', 'value': '4500руб', 'category': 'Cost'},
            {'name': 'Coach Reputation', 'value': '5', 'category': 'Coach Reputation'},
            {'name': 'Atmosphere', 'value': 'Дружелюбная', 'category': 'Atmosphere'},
            {'name': 'Club Achievements', 'value': 'Есть', 'category': 'Club Achievements'},
            {'name': 'Development Opportunities', 'value': 'Да', 'category': 'Development Opportunities'},
        ]
    else:
        return []


# Tomsk
def get_parameters_tsk(section_name):
    if section_name == 'Football Section':
        return [
            {'name': 'Physical Fitness', 'value': 'Максимальная подготовка', 'category': 'Physical Fitness'},
            {'name': 'Schedule', 'value': '16:00-20:00', 'category': 'Schedule'},
            {'name': 'Location', 'value': 'Парк', 'category': 'Location'},
            {'name': 'Cost', 'value': '4500руб', 'category': 'Cost'},
            {'name': 'Coach Reputation', 'value': '5', 'category': 'Coach Reputation'},
            {'name': 'Atmosphere', 'value': 'Дружелюбная', 'category': 'Atmosphere'},
            {'name': 'Club Achievements', 'value': 'Есть', 'category': 'Club Achievements'},
            {'name': 'Development Opportunities', 'value': 'Да', 'category': 'Development Opportunities'},
        ]
    elif section_name == 'Tennis Section':
        return [
            {'name': 'Physical Fitness', 'value': 'Средняя подготовка', 'category': 'Physical Fitness'},
            {'name': 'Schedule', 'value': '16:00-20:00', 'category': 'Schedule'},
            {'name': 'Location', 'value': 'Парк', 'category': 'Location'},
            {'name': 'Cost', 'value': '2500руб', 'category': 'Cost'},
            {'name': 'Coach Reputation', 'value': '4.5', 'category': 'Coach Reputation'},
            {'name': 'Atmosphere', 'value': 'Дружелюбная', 'category': 'Atmosphere'},
            {'name': 'Club Achievements', 'value': 'Есть', 'category': 'Club Achievements'},
            {'name': 'Development Opportunities', 'value': 'Да', 'category': 'Development Opportunities'},
        ]
    elif section_name == 'Volleyball Section':
        return [
            {'name': 'Physical Fitness', 'value': 'Средняя подготовка', 'category': 'Physical Fitness'},
            {'name': 'Schedule', 'value': '12:00-16:00', 'category': 'Schedule'},
            {'name': 'Location', 'value': 'Парк', 'category': 'Location'},
            {'name': 'Cost', 'value': '3500руб', 'category': 'Cost'},
            {'name': 'Coach Reputation', 'value': '5', 'category': 'Coach Reputation'},
            {'name': 'Atmosphere', 'value': 'Дружелюбная', 'category': 'Atmosphere'},
            {'name': 'Club Achievements', 'value': 'Есть', 'category': 'Club Achievements'},
            {'name': 'Development Opportunities', 'value': 'Да', 'category': 'Development Opportunities'},
        ]
    elif section_name == 'Yoga Section':
        return [
            {'name': 'Physical Fitness', 'value': 'Максимальная подготовка', 'category': 'Physical Fitness'},
            {'name': 'Schedule', 'value': '8:00-12:00', 'category': 'Schedule'},
            {'name': 'Location', 'value': 'Парк', 'category': 'Location'},
            {'name': 'Cost', 'value': '4500руб', 'category': 'Cost'},
            {'name': 'Coach Reputation', 'value': '5', 'category': 'Coach Reputation'},
            {'name': 'Atmosphere', 'value': 'Дружелюбная', 'category': 'Atmosphere'},
            {'name': 'Club Achievements', 'value': 'Есть', 'category': 'Club Achievements'},
            {'name': 'Development Opportunities', 'value': 'Да', 'category': 'Development Opportunities'},
        ]
    else:
        return []


# Novosibirsk
def get_parameters_nsk(section_name):
    if section_name == 'Football Section':
        return [
            {'name': 'Physical Fitness', 'value': 'Максимальная подготовка', 'category': 'Physical Fitness'},
            {'name': 'Schedule', 'value': '16:00-20:00', 'category': 'Schedule'},
            {'name': 'Location', 'value': 'Парк', 'category': 'Location'},
            {'name': 'Cost', 'value': '4500руб', 'category': 'Cost'},
            {'name': 'Coach Reputation', 'value': '5', 'category': 'Coach Reputation'},
            {'name': 'Atmosphere', 'value': 'Дружелюбная', 'category': 'Atmosphere'},
            {'name': 'Club Achievements', 'value': 'Есть', 'category': 'Club Achievements'},
            {'name': 'Development Opportunities', 'value': 'Да', 'category': 'Development Opportunities'},
        ]
    elif section_name == 'Tennis Section':
        return [
            {'name': 'Physical Fitness', 'value': 'Средняя подготовка', 'category': 'Physical Fitness'},
            {'name': 'Schedule', 'value': '16:00-20:00', 'category': 'Schedule'},
            {'name': 'Location', 'value': 'Парк', 'category': 'Location'},
            {'name': 'Cost', 'value': '2500руб', 'category': 'Cost'},
            {'name': 'Coach Reputation', 'value': '4.5', 'category': 'Coach Reputation'},
            {'name': 'Atmosphere', 'value': 'Дружелюбная', 'category': 'Atmosphere'},
            {'name': 'Club Achievements', 'value': 'Есть', 'category': 'Club Achievements'},
            {'name': 'Development Opportunities', 'value': 'Да', 'category': 'Development Opportunities'},
        ]
    elif section_name == 'Basketball Section':
        return [
            {'name': 'Physical Fitness', 'value': 'Средняя подготовка', 'category': 'Physical Fitness'},
            {'name': 'Schedule', 'value': '12:00-16:00', 'category': 'Schedule'},
            {'name': 'Location', 'value': 'Парк', 'category': 'Location'},
            {'name': 'Cost', 'value': '3500руб', 'category': 'Cost'},
            {'name': 'Coach Reputation', 'value': '5', 'category': 'Coach Reputation'},
            {'name': 'Atmosphere', 'value': 'Дружелюбная', 'category': 'Atmosphere'},
            {'name': 'Club Achievements', 'value': 'Есть', 'category': 'Club Achievements'},
            {'name': 'Development Opportunities', 'value': 'Да', 'category': 'Development Opportunities'},
        ]
    elif section_name == 'Swimming Section':
        return [
            {'name': 'Physical Fitness', 'value': 'Максимальная подготовка', 'category': 'Physical Fitness'},
            {'name': 'Schedule', 'value': '8:00-12:00', 'category': 'Schedule'},
            {'name': 'Location', 'value': 'Бассейн', 'category': 'Location'},
            {'name': 'Cost', 'value': '4500руб', 'category': 'Cost'},
            {'name': 'Coach Reputation', 'value': '5', 'category': 'Coach Reputation'},
            {'name': 'Atmosphere', 'value': 'Дружелюбная', 'category': 'Atmosphere'},
            {'name': 'Club Achievements', 'value': 'Есть', 'category': 'Club Achievements'},
            {'name': 'Development Opportunities', 'value': 'Да', 'category': 'Development Opportunities'},
        ]
    elif section_name == 'Volleyball Section':
        return [
            {'name': 'Physical Fitness', 'value': 'Средняя подготовка', 'category': 'Physical Fitness'},
            {'name': 'Schedule', 'value': '8:00-12:00', 'category': 'Schedule'},
            {'name': 'Location', 'value': 'Парк', 'category': 'Location'},
            {'name': 'Cost', 'value': '2500руб', 'category': 'Cost'},
            {'name': 'Coach Reputation', 'value': '5', 'category': 'Coach Reputation'},
            {'name': 'Atmosphere', 'value': 'Дружелюбная', 'category': 'Atmosphere'},
            {'name': 'Club Achievements', 'value': 'Есть', 'category': 'Club Achievements'},
            {'name': 'Development Opportunities', 'value': 'Да', 'category': 'Development Opportunities'},
        ]
    elif section_name == 'Yoga Section':
        return [
            {'name': 'Physical Fitness', 'value': 'Максимальная подготовка', 'category': 'Physical Fitness'},
            {'name': 'Schedule', 'value': '8:00-12:00', 'category': 'Schedule'},
            {'name': 'Location', 'value': 'Парк', 'category': 'Location'},
            {'name': 'Cost', 'value': '2500руб', 'category': 'Cost'},
            {'name': 'Coach Reputation', 'value': '5', 'category': 'Coach Reputation'},
            {'name': 'Atmosphere', 'value': 'Дружелюбная', 'category': 'Atmosphere'},
            {'name': 'Club Achievements', 'value': 'Есть', 'category': 'Club Achievements'},
            {'name': 'Development Opportunities', 'value': 'Да', 'category': 'Development Opportunities'},
        ]
    else:
        return []


# Moscow
def get_parameters_msc(section_name):
    if section_name == 'Football Section':
        return [
            {'name': 'Physical Fitness', 'value': 'Максимальная подготовка', 'category': 'Physical Fitness'},
            {'name': 'Schedule', 'value': '16:00-20:00', 'category': 'Schedule'},
            {'name': 'Location', 'value': 'Крытый стадитон', 'category': 'Location'},
            {'name': 'Cost', 'value': '4500руб', 'category': 'Cost'},
            {'name': 'Coach Reputation', 'value': '5', 'category': 'Coach Reputation'},
            {'name': 'Atmosphere', 'value': 'Дружелюбная', 'category': 'Atmosphere'},
            {'name': 'Club Achievements', 'value': 'Есть', 'category': 'Club Achievements'},
            {'name': 'Development Opportunities', 'value': 'Да', 'category': 'Development Opportunities'},
        ]
    elif section_name == 'Tennis Section':
        return [
            {'name': 'Physical Fitness', 'value': 'Средняя подготовка', 'category': 'Physical Fitness'},
            {'name': 'Schedule', 'value': '16:00-20:00', 'category': 'Schedule'},
            {'name': 'Location', 'value': 'Крытый стадитон', 'category': 'Location'},
            {'name': 'Cost', 'value': '2500руб', 'category': 'Cost'},
            {'name': 'Coach Reputation', 'value': '4.5', 'category': 'Coach Reputation'},
            {'name': 'Atmosphere', 'value': 'Дружелюбная', 'category': 'Atmosphere'},
            {'name': 'Club Achievements', 'value': 'Есть', 'category': 'Club Achievements'},
            {'name': 'Development Opportunities', 'value': 'Да', 'category': 'Development Opportunities'},
        ]
    elif section_name == 'Basketball Section':
        return [
            {'name': 'Physical Fitness', 'value': 'Средняя подготовка', 'category': 'Physical Fitness'},
            {'name': 'Schedule', 'value': '12:00-16:00', 'category': 'Schedule'},
            {'name': 'Location', 'value': 'Крытый стадитон', 'category': 'Location'},
            {'name': 'Cost', 'value': '3500руб', 'category': 'Cost'},
            {'name': 'Coach Reputation', 'value': '5', 'category': 'Coach Reputation'},
            {'name': 'Atmosphere', 'value': 'Дружелюбная', 'category': 'Atmosphere'},
            {'name': 'Club Achievements', 'value': 'Есть', 'category': 'Club Achievements'},
            {'name': 'Development Opportunities', 'value': 'Да', 'category': 'Development Opportunities'},
        ]
    elif section_name == 'Swimming Section':
        return [
            {'name': 'Physical Fitness', 'value': 'Максимальная подготовка', 'category': 'Physical Fitness'},
            {'name': 'Schedule', 'value': '8:00-12:00', 'category': 'Schedule'},
            {'name': 'Location', 'value': 'Бассейн', 'category': 'Location'},
            {'name': 'Cost', 'value': '4500руб', 'category': 'Cost'},
            {'name': 'Coach Reputation', 'value': '5', 'category': 'Coach Reputation'},
            {'name': 'Atmosphere', 'value': 'Дружелюбная', 'category': 'Atmosphere'},
            {'name': 'Club Achievements', 'value': 'Есть', 'category': 'Club Achievements'},
            {'name': 'Development Opportunities', 'value': 'Да', 'category': 'Development Opportunities'},
        ]
    elif section_name == 'Volleyball Section':
        return [
            {'name': 'Physical Fitness', 'value': 'Средняя подготовка', 'category': 'Physical Fitness'},
            {'name': 'Schedule', 'value': '8:00-12:00', 'category': 'Schedule'},
            {'name': 'Location', 'value': 'Парк', 'category': 'Location'},
            {'name': 'Cost', 'value': '2500руб', 'category': 'Cost'},
            {'name': 'Coach Reputation', 'value': '5', 'category': 'Coach Reputation'},
            {'name': 'Atmosphere', 'value': 'Дружелюбная', 'category': 'Atmosphere'},
            {'name': 'Club Achievements', 'value': 'Есть', 'category': 'Club Achievements'},
            {'name': 'Development Opportunities', 'value': 'Да', 'category': 'Development Opportunities'},
        ]
    elif section_name == 'Yoga Section':
        return [
            {'name': 'Physical Fitness', 'value': 'Максимальная подготовка', 'category': 'Physical Fitness'},
            {'name': 'Schedule', 'value': '16:00-20:00', 'category': 'Schedule'},
            {'name': 'Location', 'value': 'Парк', 'category': 'Location'},
            {'name': 'Cost', 'value': '4500руб', 'category': 'Cost'},
            {'name': 'Coach Reputation', 'value': '5', 'category': 'Coach Reputation'},
            {'name': 'Atmosphere', 'value': 'Дружелюбная', 'category': 'Atmosphere'},
            {'name': 'Club Achievements', 'value': 'Есть', 'category': 'Club Achievements'},
            {'name': 'Development Opportunities', 'value': 'Да', 'category': 'Development Opportunities'},
        ]
    elif section_name == 'Running Section':
        return [
            {'name': 'Physical Fitness', 'value': 'Максимальная подготовка', 'category': 'Physical Fitness'},
            {'name': 'Schedule', 'value': '8:00-12:00', 'category': 'Schedule'},
            {'name': 'Location', 'value': 'Парк', 'category': 'Location'},
            {'name': 'Cost', 'value': '2500руб', 'category': 'Cost'},
            {'name': 'Coach Reputation', 'value': '5', 'category': 'Coach Reputation'},
            {'name': 'Atmosphere', 'value': 'Дружелюбная', 'category': 'Atmosphere'},
            {'name': 'Club Achievements', 'value': 'Есть', 'category': 'Club Achievements'},
            {'name': 'Development Opportunities', 'value': 'Да', 'category': 'Development Opportunities'},
        ]
    elif section_name == 'Gymnastics Section':
        return [
            {'name': 'Physical Fitness', 'value': 'Максимальная подготовка', 'category': 'Physical Fitness'},
            {'name': 'Schedule', 'value': '8:00-12:00', 'category': 'Schedule'},
            {'name': 'Location', 'value': 'Крытый стадитон', 'category': 'Location'},
            {'name': 'Cost', 'value': '3500руб', 'category': 'Cost'},
            {'name': 'Coach Reputation', 'value': '5', 'category': 'Coach Reputation'},
            {'name': 'Atmosphere', 'value': 'Дружелюбная', 'category': 'Atmosphere'},
            {'name': 'Club Achievements', 'value': 'Есть', 'category': 'Club Achievements'},
            {'name': 'Development Opportunities', 'value': 'Да', 'category': 'Development Opportunities'},
        ]
    elif section_name == 'Cycling Section':
        return [
            {'name': 'Physical Fitness', 'value': 'Максимальная подготовка', 'category': 'Physical Fitness'},
            {'name': 'Schedule', 'value': '8:00-12:00', 'category': 'Schedule'},
            {'name': 'Location', 'value': 'Парк', 'category': 'Location'},
            {'name': 'Cost', 'value': '3500руб', 'category': 'Cost'},
            {'name': 'Coach Reputation', 'value': '5', 'category': 'Coach Reputation'},
            {'name': 'Atmosphere', 'value': 'Дружелюбная', 'category': 'Atmosphere'},
            {'name': 'Club Achievements', 'value': 'Есть', 'category': 'Club Achievements'},
            {'name': 'Development Opportunities', 'value': 'Да', 'category': 'Development Opportunities'},
        ]
    elif section_name == 'Dancing Section':
        return [
            {'name': 'Physical Fitness', 'value': 'Максимальная подготовка', 'category': 'Physical Fitness'},
            {'name': 'Schedule', 'value': '16:00-20:00', 'category': 'Schedule'},
            {'name': 'Location', 'value': 'Крытый стадитон', 'category': 'Location'},
            {'name': 'Cost', 'value': '3500руб', 'category': 'Cost'},
            {'name': 'Coach Reputation', 'value': '5', 'category': 'Coach Reputation'},
            {'name': 'Atmosphere', 'value': 'Дружелюбная', 'category': 'Atmosphere'},
            {'name': 'Club Achievements', 'value': 'Есть', 'category': 'Club Achievements'},
            {'name': 'Development Opportunities', 'value': 'Да', 'category': 'Development Opportunities'},
        ]
    else:
        return []


# Saint Petersburg
def get_parameters_stp(section_name):
    if section_name == 'Football Section':
        return [
            {'name': 'Physical Fitness', 'value': 'Максимальная подготовка', 'category': 'Physical Fitness'},
            {'name': 'Schedule', 'value': '16:00-20:00', 'category': 'Schedule'},
            {'name': 'Location', 'value': 'Крытый стадитон', 'category': 'Location'},
            {'name': 'Cost', 'value': '4500руб', 'category': 'Cost'},
            {'name': 'Coach Reputation', 'value': '5', 'category': 'Coach Reputation'},
            {'name': 'Atmosphere', 'value': 'Дружелюбная', 'category': 'Atmosphere'},
            {'name': 'Club Achievements', 'value': 'Есть', 'category': 'Club Achievements'},
            {'name': 'Development Opportunities', 'value': 'Да', 'category': 'Development Opportunities'},
        ]
    elif section_name == 'Tennis Section':
        return [
            {'name': 'Physical Fitness', 'value': 'Средняя подготовка', 'category': 'Physical Fitness'},
            {'name': 'Schedule', 'value': '16:00-20:00', 'category': 'Schedule'},
            {'name': 'Location', 'value': 'Крытый стадитон', 'category': 'Location'},
            {'name': 'Cost', 'value': '2500руб', 'category': 'Cost'},
            {'name': 'Coach Reputation', 'value': '4.5', 'category': 'Coach Reputation'},
            {'name': 'Atmosphere', 'value': 'Дружелюбная', 'category': 'Atmosphere'},
            {'name': 'Club Achievements', 'value': 'Есть', 'category': 'Club Achievements'},
            {'name': 'Development Opportunities', 'value': 'Да', 'category': 'Development Opportunities'},
        ]
    elif section_name == 'Basketball Section':
        return [
            {'name': 'Physical Fitness', 'value': 'Средняя подготовка', 'category': 'Physical Fitness'},
            {'name': 'Schedule', 'value': '12:00-16:00', 'category': 'Schedule'},
            {'name': 'Location', 'value': 'Крытый стадитон', 'category': 'Location'},
            {'name': 'Cost', 'value': '3500руб', 'category': 'Cost'},
            {'name': 'Coach Reputation', 'value': '5', 'category': 'Coach Reputation'},
            {'name': 'Atmosphere', 'value': 'Дружелюбная', 'category': 'Atmosphere'},
            {'name': 'Club Achievements', 'value': 'Есть', 'category': 'Club Achievements'},
            {'name': 'Development Opportunities', 'value': 'Да', 'category': 'Development Opportunities'},
        ]
    elif section_name == 'Swimming Section':
        return [
            {'name': 'Physical Fitness', 'value': 'Максимальная подготовка', 'category': 'Physical Fitness'},
            {'name': 'Schedule', 'value': '8:00-12:00', 'category': 'Schedule'},
            {'name': 'Location', 'value': 'Бассейн', 'category': 'Location'},
            {'name': 'Cost', 'value': '4500руб', 'category': 'Cost'},
            {'name': 'Coach Reputation', 'value': '5', 'category': 'Coach Reputation'},
            {'name': 'Atmosphere', 'value': 'Дружелюбная', 'category': 'Atmosphere'},
            {'name': 'Club Achievements', 'value': 'Есть', 'category': 'Club Achievements'},
            {'name': 'Development Opportunities', 'value': 'Да', 'category': 'Development Opportunities'},
        ]
    elif section_name == 'Volleyball Section':
        return [
            {'name': 'Physical Fitness', 'value': 'Средняя подготовка', 'category': 'Physical Fitness'},
            {'name': 'Schedule', 'value': '8:00-12:00', 'category': 'Schedule'},
            {'name': 'Location', 'value': 'Парк', 'category': 'Location'},
            {'name': 'Cost', 'value': '2500руб', 'category': 'Cost'},
            {'name': 'Coach Reputation', 'value': '5', 'category': 'Coach Reputation'},
            {'name': 'Atmosphere', 'value': 'Дружелюбная', 'category': 'Atmosphere'},
            {'name': 'Club Achievements', 'value': 'Есть', 'category': 'Club Achievements'},
            {'name': 'Development Opportunities', 'value': 'Да', 'category': 'Development Opportunities'},
        ]
    elif section_name == 'Yoga Section':
        return [
            {'name': 'Physical Fitness', 'value': 'Максимальная подготовка', 'category': 'Physical Fitness'},
            {'name': 'Schedule', 'value': '16:00-20:00', 'category': 'Schedule'},
            {'name': 'Location', 'value': 'Парк', 'category': 'Location'},
            {'name': 'Cost', 'value': '4500руб', 'category': 'Cost'},
            {'name': 'Coach Reputation', 'value': '5', 'category': 'Coach Reputation'},
            {'name': 'Atmosphere', 'value': 'Дружелюбная', 'category': 'Atmosphere'},
            {'name': 'Club Achievements', 'value': 'Есть', 'category': 'Club Achievements'},
            {'name': 'Development Opportunities', 'value': 'Да', 'category': 'Development Opportunities'},
        ]
    elif section_name == 'Running Section':
        return [
            {'name': 'Physical Fitness', 'value': 'Максимальная подготовка', 'category': 'Physical Fitness'},
            {'name': 'Schedule', 'value': '8:00-12:00', 'category': 'Schedule'},
            {'name': 'Location', 'value': 'Парк', 'category': 'Location'},
            {'name': 'Cost', 'value': '2500руб', 'category': 'Cost'},
            {'name': 'Coach Reputation', 'value': '5', 'category': 'Coach Reputation'},
            {'name': 'Atmosphere', 'value': 'Дружелюбная', 'category': 'Atmosphere'},
            {'name': 'Club Achievements', 'value': 'Есть', 'category': 'Club Achievements'},
            {'name': 'Development Opportunities', 'value': 'Да', 'category': 'Development Opportunities'},
        ]
    elif section_name == 'Gymnastics Section':
        return [
            {'name': 'Physical Fitness', 'value': 'Максимальная подготовка', 'category': 'Physical Fitness'},
            {'name': 'Schedule', 'value': '8:00-12:00', 'category': 'Schedule'},
            {'name': 'Location', 'value': 'Крытый стадитон', 'category': 'Location'},
            {'name': 'Cost', 'value': '3500руб', 'category': 'Cost'},
            {'name': 'Coach Reputation', 'value': '5', 'category': 'Coach Reputation'},
            {'name': 'Atmosphere', 'value': 'Дружелюбная', 'category': 'Atmosphere'},
            {'name': 'Club Achievements', 'value': 'Есть', 'category': 'Club Achievements'},
            {'name': 'Development Opportunities', 'value': 'Да', 'category': 'Development Opportunities'},
        ]
    elif section_name == 'Cycling Section':
        return [
            {'name': 'Physical Fitness', 'value': 'Максимальная подготовка', 'category': 'Physical Fitness'},
            {'name': 'Schedule', 'value': '8:00-12:00', 'category': 'Schedule'},
            {'name': 'Location', 'value': 'Парк', 'category': 'Location'},
            {'name': 'Cost', 'value': '3500руб', 'category': 'Cost'},
            {'name': 'Coach Reputation', 'value': '5', 'category': 'Coach Reputation'},
            {'name': 'Atmosphere', 'value': 'Дружелюбная', 'category': 'Atmosphere'},
            {'name': 'Club Achievements', 'value': 'Есть', 'category': 'Club Achievements'},
            {'name': 'Development Opportunities', 'value': 'Да', 'category': 'Development Opportunities'},
        ]
    elif section_name == 'Dancing Section':
        return [
            {'name': 'Physical Fitness', 'value': 'Максимальная подготовка', 'category': 'Physical Fitness'},
            {'name': 'Schedule', 'value': '16:00-20:00', 'category': 'Schedule'},
            {'name': 'Location', 'value': 'Крытый стадитон', 'category': 'Location'},
            {'name': 'Cost', 'value': '3500руб', 'category': 'Cost'},
            {'name': 'Coach Reputation', 'value': '5', 'category': 'Coach Reputation'},
            {'name': 'Atmosphere', 'value': 'Дружелюбная', 'category': 'Atmosphere'},
            {'name': 'Club Achievements', 'value': 'Есть', 'category': 'Club Achievements'},
            {'name': 'Development Opportunities', 'value': 'Да', 'category': 'Development Opportunities'},
        ]
    else:
        return []


# Ekaterinburg
def get_parameters_ekb(section_name):
    if section_name == 'Football Section':
        return [
            {'name': 'Physical Fitness', 'value': 'Максимальная подготовка', 'category': 'Physical Fitness'},
            {'name': 'Schedule', 'value': '16:00-20:00', 'category': 'Schedule'},
            {'name': 'Location', 'value': 'Крытый стадитон', 'category': 'Location'},
            {'name': 'Cost', 'value': '4500руб', 'category': 'Cost'},
            {'name': 'Coach Reputation', 'value': '5', 'category': 'Coach Reputation'},
            {'name': 'Atmosphere', 'value': 'Дружелюбная', 'category': 'Atmosphere'},
            {'name': 'Club Achievements', 'value': 'Есть', 'category': 'Club Achievements'},
            {'name': 'Development Opportunities', 'value': 'Да', 'category': 'Development Opportunities'},
        ]
    elif section_name == 'Tennis Section':
        return [
            {'name': 'Physical Fitness', 'value': 'Средняя подготовка', 'category': 'Physical Fitness'},
            {'name': 'Schedule', 'value': '16:00-20:00', 'category': 'Schedule'},
            {'name': 'Location', 'value': 'Крытый стадитон', 'category': 'Location'},
            {'name': 'Cost', 'value': '2500руб', 'category': 'Cost'},
            {'name': 'Coach Reputation', 'value': '4.5', 'category': 'Coach Reputation'},
            {'name': 'Atmosphere', 'value': 'Дружелюбная', 'category': 'Atmosphere'},
            {'name': 'Club Achievements', 'value': 'Есть', 'category': 'Club Achievements'},
            {'name': 'Development Opportunities', 'value': 'Да', 'category': 'Development Opportunities'},
        ]
    elif section_name == 'Basketball Section':
        return [
            {'name': 'Physical Fitness', 'value': 'Средняя подготовка', 'category': 'Physical Fitness'},
            {'name': 'Schedule', 'value': '12:00-16:00', 'category': 'Schedule'},
            {'name': 'Location', 'value': 'Крытый стадитон', 'category': 'Location'},
            {'name': 'Cost', 'value': '3500руб', 'category': 'Cost'},
            {'name': 'Coach Reputation', 'value': '5', 'category': 'Coach Reputation'},
            {'name': 'Atmosphere', 'value': 'Дружелюбная', 'category': 'Atmosphere'},
            {'name': 'Club Achievements', 'value': 'Есть', 'category': 'Club Achievements'},
            {'name': 'Development Opportunities', 'value': 'Да', 'category': 'Development Opportunities'},
        ]
    elif section_name == 'Swimming Section':
        return [
            {'name': 'Physical Fitness', 'value': 'Максимальная подготовка', 'category': 'Physical Fitness'},
            {'name': 'Schedule', 'value': '8:00-12:00', 'category': 'Schedule'},
            {'name': 'Location', 'value': 'Бассейн', 'category': 'Location'},
            {'name': 'Cost', 'value': '4500руб', 'category': 'Cost'},
            {'name': 'Coach Reputation', 'value': '5', 'category': 'Coach Reputation'},
            {'name': 'Atmosphere', 'value': 'Дружелюбная', 'category': 'Atmosphere'},
            {'name': 'Club Achievements', 'value': 'Есть', 'category': 'Club Achievements'},
            {'name': 'Development Opportunities', 'value': 'Да', 'category': 'Development Opportunities'},
        ]
    elif section_name == 'Volleyball Section':
        return [
            {'name': 'Physical Fitness', 'value': 'Средняя подготовка', 'category': 'Physical Fitness'},
            {'name': 'Schedule', 'value': '8:00-12:00', 'category': 'Schedule'},
            {'name': 'Location', 'value': 'Парк', 'category': 'Location'},
            {'name': 'Cost', 'value': '2500руб', 'category': 'Cost'},
            {'name': 'Coach Reputation', 'value': '5', 'category': 'Coach Reputation'},
            {'name': 'Atmosphere', 'value': 'Дружелюбная', 'category': 'Atmosphere'},
            {'name': 'Club Achievements', 'value': 'Есть', 'category': 'Club Achievements'},
            {'name': 'Development Opportunities', 'value': 'Да', 'category': 'Development Opportunities'},
        ]
    elif section_name == 'Yoga Section':
        return [
            {'name': 'Physical Fitness', 'value': 'Максимальная подготовка', 'category': 'Physical Fitness'},
            {'name': 'Schedule', 'value': '16:00-20:00', 'category': 'Schedule'},
            {'name': 'Location', 'value': 'Парк', 'category': 'Location'},
            {'name': 'Cost', 'value': '4500руб', 'category': 'Cost'},
            {'name': 'Coach Reputation', 'value': '5', 'category': 'Coach Reputation'},
            {'name': 'Atmosphere', 'value': 'Дружелюбная', 'category': 'Atmosphere'},
            {'name': 'Club Achievements', 'value': 'Есть', 'category': 'Club Achievements'},
            {'name': 'Development Opportunities', 'value': 'Да', 'category': 'Development Opportunities'},
        ]
    elif section_name == 'Running Section':
        return [
            {'name': 'Physical Fitness', 'value': 'Максимальная подготовка', 'category': 'Physical Fitness'},
            {'name': 'Schedule', 'value': '8:00-12:00', 'category': 'Schedule'},
            {'name': 'Location', 'value': 'Парк', 'category': 'Location'},
            {'name': 'Cost', 'value': '2500руб', 'category': 'Cost'},
            {'name': 'Coach Reputation', 'value': '5', 'category': 'Coach Reputation'},
            {'name': 'Atmosphere', 'value': 'Дружелюбная', 'category': 'Atmosphere'},
            {'name': 'Club Achievements', 'value': 'Есть', 'category': 'Club Achievements'},
            {'name': 'Development Opportunities', 'value': 'Да', 'category': 'Development Opportunities'},
        ]
    elif section_name == 'Gymnastics Section':
        return [
            {'name': 'Physical Fitness', 'value': 'Максимальная подготовка', 'category': 'Physical Fitness'},
            {'name': 'Schedule', 'value': '8:00-12:00', 'category': 'Schedule'},
            {'name': 'Location', 'value': 'Крытый стадитон', 'category': 'Location'},
            {'name': 'Cost', 'value': '3500руб', 'category': 'Cost'},
            {'name': 'Coach Reputation', 'value': '5', 'category': 'Coach Reputation'},
            {'name': 'Atmosphere', 'value': 'Дружелюбная', 'category': 'Atmosphere'},
            {'name': 'Club Achievements', 'value': 'Есть', 'category': 'Club Achievements'},
            {'name': 'Development Opportunities', 'value': 'Да', 'category': 'Development Opportunities'},
        ]
    elif section_name == 'Cycling Section':
        return [
            {'name': 'Physical Fitness', 'value': 'Максимальная подготовка', 'category': 'Physical Fitness'},
            {'name': 'Schedule', 'value': '8:00-12:00', 'category': 'Schedule'},
            {'name': 'Location', 'value': 'Парк', 'category': 'Location'},
            {'name': 'Cost', 'value': '3500руб', 'category': 'Cost'},
            {'name': 'Coach Reputation', 'value': '5', 'category': 'Coach Reputation'},
            {'name': 'Atmosphere', 'value': 'Дружелюбная', 'category': 'Atmosphere'},
            {'name': 'Club Achievements', 'value': 'Есть', 'category': 'Club Achievements'},
            {'name': 'Development Opportunities', 'value': 'Да', 'category': 'Development Opportunities'},
        ]
    elif section_name == 'Dancing Section':
        return [
            {'name': 'Physical Fitness', 'value': 'Максимальная подготовка', 'category': 'Physical Fitness'},
            {'name': 'Schedule', 'value': '16:00-20:00', 'category': 'Schedule'},
            {'name': 'Location', 'value': 'Крытый стадитон', 'category': 'Location'},
            {'name': 'Cost', 'value': '3500руб', 'category': 'Cost'},
            {'name': 'Coach Reputation', 'value': '5', 'category': 'Coach Reputation'},
            {'name': 'Atmosphere', 'value': 'Дружелюбная', 'category': 'Atmosphere'},
            {'name': 'Club Achievements', 'value': 'Есть', 'category': 'Club Achievements'},
            {'name': 'Development Opportunities', 'value': 'Да', 'category': 'Development Opportunities'},
        ]
    else:
        return []
