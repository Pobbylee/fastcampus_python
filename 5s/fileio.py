import os

with open(os.path.join(os.getcwd(), 'lipsum.txt'), 'r+') as f:
    read_file = f.read()

print read_file
