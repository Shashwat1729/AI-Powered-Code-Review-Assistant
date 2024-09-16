import os

# Function to extract code from a file (assumes the file is a Python script for now)
def extract_code_from_file(file_path):
    _, file_extension = os.path.splitext(file_path)
    if file_extension.lower() in ['.py', '.js', '.java', '.cpp']:
        with open(file_path, 'r') as file:
            return file.read()
    else:
        return "Unsupported file type."
