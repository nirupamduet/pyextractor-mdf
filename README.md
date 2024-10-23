# pyextractor-mdf
Data extrator from file storage [60GB] including specially mdf files

# Data Processing Script

This script cleans a directory of unwanted files, unzips ZIP files, unarchives RAR files, deletes empty folders, and merges DBF files based on their headers into CSV files.

## Features
- **Unzip Files**: Unzips all ZIP files and deletes them post-extraction.
- **Unrar Files**: Unarchives RAR files and deletes them after extraction.
- **Clean Directory**: Recursively deletes files with unwanted extensions.
- **Delete Empty Folders**: Removes any empty directories.
- **Merge DBF Files**: Merges DBF files by their headers into separate CSV files.

## Installation
Make sure you have the required libraries installed:

```bash
pip install pandas dbfread rarfile

```

## Usage
Run the script with the following command:

```bash
python data_processing_script.py
```

## Example
To execute the script, simply run it in your terminal. It will process the specified directory defined in the script.

## Parameters

## Parameter	Type	Description
data_dir	string	The root directory containing files to process

## Output
The script generates CSV files named merged_output_#.csv and merged_output_clean_#.csv for merged DBF files.

## Error Handling
The script handles various exceptions, including file deletion errors and extraction failures, logging appropriate messages.

## Contributing
Feel free to submit issues or pull requests to improve functionality.


