import csv

def extract_distinct_field(file_path, column_index):
    distinct_values = set()
    
    with open(file_path, mode='r', newline='') as file:
        reader = csv.reader(file)
        next(reader)  # Skip the header row
        for row in reader:
            if len(row) > column_index:
                distinct_values.add(row[column_index])
    
    return distinct_values

file_path = './data/Cruscotto_Storico_export_1737472732848.csv'

column_index = 0  # Column index starts from 0, so column 3 is index 2


def visualize_first_10_rows(file_path):
    with open(file_path, mode='r', newline='') as file:
        reader = csv.reader(file)
        for i, row in enumerate(reader):
            if i >= 10:
                break
            print(row)

#visualize_first_10_rows(file_path)

distinct_values = extract_distinct_field(file_path, column_index)
print(distinct_values)
