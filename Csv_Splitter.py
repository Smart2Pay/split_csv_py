class Csv_Splitter:
    def __init__(self, file_name, rows_per_csv):
        self.file_name = file_name
        self.rows_per_csv = int(rows_per_csv)
    
    def split(self):
        try:
            original_csv = open(f'{self.file_name}','r')
            original_content = original_csv.readlines()
            original_csv.close()
            total_rows = original_content.__len__()
            split_no = (int)(total_rows / self.rows_per_csv)+1
            print(f'Total rows per CSV: {total_rows}')
            print(f'Splitting in {split_no} CSVs...')
    
            for i in range(split_no):
                print(f'Splitting {self.file_name}_{i}.csv')
                f = open(f'{self.file_name}_{i}.csv', 'w+')
                if i>0:
                    f.writelines(original_content[0])
                f.writelines(original_content[i*self.rows_per_csv:(i+1)*(self.rows_per_csv)])
                f.close()

    
        except FileNotFoundError:
            print(f'Filename {self.file_name} was not found!')
