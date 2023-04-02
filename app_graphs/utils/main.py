import mod

data = [{
  'Country': 'Colombia',
  'Population': 500
}, {
  'Country': 'Bolivia',
  'Population': 300
}]


def run():
  keys, values = mod.get_population()
  print(keys, values)

  print(mod.A)

  country = input('Ingresa país: ')
  result = mod.population_by_country(data, country)
  print(f'result: {result}')


if __name__ == '__main__':
  run()
