import os

def print_directory_concepts(path='.'):
    """
    Prints entries in the given directory, classifying them as files or directories.
    """
    try:
        entries = os.listdir(path)
    except Exception as e:
        print(f"Error accessing directory '{path}': {e}")
        return

    print(f"Contents of directory '{path}':")
    for entry in entries:
        full_path = os.path.join(path, entry)
        if os.path.isfile(full_path):
            print(f"  [FILE] {entry}")
        elif os.path.isdir(full_path):
            print(f"  [DIR]  {entry}")
        else:
            print(f"  [OTHER] {entry}")

if __name__ == "__main__":
    directory = input("Enter directory path (leave blank for current directory): ").strip() or '.'
    print_directory_concepts(directory)
