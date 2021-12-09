def print_file_content():
    with open('Lab/automobile.csv', 'r') as f:
        print(f.read(10))  # Read only specific bytes of the file content


def print_file_content_readlines():
    with open('Lab/voucher.py', 'r') as f:
        lines = f.readlines()
        print(lines[0])


def print_file_content_one_line_at_time():
    with open('Lab/voucher.py', 'r') as f:
        line = f.readline()
        while line != '':
            print(line, end='')
            line = f.readline()


if __name__ == "__main__":
    print_file_content_one_line_at_time()
