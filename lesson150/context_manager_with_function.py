from contextlib import contextmanager

@contextmanager
def my_open(file_path, mode):
    try:
        print('Opening file')
        file = open(file_path, mode, encoding='utf8')
        yield file  # Pass the file object to the with block
    except Exception as e:
        print('An error occurred:', e)
    finally:
        print('Closing file')
        file.close()
