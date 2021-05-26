from hash_table import HashTable
from package import Package

hash_table = HashTable()

hash_table.insert(1, "foo")

result = hash_table.lookup(1)

print(result)

package1 = Package(1, '123 sesame st', 'malvern',
                   'oh', 44644, '12:20', 14, None)

print(package1.package_to_string())

package1.set_zip(44718)

print(package1.package_to_string())
