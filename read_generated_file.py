import csv


def get_type(value):
    """
    Get type given a value
    """
    alphabet = 'alphabetical strings'
    real_numbers = 'real numbers'
    integer = 'integer'
    alphanumeric = 'alphanumeric'

    if value.isalpha():
        return alphabet
    elif value.isdigit():
        return integer
    elif value.isalnum():
        return alphanumeric

    try:
        real_num = float(value)
        return real_numbers
    except ValueError:
        return 'Error'

    return 'Error'

def read_file(filename):
    """
    Read file given a filename
    """
    with open(filename) as csv_file:
        csv_reader = csv.reader(csv_file)
        for row in csv_reader:
            for value in row:
                trim_value = value.strip()
                result = trim_value + ' - ' + get_type(trim_value)
                print(result)

if __name__ == "__main__":
    filename = "sample.txt"
    read_file(filename)
