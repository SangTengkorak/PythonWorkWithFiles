def print_content():
    with open("Lab/automobile.csv", 'r') as f:
        contents = f.read()
        print(contents)


def write_new_content():
    with open("Lab/automobile.csv", 'w') as f:
        f.write("Alhamdulillah")


if __name__ == "__main__":
    write_new_content()
    print_content()
