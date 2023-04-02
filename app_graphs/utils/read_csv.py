import csv


def read_csv(path):
  with open(path, 'r') as csvFile:
    reader = csv.reader(csvFile, delimiter=',')
    header = next(reader)
    data = []

    for row in reader:
      #print(row)
      iterable = zip(header, row)
      country_dict = {key: value for key, value in iterable}
      #print(country_dict)
      #print("***" * 5)
      data.append(country_dict)

    return data


if __name__ == '__main__':
  data = read_csv('./utils/data.csv')
  #print(data)
