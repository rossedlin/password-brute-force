import csv
from itertools import product

def import_csv_to_array(file_path):
    with open(file_path, 'r') as file:
        reader = csv.reader(file)
        return [row[0].strip() for row in reader if row]


# Replace with your own CSV file paths
files = ['csv/Aword.csv', 'csv/Fword.csv', 'csv/Hword.csv', 'csv/Mword.csv']
words = [import_csv_to_array(file) for file in files]

password = 'hedgehog_finite_minus'

# Generate all combinations and compare with password
for combination in product(*words):
    potential = "_".join(combination)
    if potential == password:
        print('Password found:', potential)
        break
