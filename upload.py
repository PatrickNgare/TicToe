import csv
with open("job.csv",'rb') as f:
    reader=csv.reader(f)
    for row in reader:
        print (row)
