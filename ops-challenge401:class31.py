import os

def search_files(file_name, search_directory):
    files_searched = 0
    hits_found = 0

    for root, dirs, files in os.walk(search_directory):
        for file in files:
            files_searched += 1
            if file == file_name:
                hits_found += 1
                print(f"Found: {file} in {root}")

    print(f"Files searched: {files_searched}")
    print(f"Hits found: {hits_found}")

if __name__ == "__main__":
    file_name_to_search = input("Enter file name to search for: ")
    directory_to_search = input("Enter directory to search in: ")

    if os.path.isdir(directory_to_search):
        search_files(file_name_to_search, directory_to_search)
    else:
        print("Directory does not exist.")