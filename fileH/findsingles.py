

with open('files_found.txt') as oldfile, open('file_multiples.txt', 'w') as newfile:
    for line in oldfile:
        if "," in line:
            newfile.write(line)
