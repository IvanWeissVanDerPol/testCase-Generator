import os
import json

def merge_python_files(startpath, output_file, exclude_paths=None, exclude_files=None, extensions=None, include_config_env=False):
    """
    Traverse through the directory tree and merge contents of specified file types into a JSON file, excluding certain files and paths.
    
    :param startpath: The root directory to start scanning.
    :param output_file: The output JSON file where the merged content will be stored.
    :param exclude_paths: A list of directories to exclude from scanning.
    :param exclude_files: A list of file names to exclude.
    :param extensions: A list of file extensions to include (e.g., ['.py', '.json']).
    :param include_config_env: Whether to include config.json and .env file contents in the output.
    """
    if exclude_paths is None:
        exclude_paths = []
    if exclude_files is None:
        exclude_files = ['__init__.py', 'merge_python_files.py', 'rate_limiter.py', 'tree_view.py', 'merged_python_files.json']
    if extensions is None:
        extensions = ['.py', '.json']  # Default to Python and JSON files

    merged_files = {}

    # Normalize the exclude paths
    exclude_paths = [os.path.normpath(path) for path in exclude_paths]

    for root, dirs, files in os.walk(startpath):
        # Exclude specified directories
        dirs[:] = [d for d in dirs if os.path.join(root, d) not in exclude_paths]

        for file in files:
            # Skip excluded files and ensure Markdown files are excluded
            if file in exclude_files or file.endswith('.md'):
                continue
            # Check if the file has the desired extension or if config/env files should be included
            if any(file.endswith(ext) for ext in extensions) or (include_config_env and (file == '.env' or file == 'config.json')):
                file_path = os.path.join(root, file)
                try:
                    with open(file_path, 'r', encoding='utf-8') as f:
                        content = f.read()
                        # Store the relative path and content
                        relative_path = os.path.relpath(file_path, startpath)
                        merged_files[relative_path] = content
                except Exception as e:
                    print(f"Error reading file {file_path}: {e}")

    # Write the merged content to a JSON file
    with open(output_file, 'w', encoding='utf-8') as outfile:
        json.dump(merged_files, outfile, indent=4, ensure_ascii=False)
    
    print(f"Python files and selected config/env files merged and saved to {output_file}")

# Example usage
if __name__ == "__main__":
    # Set the project root directory to the current working directory
    root_directory = os.getcwd()
    
    # List of directories to exclude
    exclude = [
        os.path.join(root_directory, '.venv'),
        os.path.join(root_directory, '__pycache__')
    ]
    
    # Output JSON file
    output_json = os.path.join(root_directory, 'debug_files\merged_python_files.json')
    
    # Merge Python files into the JSON file, excluding specified files and paths, and including config and .env
    merge_python_files(root_directory, output_json, exclude_paths=exclude, exclude_files=['__init__.py', 'merge_python_files.py', 'rate_limiter.py', 'tree_view.py'], extensions=['.py', '.json'], include_config_env=True)
