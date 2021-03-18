import random, string

min_length = 3
max_length = 18
max_num_length = 10 ** max_length
blank = ''
space = ' '
separator = ','
decimal_point = '.'
alphabet = string.ascii_letters
number = string.digits + '0'
alphanumeric = alphabet + number

def get_random_integer(start=1, end=max_length):
    """
    Get random integer given an optional start and end
    """
    return random.randint(start, end)

def get_random_char(option, length):
    """
    Get random string given option and length
    """
    return blank.join(random.choices(option, k=length))

def get_random_num():
    """
    Get random number string
    """
    return get_random_char(number, get_random_integer())

def get_spaces():
    """
    Get random spaces
    """
    num = get_random_integer(end=10)
    return space * num

def get_alphabet():
    """
    Get random alphabet string
    """
    return get_random_char(alphabet, get_random_integer())

def get_real_numbers():
    """
    Get random real number
    Decimal point location is random
    """
    num = get_random_num()
    id = get_random_integer(0, len(num) - 1)
    real_num = num[:id - 1] + decimal_point + num[id:]
    return float(real_num)

def get_integers():
    """
    Get random integer
    """
    return int(get_random_num())

def get_alphanumeric():
    """
    Get random alphanumeric string
    """
    s = get_random_char(alphanumeric, get_random_integer())
    return get_spaces() + s + get_spaces()

def get_random_func():
    """
    Get random function from array
    """
    funcs = [
        get_alphabet,
        get_real_numbers,
        get_integers,
        get_alphanumeric
    ]
    id = get_random_integer(start=0, end=len(funcs) - 1)
    return funcs[id]()

def create_file(filename, size):
    """
    Create file given a filename
    """
    f = open(filename, "w")
    for i in range(size):
        if i + 1 == size:
            f.write(str(get_random_func()))
        else:
            f.write(str(get_random_func()) + separator)
    f.close()

if __name__ == "__main__":
    print("Start")
    filename = "sample.txt"
    size = 10 ** 6
    create_file(filename, size)
    print("End")
