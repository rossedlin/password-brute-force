import csv

def import_csv_to_array(file_path):
    with open(file_path, mode='r') as file:
        # reading the CSV file
        csvFile = csv.reader(file)

        # Create an empty list to store the rows of the csv
        csv_data = []

        # Get the header row
        header = next(csvFile)

        # Iterate over remaining rows
        for row in csvFile:
            if 0 < len(row):
                line = row[0]
                item = line.strip()
                # print(item)
                csv_data.append(item)
                # break

        return csv_data


# Replace with your own CSV file path
a = import_csv_to_array('csv/Aword.csv')
f = import_csv_to_array('csv/Fword.csv')
h = import_csv_to_array('csv/Hword.csv')
m = import_csv_to_array('csv/Mword.csv')

password = 'hedgehog_finite_minus'
words = a + f + h + m

potential = ['hedgehog', '1', '2']
for first in words:
    # print(first)
    # potential[0] = first
    for second in words:
        # print(second)
        potential[1] = second
        for third in words:
            # print(third)
            potential[2] = third
            print("_".join(potential))
            if password == "_".join(potential):
                print('FOUND!!!')
                exit()
            # break
        # break
    # break
