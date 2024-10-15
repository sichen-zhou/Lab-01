import csv
with open('rectangles_data.csv', newline="") as f:
    reader = csv.reader(f)
    next(reader)
    for row in reader:
        print(row)

rectangles = row
for r in rectangles:
    print(r)

with open("summary.csv", 'w', newline="") as f:
    writer = csv.writer(f)
    writer.writerow([r[0]] for r in rectangles)
    writer.writerow([r[1]] for r in rectangles)
