def read_file(path):
    arr = []
    with open(path, "r") as file:
        for line in file:
            arr.append(line.rstrip())
    return arr


if __name__ == "__main__":
    # space reserved for testing
    arr = [1, 2, 23, 4, "adgf"]
    [print(a) for a in arr]
