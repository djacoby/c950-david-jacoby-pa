from hash_table import HashTable
from package import Package
import csv

hash_table = HashTable()

with open('./data/packages.csv', 'r', encoding='utf-8-sig') as csvfile:
    package_reader = csv.reader(csvfile)
    for row in package_reader:
        package = Package(row[0], row[1], row[2], row[3],
                          row[4], row[5], row[6], row[7])
        break
        # hash_table.insert(row[0],
        #                   Package(row[0], row[1], row[2], row[3], row[4], row[5], row[6], row[7]))


# result = hash_table.lookup(2)

# print(result.address)

# result.to_string()

package.set_status('In transit')
package.to_string()
