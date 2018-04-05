#from pympler import asizeof

class Csv_Splitter:

    def __init__(self, file_name, rows_per_csv, buffer=10000, memory_hint=8196):
        self.file_name = file_name.split('.')[0]
        self.file = file_name
        self.rows_per_csv = int(rows_per_csv)
        self.buffer = min(buffer, self.rows_per_csv)
        self.memory_hint = memory_hint

    def split(self):
        try:
            original_csv = open(f'{self.file}','r')
            header = original_csv.readline()
            print(f'Splitting {self.file} in  CSVs...')
            stop_read = False
            current_batch_no = 1
            while not stop_read:
                print(f'Splitting to {self.file_name}_{current_batch_no}.csv')
                f = open(f'{self.file_name}_{current_batch_no}.csv', 'w+')
                f.writelines(header)
                current_batch_start=0
                current_batch = []
                current_batch_line_read = 0
                current_batch_buffer_line_read = 0
                stop_batch = False
                while not stop_batch:
                    current_lines = original_csv.readlines(self.memory_hint)
                    #print(f'Batch memory current_lines (bytes): {asizeof.asizeof(current_lines)}')
                    if not current_lines:
                        f.writelines(current_batch) 
                        stop_read = True
                        stop_batch = True
                        break

                    current_batch += current_lines
                    current_batch_buffer_line_read += len(current_lines)
                    current_batch_line_read += len(current_lines)
                    if current_batch_buffer_line_read >= self.buffer:
                        #print('------------------------Writing batch')
                        #print(f'Batch memory current_batch (bytes): {asizeof.asizeof(current_batch)}')
                        f.writelines(current_batch)
                        current_batch = []
                        current_batch_buffer_line_read = 0
                    if current_batch_line_read >= self.rows_per_csv:
                        stop_batch = True
                    if stop_batch and not stop_read:
                        #print('------------------------Finalizing batch')
                        #print(f'Batch memory current_batch (bytes): {asizeof.asizeof(current_batch)}')
                        f.writelines(current_batch) 
                        f.close() 
                        current_batch = []
                        current_batch_line_read = 0
                        current_batch_start += current_batch_no * self.buffer
                        current_batch_no += 1
                    elif stop_read:
                        original_csv.close()
                        break
        except FileNotFoundError:
            print(f'Filename {self.file_name} was not found!')
