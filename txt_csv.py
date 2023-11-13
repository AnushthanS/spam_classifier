import csv

input_file = 'lemmatization-en.txt'
output_file = 'lemmatization-en.csv'

with open(input_file, 'r') as txtfile, open(output_file, 'w', newline='') as csvfile:
    reader = csv.reader(txtfile, delimiter='\t')
    writer = csv.writer(csvfile)
    
    for row in reader:
        writer.writerow(row)