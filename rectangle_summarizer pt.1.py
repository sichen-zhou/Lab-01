# Lab Activity 3 part 1
# %% Reads the content of a CSV file
import csv
with open('rectangles_data.csv', newline="") as f:
    reader = csv.reader(f)
    next(reader)
    for row in reader:
        print(row)

# %% Counts and prints out the total count of rectangles
import csv
with open('rectangles_data.csv', newline="") as f:
    reader = csv.reader(f)
    next(reader)
    data = list(csv.reader(f))
print("rows:",len(data))