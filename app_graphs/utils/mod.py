# def get_population():
#  keys = ['col', 'bol']
#  values = [300, 400]
#  return keys, values


def get_population(country_dict):
    population_dict = {
        '2022': country_dict['2022 Population'],
        '2020': country_dict['2020 Population'],
        '2015': country_dict['2015 Population'],
        '2010': country_dict['2010 Population'],
        '2000': country_dict['2000 Population'],
        '1990': country_dict['1990 Population'],
        '1980': country_dict['1980 Population'],
        '1970': country_dict['1970 Population'],
    }

    population_dict = {key: int(value)
                       for key, value in population_dict.items()}
    labels = population_dict.keys()
    values = population_dict.values()

    return labels, values


A = 'Hola'


def population_by_country(data, country):
    result = list(filter(lambda item: item['Country'] == country,
                         data))
    return result


def get_data_by_country(data, country):
    result = list(filter(lambda item: item['Country'] == country,
                         data))
    return result[0]


def get_countrys_percents(data):
    countrys = list(map(lambda dict: dict['Country'], data))
    countrys_code = list(map(lambda dict: dict['CCA3'], data))
    percents = list(
        map(lambda dict: dict['World Population Percentage'], data))
    return countrys, countrys_code, percents


if __name__ == '__main__':
    pass
