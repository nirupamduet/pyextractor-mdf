import os
import zipfile
import pandas as pd
from dbfread import DBF
from collections import defaultdict
import rarfile


data_dir = r"C:\Users\nirupam\Desktop\GPF_Projects\Data\001-025"
output_csv = 'merged_output.csv'
counter = 1

unwanted_file_types = [
    '.tmp', '.temp', '.swp', '.swo', '.3gp', '.avi', '.mp4', '.pif', '.mdb',
    '.bak', '.old', '.backup', '.wmv',
    '.log', '.trace', '.out',
    '.cache', '.pyo', '.pyc',
    '.DS_Store', '.thumbs.db', 'desktop.ini',
    '.git', '.vscode', '.idea', '.obj', '.act', '.ocx', '.api',
    '.app', '.exe', '.dll', '.application', '.aps', '.awx', '.bad', '.bas', '.BIN',
    '.bmp', '.c', '.csproj', '.cs', '.H', '.js', '.act', '.ocx',
    '.c00', '.cmd', '.cdx', '.cmd', '.cdx',
    '.CSS', '.css', '.cfm', '.CFM', '.pdf', '.pdf', '.clw', '.clw',
    '.dat', '.DAT', '.xsd', '.wri', '.wm', '.cab', '.cab', '.sct',
    '.msi', '.bat', '.wav', '.vsl', '.suo', '.sln',
    '.vcx', '.vcx', '.vct', '.vcd', '.mdp', '.vbw',
    '.vbp', '.pfm', '.tto', '.tto', '.ttf', '.TTF',
    '.tlb', '.tfr', '.tlb', '.tfr', '.tbk', '.TBK',
    '.tag', '.sys', '.ss', '.spx', '.spx', '.spr', '.sms',
    '.shx', '.shx', '.shs', '.inf', '.settings', '.sdf',
    '.scx', '.scv', '.scc', '.scc', '.rul',
    '.sct', '.obj', '.apl', '.bin', '.bkf', '.c01',
    '.c02', '.cdm', '.cshtml', '.html', '.cnt', '.chw',
    '.cnt', '.cps', '.ctl', '.dbc', '.dca', '.dif',
    '.dos', '.dsr', '.dsx', '.dtf', '.dtt', '.dwg', '.err',
    '.esl', '.eso', '.gif', '.icon', 'pdf', '.mmb', '.mmx',
    '.mpp', '.mso', '.par', '.pdm', '.pll', '.plx', '.png',
    '.htm', '.h', '.cpp', '.chm', '.ini', 'cfg',
    '.dbd', '.dct', '.ddf', '.dgn', '.de', '.dict', '.dis',
    '.doc-1', '.ex_', '.def', '.fs', '.jpg', '.flt', '.b~k',
    '.fbm', '.fmp', '.fmx', '.fnt', '.pdf', '.fp', '.31447144',
    '.cfg', '.db', '.xsc', '.dcx', '.', '.fmb', '.fdf',
    '.fpt', '.frm', '.frt', '.frx', '.fxd', '.fxp', '.gid',
    '.hdr', '.ico', '.icon', '.idx', '.ins', '.int', '.ion', '.jpeg',
    '.latex', '.lid', '.lim', '.hlp', '.hpj', '.htc', 'inc',
    '.mak', '.manifest', '.ist', '.mcs', '.mdi', '.mem',
    '.dmp', '.mib', '.resx', '.odc', '.xml', '.xlsm', '.slk',
    '.xlt', '.one', '.ppa', '.ppt', '.pps', '.pot', '.pptx',
    '.pub', '.doc', '.docx', '.dot', '.sql', '.vst', '.wbk',
    '.mid', '.mmm', '.mnt', '.mnx', '.mor', '.mp3', '.xss', '.inc',
    '.cls', '.lst', '.svg', '.ppsx', '.vsd', '.mpr', '.mpx',
    '.ms', '.mswmm', '.nap', '.nrg', '.lib', '.ogd', '.oldcdx',
    '.msg', '.ovl', '.ovr', '.pfx', '.user', '.pfb', '.php',
    '.pjt', '.pjx', '.pms', '.plc', '.prg', '.pdb',
    '.prt', '.psd', '.qpr', '.rdf', '.rep', '.vbp', '.rpt', '.rtf',
    '.mht', '.vss', '.mpeg', '.mpg', '.pls', '.reg', '.pmc', '.provision',
    '.rdp', '.rc', '.resources', '.rc2', '.txt', '.lnk', '.dic',
    '.flv', '.xlsx', '.csv', '.xls', '.asp', '.aspx', '.master',
    '.ascx', '.config', '.builder', '.cd', '.ascx', '.aspx', '.asax',
    '.cgi', '.class', '.compiled', '.data', '.datasource', '.enc', '.erd',
    '.fcgi', '.fct', '.fky', '.fll', '.force', '.fox', '.fpc', '.fpq', '.htaccess',
    '.ibs', '.java', '.lastcodeanalysissucceeded', '.lbt', '.lbx', '.lng',
    '.mf', '.msk', '.nupkg', '.nuspec', '.o', '.perl', '.plb', '.prc', '.yaml',
    '.xsl', '.psm1', '.ps1', '.wsdl', '.svc', '.war', '.vol', '.map', '.yml',
    '.qpx', '.r935', '.r1118', '.rdlc', '.rid', '.rgn', '.htaccess',
    '.jsp', '.com', '.pp', '.pubxml', '.rb', '.sch'
]




