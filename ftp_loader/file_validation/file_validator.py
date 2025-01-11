import pandas as pd

def validate_files():
    # Read the files
    files = ['file1.csv', 'file2.csv']
    for file in files:
        df = pd.read_csv(file)

        # Check the file format
        if not df.columns.equals(['column1', 'column2', 'column3']):
            raise ValueError(f'Invalid file format: {file}')
