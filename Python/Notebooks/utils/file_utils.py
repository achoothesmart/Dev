def read_file(file_path):
    """Reads the entire content of a file."""
    try:
        with open(file_path, 'r') as file:
            return file.read()
    except FileNotFoundError:
        return f"The file '{file_path}' was not found."