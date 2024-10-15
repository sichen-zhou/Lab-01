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
    data = list(csv.reader(f))
print("rows:",len(data)-1)
# print("columns:", len(data[0]))

# %% Calculates and prints out the total, average, maximum and minimum area of all rectangles
import csv
with open('rectangles_data.csv', newline="") as f:
    reader = csv.reader(f)
    next(reader)
    for row in reader:
        data.append([float(row[2]) * float(row[3])])


# %%
import csv
with open("summary.csv", 'w', newline="") as f:
    writer = csv.writer(f, delimiter=' ', quotechar='|', quoting=csv.QUOTE_MINIMAL)
    writer.writerow(['total count'], ['total area'], ['average area'], ['maximum area'], ['minimum area'])




