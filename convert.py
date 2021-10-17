
import csv
import os

"in_folder = ""/Users/xutian/Documents/Dev/concare/mimic-iii-clinical-database-demo-1.4/"""
"out_folder = ""/Users/xutian/Documents/Dev/concare/mimic-iii-dataset2/"""
arr = os.listdir(in_folder)
# print(arr)

for file_name in arr:
    # print(file_name)
    in_file_name = in_folder + file_name
    out_file_name = out_folder + file_name
    print(in_file_name)
    print(out_file_name)

    inFile = open(in_file_name)
    outFile = open(out_file_name, 'w', newline='')
    inReader = csv.reader(inFile)
    outWriter = csv.writer(outFile)

"    # print(""file row number: """, (inReader))
    counter = 0
    for row in inReader:
        for i in range(len(row)):
            if counter == 0:
                row[i] = row[i].upper()
            else:
                row[i] = row[i]
        outWriter.writerow(row)
        counter = counter + 1
