import os
import shutil

def copy_files(source_dir, destination_dir):
    if not os.path.exists(destination_dir):
        os.makedirs(destination_dir)

    for root, dirs, files in os.walk(source_dir):
        for file in files:
            if file.endswith(('.md', '.ipynb')):
                file_path = os.path.join(root, file)
                shutil.copy2(file_path, destination_dir)
                print(f"Copied: {file}")


source_directory = '/Users/yash/Documents/Data-8-ChatBot/D8Chat/textbook-main/chapters'  
destination_directory = './databook'  


copy_files(source_directory, destination_directory)