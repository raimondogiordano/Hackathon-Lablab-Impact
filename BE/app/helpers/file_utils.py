import sys
import os
import shutil
import io

# create file contents function
def create_file(file, destination):
    with open(destination, "wb") as buffer:
        shutil.copyfileobj(file, buffer)

# copy file function
def copy_file(source, destination):
    shutil.copy(source, destination)

# delete file function
def delete_file(file_to_delete):
    if os.path.exists(file_to_delete):
        os.remove(file_to_delete)             
    else:
        raise Exception("File not found.")

# rename file function
def rename_file(file_name, new_name):
    source_path = os.path.dirname(file_name)
    extension = os.path.splitext(file_name)[1]

    path = os.path.join(source_path, new_name)
    os.rename(file_name, path)

# move file function
def move_file(source, destination):
    if(source==destination):
        raise Exception("Source and destination are same.")
    else:
        shutil.move(source, destination)  

# rename folder function
def rename_folder(folder_name, new_name):
    source_path = os.path.dirname(folder_name)

    path = os.path.join(source_path, new_name)
    os.rename(folder_name, path)

# function to check a folder
def check_folder(path):
    return os.path.exists(path)

def make_folder(path):
    if os.path.exists(path):
        raise Exception("Folder already present.")
    else:
        #os.mkdir(path)
        os.makedirs(path, exist_ok=True)

# function to remove a folder
def remove_folder(folder_to_delete):
    if os.path.exists(folder_to_delete):
        shutil.rmtree(folder_to_delete)
        os.rmdir(folder_to_delete)
    else:
        raise Exception("Folder not found.")

# function to remove a folder recursively
def remove_recursive_folder(path):
    if os.path.exists(path):
        for root, dirs, files in os.walk(path, topdown=False):
            for name in files:
                file_path = os.path.join(root, name)
                os.remove(file_path)
            for name in dirs:
                dir_path = os.path.join(root, name)
                os.rmdir(dir_path)
        os.rmdir(path)

# function to remove a folder recursively
def clear_folder(path):
    if os.path.exists(path):
        for root, dirs, files in os.walk(path, topdown=False):
            for name in files:
                file_path = os.path.join(root, name)
                os.remove(file_path)
            for name in dirs:
                dir_path = os.path.join(root, name)
                os.rmdir(dir_path)

# function to list all the files in folder
def list_files(folder):
    if os.path.exists(folder):
        return sorted(os.listdir(folder))       
    else:
        raise Exception("Folder not found.")

def check_extension(file_name, extension_list_string):
    # Converte la stringa della lista di estensioni in una lista di estensioni
    extension_list = extension_list_string.split(',')
    
    # Ottiene l'estensione del file
    file_extension = file_name.split('.')[-1]
    
    # Controlla se l'estensione del file è presente nella lista di estensioni
    if file_extension in extension_list:
        return True
    else:
        return False
def open_file(name):
    base=os.environ["BASE_FOLDER_PATH"]
    full_path=os.path.join(base,name)
    try:
        with open(full_path, 'rb') as file:
            audio_data = file.read()
            return audio_data
    except IOError as e:
        print("Errore durante l'apertura del file:", e)