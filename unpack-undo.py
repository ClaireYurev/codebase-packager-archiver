import os

def delete_files_from_input(input_file):
    with open(input_file, 'r') as file:
        lines = file.readlines()

    for line in lines:
        # Check if the line specifies a file path
        if line.startswith("// "):
            file_path = line[3:].strip()  # Remove "// " and strip whitespace
            delete_file(file_path)

def delete_file(file_path):
    if os.path.exists(file_path):
        # Delete the file
        os.remove(file_path)
        print(f"Deleted file: {file_path}")

        # Remove empty parent directories
        remove_empty_directories(os.path.dirname(file_path))
    else:
        print(f"File not found: {file_path}")

def remove_empty_directories(directory):
    # Recursively remove empty directories
    while directory and os.path.exists(directory) and not os.listdir(directory):
        os.rmdir(directory)
        print(f"Deleted empty directory: {directory}")
        directory = os.path.dirname(directory)

if __name__ == "__main__":
    input_file = "input_text.txt"  # Replace with your file name if different
    delete_files_from_input(input_file)
