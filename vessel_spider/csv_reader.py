import csv

# load input file
data = list()

with open("../data/unique_vessel.csv", newline="") as f:
    reader = csv.DictReader(f)
    for row in reader:
        data.append(row["Vessel_name"])