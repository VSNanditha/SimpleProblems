import csv

f = open('football.csv', 'r')
# reader = csv.reader(f, delimiter=',')
# # fieldnames = reader.next()
# for row in reader:
#     print('\t'.join(row))

dict_reader = csv.DictReader(f)
for row in dict_reader:
    if row['Team'] == 'Liverpool':
        print(row)
# print(dict_reader)
