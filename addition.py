import numpy as np

array_number = int(input('Enter the number of arrays you want to create: '))
array_no = []

for i in range(array_number):
    rows = int(input('Enter the number of rows: '))
    cols = int(input('Enter the number of columns: '))
    value = []
    
    for r in range(rows):
        row = []  
        for c in range(cols):
            print('Enter the value for position ({},{}):'.format(r+1, c+1))
            ele = int(input())
            row.append(ele)
        value.append(row)
    
    array_no.append(value)

print("Created arrays:")
for j, value in enumerate(array_no):
    print(f'Array {j+1}:')
    for row in value:
        print(row)

rows = len(array_no[0])  
cols = len(array_no[0][0])  
result_mat = [[0] * cols for _ in range(rows)]  

for value in array_no:
    for i in range(rows):
        for j in range(cols):
            result_mat[i][j] += value[i][j]

print("Resultant Matrix after addition:")
for row in result_mat:
    print(row)
