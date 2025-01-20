import os

def create_files_from_input(input_file):
    with open(input_file, 'r') as file:
        lines = file.readlines()

    current_file_path = None
    file_content = []

    for line in lines:
        # Check if the line specifies a file path
        if line.startswith("// "):
            # Save the content of the previous file
            if current_file_path and file_content:
                save_file(current_file_path, file_content)
            # Reset for the new file
            current_file_path = line[3:].strip()  # Remove "// " and strip whitespace
            file_content = []
        else:
            # Append the line to the current file content
            file_content.append(line)

    # Save the last file
    if current_file_path and file_content:
        save_file(current_file_path, file_content)

def save_file(file_path, content_lines):
    # Ensure the directory exists
    directory = os.path.dirname(file_path)
    if directory and not os.path.exists(directory):
        os.makedirs(directory)

    # Write the content to the file
    with open(file_path, 'w') as file:
        file.writelines(content_lines)
    print(f"Created file: {file_path}")

if __name__ == "__main__":
    input_file = "input_text.txt"  # Replace with your file name if different
    create_files_from_input(input_file)
