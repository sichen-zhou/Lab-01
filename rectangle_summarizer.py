# %% Reading CSV
import csv
with open('rectangles_data.csv', newline="") as f:
    reader = csv.reader(f)
    next(reader)
    for row in reader:
        print(row)

# %% Counting Rows and Columns
import csv
with open('rectangles_data.csv', newline="") as f:
    data = list(csv.reader(f))
print("rows:",len(data)-1)
print("columns:", len(data[0]))

# %%
with open("summary.csv", 'w', newline="") as f:
    writer = csv.writer(f)
    writer.writerow([r[0] for r in data])
    writer.writerow([r[1] for r in data])



