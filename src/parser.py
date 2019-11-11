import csv
import codecs

all_rows = []
newRowsList = []

# Open txt file and split by quotes
with codecs.open("data.txt", "r", encoding="utf-8", errors="ignore") as data:
    for line in data:
        splittedLine = line.split("\"")
        for token in splittedLine:
            if token == "" or token == " ":
                splittedLine.remove(token)
            if "\n" in token:
                token.strip("\r\n")
        all_rows.append(splittedLine)

# Strip leading and trailing empty spaces in the tokens
for i in range(len(all_rows)):
    for j in range(len(all_rows[i])):
        if all_rows[i][j][0] == " " or all_rows[i][j][len(all_rows[i][j]) - 1]:
            all_rows[i][j] = all_rows[i][j].lstrip()
            all_rows[i][j] = all_rows[i][j].rstrip()

# Join the two numbers for the question key
for i in range(len(all_rows)):
    if i > 0:
        all_rows[i][0:2] = [' '.join(all_rows[i][0:2])]

# Separate the NAs
for row in all_rows:
    newRow = []
    for token in row:
        if token[0:2] == "NA" or (token[0:2] == "1 " and "NA" in token):
            for word in token.split(" "):
                newRow.append(word)
        else:
            newRow.append(token)
    newRowsList.append(newRow)

# Remove the \r\n in the last token of the row
del newRowsList[0][-1]
for row in newRowsList:
    if '\r\n' in row[189]:
        row[189] = row[189].replace('\r\n', '')


# Write to CSV file
with open("output.csv", "w") as output:
    for i in range(len(newRowsList)):
        writer = csv.writer(output)
        writer.writerow(newRowsList[i])
