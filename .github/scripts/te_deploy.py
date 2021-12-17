import os
from pathlib import Path
import sys
import urllib.request
import zipfile
import argparse

def main():

    parser = argparse.ArgumentParser()
    parser.add_argument("--tenant_id", nargs = 1)
    parser.add_argument("--db_url", nargs = 1)
    parser.add_argument("--files", nargs = 1)
    args = parser.parse_args()
    
    tenant_id = args.tenant_id
    db_url = args.db_url
    files = args.files

    client_id = os.environ['CLIENT_ID']
    client_secret = os.environ['CLIENT_SECRET']
    

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
    
    # Post datasets to workspace
    for dataset in updated_datasets:
        run_str = "TabularEditor.exe .\{} -D \"Provider=MSOLAP;Data Source={};User ID=app:{}@{};Password={}\" {} -O -C -G -E -W"\
            .format(dataset, db_url, client_id, tenant_id, client_secret, dataset)
        os.system(run_str)
        print("Deployed {}".format(dataset))


if __name__ == "__main__":
    main()