import os

def print_directory_tree(startpath, exclude_paths=None, exclude_files=None, exclude_extensions=None, level=0):
    """
    Recursively prints a directory tree starting from 'startpath', excluding paths and files with certain extensions or filenames.
    
    :param startpath: The root directory to start printing the tree.
    :param exclude_paths: A list of paths (folders or files) to exclude from the tree.
    :param exclude_files: A list of filenames to exclude.
    :param exclude_extensions: A list of file extensions to exclude.
    :param level: Internal parameter to track the level of the tree (used for indentation).
    """
    if exclude_paths is None:
        exclude_paths = []
    if exclude_files is None:
        exclude_files = []
    if exclude_extensions is None:
        exclude_extensions = []

    # Normalize the exclude paths
    exclude_paths = [os.path.normpath(path) for path in exclude_paths]
    
    for item in os.listdir(startpath):
        item_path = os.path.join(startpath, item)
        
        # Exclude irrelevant files or folders, such as __pycache__ or others
        if item == '__pycache__' or any(os.path.commonpath([item_path, excluded]) == excluded for excluded in exclude_paths):
            continue

        # Skip files that should be excluded based on name or extension
        if os.path.isfile(item_path):
            if item in exclude_files or any(item.endswith(ext) for ext in exclude_extensions):
                continue

        indent = '│   ' * level + '├── ' if level > 0 else ''
        print(f"{indent}{item}")

        # If it's a folder, recurse into it
        if os.path.isdir(item_path):
            print_directory_tree(item_path, exclude_paths, exclude_files, exclude_extensions, level + 1)

# Example usage
if __name__ == "__main__":
    # Set the project root to the current working directory
    root_directory = os.getcwd()
    
    # List of directories to exclude (including __pycache__)
    exclude = [
        os.path.join(root_directory, '.venv'),        # Exclude .venv folder
        os.path.join(root_directory, '.git'),   # Exclude __pycache__ folder
        os.path.join(root_directory, '__pycache__')   # Exclude __pycache__ folder
    ]
    
    # List of filenames to exclude
    exclude_files = ['__init__.py', 'merge_python_files.py', 'rate_limiter.py', 'tree_view.py']

    # Exclude files with certain extensions
    exclude_extensions = ['.pyc', '.ps1']  # Exclude .pyc and .ps1 files

    print(f"Project Root: {root_directory}")
    print_directory_tree(root_directory, exclude, exclude_files, exclude_extensions)
