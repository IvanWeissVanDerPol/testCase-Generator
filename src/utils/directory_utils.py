import os

def ensure_directory_exists(path):
    """Ensure that the given directory path exists."""
    if not os.path.exists(path):
        os.makedirs(path)
