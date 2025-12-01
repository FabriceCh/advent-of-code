def read_file(path):
    arr = []
    with open(path, "r") as file:
        for line in file:
            arr.append(line.rstrip())
    return arr



