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
    for file in file_list:
        if os.path.exists(file):
            path = Path(file)
            dataset = path.parts[0]
            if dataset not in updated_datasets and not dataset.startswith("."):
                updated_datasets.append(dataset)
    
    alchemy_test_url = "powerbi://api.powerbi.com/v1.0/myorg/Alchemy%20Datasets%20%5BTest%5D"
    print(updated_datasets)
    for dataset in updated_datasets:
        run_str = "TabularEditor.exe .\{} -D {} {} -O -C -G -E -W".format(dataset, alchemy_test_url, dataset)
        os.system(run_str)
    # TabularEditor.exe .\AdventureWorks -S ".\Scripts\ReplaceDataSourceConnectionString.csx" -D "%AS_CONNECTIONSTRING%" ValidationDataset -O -C -G -E -W
    # 

    # os.system()

if __name__ == "__main__":
    main()