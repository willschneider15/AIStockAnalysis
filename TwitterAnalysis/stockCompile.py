import csv
import string

# with open('s&p.csv') as csvfile: #append to new file
#     csv_reader = csv.reader(csvfile, delimiter=',')
#     line_count = 0
#     with open('stocklist.csv', 'a', newline='') as write:
#         employee_writer = csv.writer(write)
#         for row in csv_reader:
#             if row[0].find('$') == -1:
#                 employee_writer.writerow([row[0], row[1]])
#                 line_count += 1
#         print(f"Processed {line_count} lines")


# with open('stocklist.csv') as csvfile: #remove same stock symbols
#     csv_reader = csv.reader(csvfile, delimiter=',')
#     line_count = 0
#     with open('stocks.csv', 'w', newline='') as write:
#         writer = csv.writer(write)
#         lastnames = set()
#         for row in csv_reader:
#             if row[0] not in lastnames:
#                 writer.writerow(row)
#                 lastnames.add( row[0] )



# with open('stocks.csv', 'r') as f:   #alphabetical sort
#     data = [line for line in csv.reader(f)]


# data.sort(key=itemgetter(0))  # 1 being the column number

# with open('stockz.csv', 'w') as f:
#     csv.writer(f).writerows(data)


  
