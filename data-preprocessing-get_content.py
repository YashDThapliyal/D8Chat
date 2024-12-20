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


toc_path = "/Users/yash/Documents/Data-8-ChatBot/D8Chat/textbook-main/_toc.yml"
toc = load_book_structure(toc_path)
print(toc)  
