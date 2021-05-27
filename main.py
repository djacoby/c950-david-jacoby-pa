from hash_table import HashTable
from package import Package
import csv

hash_table = HashTable()

with open('./data/packages.csv', 'r', encoding='utf-8-sig') as csvfile:
    package_reader = csv.reader(csvfile)
    for row in package_reader:
        hash_table.insert(row[0],
                          Package(row[0], row[1], row[2], row[3], row[4], row[5], row[6], row[7]))

result = hash_table.lookup(1)

print(result.id)
