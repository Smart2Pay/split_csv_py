import sys
from Csv_Splitter import Csv_Splitter

if len(sys.argv) < 3:
    print('usage: split_csv.exe {file_name} {rows_per_csv}')
    sys.exit()
total_rows_per_csv = None
try:
    total_rows_per_csv = int (sys.argv[2])
except Exception:
    print(f'rows_per_csv {sys.argv[2]} must be an integer. e.g. 50000')
    sys.exit()
        

splitter = Csv_Splitter(sys.argv[1],sys.argv[2])
splitter.split()
