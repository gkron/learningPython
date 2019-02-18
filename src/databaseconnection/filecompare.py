import csv, itertools,sys
#sys.stdout=open("mismatch.txt","w")
column_names = ['id','name','amount']
source_data = csv.reader(open('foo1.csv'))
print(source_data)
target_data = csv.reader(open('foo2.csv'))
print(target_data)
counter = 1
def rowElementCompare(sourceRow, targetRow):
    row_length = min(len(sourceRow), len(targetRow))
    for i in range(row_length):
        if sourceRow[i] != targetRow[i]:
            print (i)
            yield (i) # UPDATED
    return 
for source_row,target_row in itertools.zip_longest(source_data,target_data):
    comparison_result = None
    for comparison_result in rowElementCompare(source_row, target_row):
      s=print ("Mismatch in column %s on row number %d , source value %s, target value %s" % (column_names[comparison_result], counter, source_row[comparison_result], target_row[comparison_result]))
      counter += 1


rowElementCompare(source_data,target_data)