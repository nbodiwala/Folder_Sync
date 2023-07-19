import csv
from subprocess import call
from config import csv_path

with open(csv_path, mode='r') as csv_file:
    csv_reader = csv.DictReader(csv_file)
    for line in csv_reader:
        source = line['Source']
        destination = line['Destination']

        call(['robocopy', source, destination, '/MIR', '/S', '/XD', '/XO', '*_archive'])