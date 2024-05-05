todelete = []
with open('output.txt','r') as f:
    for line in f:
        if line.startswith('\run'):
            todelete.append(line.strip())
        