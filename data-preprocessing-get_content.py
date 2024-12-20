import yaml

def load_book_structure(toc_path):
    """
    Load the table of contents (TOC) from a Jupyter Book's `_toc.yml` file.
    Args:
        toc_path (str): Path to the `_toc.yml` file.
    Returns:
        dict: Parsed TOC structure as a Python dictionary.
    """
    with open(toc_path, 'r') as file:
        toc = yaml.safe_load(file)
    return toc

def read_markdown(file_path):
    """
    Reads and returns the content of a Markdown file.
    Args:
        file_path (str): Path to the markdown file.
    Returns:
        str: File content as a string.
    """
    try:
        with open(file_path, 'r', encoding='utf-8') as file:
            return file.read()
    except FileNotFoundError:
        return f"File not found: {file_path}"


if __name__ == "__main__":
    toc_path = "/Users/yash/Documents/Data-8-ChatBot/D8Chat/textbook-main/_toc.yml"
    toc = load_book_structure(toc_path)
    print(toc)  