# Recursively delete files with unwanted extensions in the specified root directory and its subdirectories.
def clean_directory_recursively(root_directory, unwanted_extensions):  
    # Ensure the root directory exists
    if not os.path.isdir(root_directory):
        print(f"The directory {root_directory} does not exist.")
        return

    # Walk through all directories and subdirectories
    for dirpath, dirnames, filenames in os.walk(root_directory):
        for filename in filenames:
            # Construct full file path
            file_path = os.path.join(dirpath, filename)

            # Get the file extension
            _, ext = os.path.splitext(filename)
            if ext.lower() in unwanted_extensions:
                try:
                    # Remove the file
                    os.remove(file_path)
                    print(f"Deleted: {file_path}")
                except Exception as e:
                    print(f"Error deleting {file_path}: {e}")





# unzip all zip files recursively
def unzip_directory_recursively(directory):
    # Walk through the directory recursively
    for root, dirs, files in os.walk(directory):
        for file in files:
            if file.endswith(".zip"):  # Check if the file is a ZIP file
                file_path = os.path.join(root, file)  # Get the full path of the file
                print(f"Unzipping: {file_path}")

                try:
                    # Unzip the file
                    with zipfile.ZipFile(file_path, 'r') as zip_ref:
                        zip_ref.extractall(root)  # Extract all files to the current directory
                        print(f"Extracted: {file_path}")

                    # Delete the ZIP file after extraction
                    os.remove(file_path)
                    print(f"Deleted: {file_path}")

                except (zipfile.BadZipFile, Exception) as e:
                    # If extraction fails, delete the file
                    print(f"Failed to unzip: {file_path} due to {e}")
                    os.remove(file_path)
                    print(f"Deleted after failure: {file_path}")





# delete all empty folder
def delete_empty_folders(directory):
    # Walk through the directory from bottom to top
    for root, dirs, files in os.walk(directory, topdown=False):
        for dir_name in dirs:
            dir_path = os.path.join(root, dir_name)
            # Check if the directory is empty
            if not os.listdir(dir_path):
                os.rmdir(dir_path)  # Delete the empty directory
                print(f"Deleted empty folder: {dir_path}")




# Function to recursively find all DBF files in a directory
def find_dbf_files(directory):
    dbf_files = []
    for root, _, files in os.walk(directory):
        for file in files:
            if file.lower().endswith('.dbf'):
                dbf_files.append(os.path.join(root, file))
    return dbf_files




# Function to read DBF file and return DataFrame and header
def read_dbf_to_dataframe(dbf_file):
    dbf_data = DBF(dbf_file, encoding='utf-8')
    df = pd.DataFrame(iter(dbf_data))
    header = tuple(df.columns)  # Convert header to a tuple to use as a dictionary key
    return df, header



# Function to group DBF files by their headers and merge them
def group_and_merge_dbf_files(directory):
    global counter
    dbf_files = find_dbf_files(directory)
    header_groups = defaultdict(list)    

    # Group DBF files by headers
    for dbf_file in dbf_files:
        try:
            df, header = read_dbf_to_dataframe(dbf_file)
            if 'MEM_SUB_MN' in header:
                header_groups[header].append(df)
                print(f"Processed {dbf_file} with header {header}")
        except Exception as e:
            print(f"Error processing {dbf_file}: {e}")

    # Merge files with the same headers and save to CSV
    for header, df_list in header_groups.items():
        # merge all of same type
        merged_df = pd.concat(df_list, ignore_index=True)
        # drop duplicates
        cleaned_df = merged_df.drop_duplicates()
        # Create a filename based on the headers
        output_csv_file = f'merged_output_{counter}.csv'
        output_csv_cleaned_file = f'merged_output_clean_{counter}.csv'
        counter = counter + 1
        merged_df.to_csv(output_csv_file, index=False)
        cleaned_df.to_csv(output_csv_cleaned_file, index=False)
        print(f"Merged files with header {header} into {output_csv_file}")




# unrar all files
def unrar_files_in_directory(directory, output_dir=None):    
    # Walk through the directory and its subdirectories
    for root, _, files in os.walk(directory):
        for file in files:
            if file.endswith('.rar'):
                rar_path = os.path.join(root, file)
                extract_to = output_dir if output_dir else root
                
                try:
                    print(f"Extracting {rar_path} to {extract_to}...")
                    with rarfile.RarFile(rar_path) as rf:
                        rf.extractall(extract_to)
                    print(f"Extracted: {rar_path}")
                    
                    # Delete the rar file after extraction
                    os.remove(rar_path)
                    print(f"Deleted: {rar_path}")
                    
                except rarfile.RarCannotExec as e:
                    print(f"Unrar executable not found or not working: {e}")
                    # Delete the rar file after extraction
                    os.remove(rar_path)
                    print(f"Deleted: {rar_path}")
                except rarfile.Error as e:
                    print(f"Error extracting {rar_path}: {e}")
                    # Delete the rar file after extraction
                    os.remove(rar_path)
                    print(f"Deleted: {rar_path}")



# clean unwanted file types
# clean_directory_recursively(data_dir, unwanted_file_types)





# unzip directory recursively and delete it
# unzip_directory_recursively(data_dir)


# unrar all files
# unrar_files_in_directory(data_dir)



# merge all mdf into one (group by same types of header)
group_and_merge_dbf_files(data_dir)





input_char = input("Ready to exit. Input a char to exit ")
