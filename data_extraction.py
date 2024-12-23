import os
import json
import nbformat

def read_markdown_file(file_path):
    with open(file_path, 'r', encoding='utf-8') as file:
        return file.read()

def extract_all_from_notebook(file_path):
    with open(file_path, 'r', encoding='utf-8') as file:
        notebook = nbformat.read(file, as_version=4)
    
    content = ""
    for cell in notebook.cells:
        if cell.cell_type == 'markdown':
            content += f"[MARKDOWN]\n{cell.source}\n\n"
        elif cell.cell_type == 'code':
            content += f"[CODE]\n{cell.source}\n"
            if cell.outputs:
                content += "[OUTPUT]\n"
                for output in cell.outputs:
                    if 'text' in output:
                        content += output['text'] + "\n"
                    elif 'data' in output:
                        if 'text/plain' in output['data']:
                            content += output['data']['text/plain'] + "\n"
            content += "\n"
    return content

def extract_all_content(directory):
    all_content = ""
    for root, _, files in os.walk(directory):
        for file in files:
            file_path = os.path.join(root, file)
            if file.endswith('.md'):
                all_content += f"[FILE: {file}]\n{read_markdown_file(file_path)}\n\n"
            elif file.endswith('.ipynb'):
                all_content += f"[FILE: {file}]\n{extract_all_from_notebook(file_path)}\n\n"
    return all_content


if __name__ == "__main__":
    data_directory = "/Users/yash/Documents/Data-8-ChatBot/D8Chat/databook"
    extracted_content = extract_all_content(data_directory)
    print(f"Total extracted content length: {len(extracted_content)} characters")
    
    with open("extracted_content.txt", "w", encoding="utf-8") as f:
        f.write(extracted_content)
