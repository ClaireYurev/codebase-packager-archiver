import os

def read_gitignore():
    gitignore_files = set()
    try:
        with open(".gitignore", "r", encoding="utf-8") as gitignore:
            for line in gitignore:
                line = line.strip()
                if line and not line.startswith("#"):
                    gitignore_files.add(line)
    except FileNotFoundError:
        pass
    return gitignore_files

def should_exclude(path):
    return path.endswith(".py")  # Exclude only Python files

def get_unique_output_filename(base_name):
    for i in range(1000):
        if i == 0:
            filename = base_name
        else:
            filename = f"{os.path.splitext(base_name)[0]}-{i}{os.path.splitext(base_name)[1]}"
        if not os.path.exists(filename):
            return filename
    print("Max output file limit reached! Overwrote output-1.rtf")
    return f"{os.path.splitext(base_name)[0]}-1{os.path.splitext(base_name)[1]}"

def scan_and_write_to_rtf(output_file):
    scanned_files = []

    output_file = get_unique_output_filename(output_file)

    with open(output_file, "w", encoding="utf-8") as rtf_file:
        for root, dirs, files in os.walk(os.getcwd()):
            for file in files:
                file_path = os.path.join(root, file)
                relative_path = os.path.relpath(file_path, os.getcwd())

                if should_exclude(file_path):
                    continue

                try:
                    with open(file_path, "r", encoding="utf-8") as f:
                        contents = f.read()

                    # Write to the .rtf file in the specified format
                    rtf_file.write(f"// Contents of \"{relative_path}\"\n")
                    rtf_file.write(contents)
                    rtf_file.write("\n\n")

                    # Add to scanned files list
                    scanned_files.append(relative_path)
                except (UnicodeDecodeError, PermissionError) as e:
                    print(f"Skipping file {relative_path} due to error: {e}")

    # Print scanned files to console
    for scanned_file in scanned_files:
        print(f"Scanned and added: {scanned_file}")

    # Print summary
    print(f"Scanned and added {len(scanned_files)} files to {output_file}.")

if __name__ == "__main__":
    output_filename = "output.rtf"
    scan_and_write_to_rtf(output_filename)
    print(f"All contents written to {output_filename}.")
