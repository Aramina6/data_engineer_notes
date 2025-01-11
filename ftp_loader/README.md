# FTP File Loader & Processing Pipeline

## Overview
This project is an Airflow pipeline that downloads files from an FTP server, validates their format, processes the data, and archives the original files.

## Features
- Downloads files from an FTP server based on a specified pattern.
- Validates the format of the downloaded files.
- Processes the data in the validated files.
- Archives the original files.

## Requirements
- Python 3.8+
- The dependencies listed in `requirements.txt`.

## Installation
### Step 1: Clone the Repository
```bash
git clone https://github.com/your-username/ftp-file-processing-pipeline.git
```

### Step 2: Install Dependencies
```bash
pip install -r requirements.txt
```

### Step 3: Initialize Airflow Database
```bash
airflow db init
```

### Step 4: Start Airflow Webserver
```bash
airflow webserver -p 8080
```

### Step 5: Start Airflow Scheduler
```bash
airflow scheduler
```

## Configuration
### Step 1: Update FTP Credentials
Update the `FTP_HOST`, `FTP_USERNAME`, and `FTP_PASSWORD` variables in `ftp_file_processing.py` to match your FTP server credentials.

### Step 2: Update File Pattern
Update the `FILE_PATTERN` variable in `ftp_file_processing.py` to match the pattern of the files you want to download.

### Step 3: Update Required Columns
Update the `REQUIRED_COLUMNS` variable in `ftp_file_processing.py` to match the required columns in the downloaded files.

## Usage
### Step 1: Trigger Pipeline
Trigger the pipeline manually using the Airflow web interface.

### Step 2: Pipeline Execution
The pipeline will:
- Download files from the FTP server.
- Validate their format.
- Process the data.
- Archive the original files.

## Contributing
Contributions are welcome! Please submit a pull request with your changes.

## Acknowledgments
This project uses the following third-party libraries:
- Apache Airflow
- pandas
- ftplib
- python-decouple
- python-dotenv
- setproctitle
- tenacity
- typing-extensions
- wheel
```
