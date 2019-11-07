import csv

all_rows = []
tokens =[]
with open("data.csv") as data:
    for line in data:
        tokens = line.split(" ")
        for i in range(len(tokens)):
            tokens[i] = tokens[i].strip("\"")
        all_rows.append(tokens)

with open("output.csv", "w") as output:
    for i in range(len(all_rows)):
        tokens = all_rows[i]
        string = ""
        for token in tokens:
            string += token
            string += ","
        string += "\n"
        output.write(string)

"""        
    for row in all_rows:
        string = ""
        for token in tokens:
            string += token
            string += ","
        string += "\n"
        output.write(string)
"""


