# Context manager (generator)

from contextlib import contextmanager

@contextmanager
def file_manager(file_path, mode):
    """
    A generator-based context manager for file handling.
    
    :param file_path: file path
    :param mode: mode of operation
    """
    f = None
    try:
        f = open(file_path, mode)
        yield f # the code in the 'with' block run here
    except Exception as e:
        print(f"An exception occured: {e}")
    finally:
        if f:
            f.close()
            print("File closed automatically")

with file_manager("test.txt", "w") as my_file:
    my_file.write("Decorated file write")