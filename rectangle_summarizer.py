# Reads the content of a CSV file
import csv
with open('rectangles_data.csv', newline="") as f:
    reader = csv.reader(f)
    next(reader)
    for row in reader:
        print(row)

# Counts and prints out the total count of rectangles
with open('rectangles_data.csv', newline="") as f:
    reader = csv.reader(f)
    next(reader)
    data = list(csv.reader(f))
print("rows:",len(data))

# Calculates and prints out the total, average, maximum and minimum area of all rectangles
# Stores the above information in another CSV file named summary02.csv
import statistics as st
with open('rectangles_data.csv', newline="") as f:
    reader = csv.reader(f) # Reads the content of a CSV file
    next(reader)     #table of strings, ignore header row
    width_list = []  #empty list
    height_list = [] #empty list
    area_list = []   #empty list
    for row in reader:  # loop begins
        width = float(row[1])
        height = float(row[2])
        width_list.append(width)
        height_list.append(height)
        area_list.append(width * height) # loop ends
    # print(f'{max(area_list)}') # without math or stat module
    # print(f'{area_list.max()}') # with math or stat module
    # create dictionary
        data = {
            'total count':len(area_list),
            'total area':sum(area_list),
            'average area':st.mean(area_list),
            'maximum area':max(area_list),
            'minimum area':min(area_list)
            }
    # print(data)
    fields = ['total count', 'total area', 'average area', 'maximum area', 'minimum area']
with open('summary02.csv', 'w', newline="") as f:
    writer = csv.DictWriter(f, fieldnames=fields)
    writer.writeheader()
    writer.writerow(data)