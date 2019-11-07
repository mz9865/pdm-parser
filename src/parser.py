import csv

with open("data.csv") as data:
    for line in data:
        tokens = line.split(" ")
        for i in range(len(tokens)):
            tokens[i] = tokens[i].strip("\"")




