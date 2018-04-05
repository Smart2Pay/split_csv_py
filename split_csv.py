import os
import sys

try:
    if len(sys.argv) < 3:
        print('usage: split_csv.exe {file_name} {rows_per_csv}')
        sys.exit()
    total_rows_per_csv = None
    try:
        total_rows_per_csv = int (sys.argv[2])
    except Exception:
        print(f'rows_per_csv {sys.argv[2]} must be an integer. e.g. 50000')
        sys.exit()
      
    file_name = sys.argv[1]

    original_csv = open(f'{file_name}','r')
    original_content = original_csv.readlines()
    original_csv.close()
    total_rows = original_content.__len__()
    split_no = (int)(total_rows / total_rows_per_csv)+1
    print(f'Total rows per CSV: {total_rows}')
    print(f'Splitting in {split_no} CSVs...')
    
    for i in range(split_no):
        print(f'Splitting {file_name}_{i}.csv')
        f = open(f'{file_name}_{i}.csv', 'w+')
        if i>0:
            f.writelines(original_content[0])
        f.writelines(original_content[i*total_rows_per_csv:(i+1)*(total_rows_per_csv)])
        f.close()

    
except FileNotFoundError:
    print(f'Filename {file_name} was not found!')