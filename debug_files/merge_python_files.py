import os
import json

def merge_files(startpath, output_file_json, output_file_md, exclude_paths=None, exclude_files=None, extensions=None, include_config_env=False):
    """
    Traverse through the directory tree and merge contents of specified file types into a JSON file and a Markdown file, excluding certain files and paths.
    
    :param startpath: The root directory to start scanning.
    :param output_file_json: The output JSON file where the merged content will be stored.
    :param output_file_md: The output Markdown file where the merged .md content will be stored.
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

    merged_files_json = {}
    merged_md_content = ""

    # Normalize the exclude paths
    exclude_paths = [os.path.normpath(path) for path in exclude_paths]

    for root, dirs, files in os.walk(startpath):
        # Exclude specified directories
        dirs[:] = [d for d in dirs if os.path.join(root, d) not in exclude_paths]

        for file in files:
            file_path = os.path.join(root, file)
            # Skip excluded files and ensure test case markdown files are excluded
            if file in exclude_files or file.startswith('TC_') or file.endswith('.test_case.md'):
                continue
            # Handle Python, JSON, and Config/Env files for JSON merging
            if any(file.endswith(ext) for ext in extensions) or (include_config_env and (file == '.env' or file == 'config.json')):
                try:
                    with open(file_path, 'r', encoding='utf-8') as f:
                        content = f.read()
                        # Store the relative path and content in JSON structure
                        relative_path = os.path.relpath(file_path, startpath)
                        merged_files_json[relative_path] = content
                except Exception as e:
                    print(f"Error reading file {file_path}: {e}")

            # Handle Markdown files separately for merging into a single Markdown file
            if file.endswith('.md') and not file.startswith('TC_'):
                try:
                    with open(file_path, 'r', encoding='utf-8') as f:
                        content = f.read()
                        # Append content to the merged markdown file, with a header indicating file name
                        merged_md_content += f"\n\n# {file}\n\n{content}\n"
                except Exception as e:
                    print(f"Error reading Markdown file {file_path}: {e}")

    # Write the merged content to the JSON file
    with open(output_file_json, 'w', encoding='utf-8') as outfile_json:
        json.dump(merged_files_json, outfile_json, indent=4, ensure_ascii=False)
    
    # Write the merged content to the Markdown file
    with open(output_file_md, 'w', encoding='utf-8') as outfile_md:
        outfile_md.write(merged_md_content)
    
    print(f"Python/JSON files merged and saved to {output_file_json}")
    print(f"Markdown files merged and saved to {output_file_md}")


# Example usage
if __name__ == "__main__":
    # Set the project root directory to the current working directory
    root_directory = "C:\\Users\\WEISSIVA\\Downloads\\testCase Generator2\\testCase Generator"
    
    # List of directories to exclude
    exclude = [
        os.path.join(root_directory, '.venv'),
        os.path.join(root_directory, '__pycache__')
    ]
    
    # Output JSON and Markdown files
    output_json = os.path.join(root_directory, 'debug_files\\merged_python_files.json')
    output_md = os.path.join(root_directory, 'debug_files\\merged_markdown_files.md')
    
    # Merge Python, JSON, and Markdown files into the respective output files
    merge_files(root_directory, output_json, output_md, exclude_paths=exclude, exclude_files=['__init__.py', 'merge_python_files.py', 'rate_limiter.py', 'tree_view.py'], extensions=['.py', '.json'], include_config_env=True)
