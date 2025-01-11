import ftplib

def download_files_from_ftp():
    # Connect to the FTP server
    ftp = ftplib.FTP('ftp.example.com')
    ftp.login(user='username', passwd='password')

    # Download files
    files = ftp.nlst('*economy_data_DDYYYY.csv')
    for file in files:
        with open(file, 'wb') as f:
            ftp.retrbinary(f'RETR {file}', f.write)

    # Close the FTP connection
    ftp.quit()
