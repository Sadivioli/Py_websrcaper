import os

# printer function
def printer(array):
    for index, val in enumerate(array):
        print(index, val + "\n")

def save_to_file(array, file_name):
    if os.path.isfile(file_name):
        # If the file exists, read its current contents and get only unique new elements
        with open(file_name, "r") as file:
            current_contents = file.read().splitlines()
        new_contents = list(set(array) - set(current_contents))
    else:
        # If the file doesn't exist, just use the entire array as new contents
        new_contents = array

    # Write the new contents to the file
    with open(file_name, "w") as file:
        for item in new_contents:
            file.write(item + "\n")

def read_file_contents(file_path):
    with open(file_path, 'r') as f:
        lines = f.readlines()
        return "<br>".join(lines)

#!Important, prefix those values with a comma
#? on bulldog format in url requries a format like [variable],[value] - providing string like for ex. experienceLevel, will result in this filter being an empty string and no results will be found. but experienceLevel will not add experienceLevel as a filter
#function to concat "," to string
def concat(string):
    return ","+string

def concatenate_and_save_files(file1, file2, file3, output_file):
    with open(file1, "r") as f1, open(file2, "r") as f2, open(file3, "r") as f3:
        contents = f1.read() + f2.read() + f3.read()
    
    with open(output_file, "w") as output:
        output.write(contents)
        
    print(f"Wszystkie oferty zostały zapisane do pliku: {output_file}.")

#function to delete files with given names, those will be files that are not needed anymore
def delete_files(*args):
    for file in args:
        if os.path.isfile(file):
            os.remove(file)
            print(f"Usunięto plik: {file}.")
        else:
            print(f"Nie znaleziono pliku: {file}.")
    print("Pliki tymczasowe zostały usunięte.")