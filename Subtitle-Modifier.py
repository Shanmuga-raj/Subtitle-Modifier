def read_file(filename):
    with open(filename, "r", encoding="utf8") as file:
        content = []
        for lines in file:
            line = lines.split()
            if line[:] == []:
                content.append(['\n'])
            elif line[0].isdigit():
                pass
            else:
                content.append(line)
    update_file(filename, content)


def update_file(filename, content):
    with open(filename, "w+", encoding="utf8") as new_file:
        for words in content:
            editedfile = " ".join(words)
            if editedfile != "\n":
                editedfile += "\n"
            new_file.write(editedfile)


def subtitle():
    end = int(input("How many files: "))
    filenames = []
    for i in range(end):
        filenames.append(input("Enter file name: "))
    for filename in range(len(filenames)):
        read_file(filenames[filename]+".srt")


subtitle()