import os, re

text = re.compile(r'txt')
result = []
os.chdir("./")

for f in os.listdir(os.getcwd()):
    found = text.findall(f)
    if len(found) != 0:
        result.append(os.path.join(os.getcwd(), f))
    
print result
