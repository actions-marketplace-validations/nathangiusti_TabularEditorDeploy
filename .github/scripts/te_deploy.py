import os
from pathlib import Path
import sys
import urllib.request
import zipfile


def main():

    arg_list = []

    file_string = sys.argv[1]
    file_list = file_string.split(',')
    for file in file_list:
        print(file)


    # Download Tabular Editor Portable, extract, and delete zip file
    cwd = os.getcwd()
    zip_location = cwd + "\TabularEditor.zip"
    unzip_location = cwd + "\TabularEditor.exe"
    urllib.request.urlretrieve("https://cdn.tabulareditor.com/files/te2/TabularEditor.Portable.zip", cwd + "\TabularEditor.zip")

    with zipfile.ZipFile(zip_location, 'r') as zip_ref:
        zip_ref.extractall(cwd)

    os.remove(zip_location)
    
    # Find all modified datasets
    updated_datasets = []
    for file in sys.argv:
        if os.path.exists(file):
            path = Path(file)
            dataset = workspace = os.path.basename(path.parent.absolute())
            if dataset not in updated_datasets:
                updated_datasets.append(dataset)
    
    print(updated_datasets)

    # os.system()

if __name__ == "__main__":
    main()