import pandas as pd

def process_files():
    # Read the files
    files = ['file1.csv', 'file2.csv']
    for file in files:
        df = pd.read_csv(file)

        # Process the data
        df['new_column'] = df['column1'] + df['column2']

        # Save the processed data to a new file
        df.to_csv(f'processed_{file}', index=False)

        # Move the original file to the archive folder
        import os
        os.rename(file, f'archive/{file}')

        # Log the processing completion
        print(f'File {file} processed successfully!')
