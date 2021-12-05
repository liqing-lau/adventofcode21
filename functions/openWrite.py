def open_file_int(filename):
    result = []
    with open(filename) as datafile:
        for line in datafile:
            result.append(int(line.strip()))
        return result

def open_file(filename):
    result = []
    with open(filename) as datafile:
        for line in datafile:
            result.append(line.strip())
        return result

def write_to_file(filename, lines):
    with open(filename, 'w') as datafile:
        for a_line in lines:
            datafile.write(f'{a_line}\n')