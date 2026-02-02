# Context manager (class)

class ContexManager:
    def __init__(self):
        print("Init called")
    
    def __enter__(self):
        print("Enter called")
        return self
    
    def __exit__(self, exc_type, exc_value, exc_traceback):
        print("Exit called")
        return True

with ContexManager() as manager:
    print("With statement block")


class FileManager:
    def __init__(self, filename, mode):
        self.filename = filename
        self.mode = mode
        self.file = None

    def __enter__(self):
        self.file = open(self.filename, self.mode)
        return self.file
    
    def __exit__(self, exc_type, exc_value, exc_tarceback):
        print('exc_type, exc_value, exc_tarceback: ', exc_type, exc_value, exc_tarceback)
        self.file.close()

with FileManager("test.txt", "w") as f:
    f.write("test file write\n")
print("Is file closed = ", f.closed)

with FileManager("test.txt", "r") as f:
    for line in f.readlines():
        print(line)
print("Is file closed = ", f.closed)
