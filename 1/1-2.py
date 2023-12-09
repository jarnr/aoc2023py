
def main():
    with open('input.txt', 'r') as f:
        lines = [line.strip() for line in f.readlines()]
    
    sum = 0
    for line in lines:
        sum += get_value(line)

    print(sum)

def get_value(line):
    first = get_first_num(line)
    last = get_last_num(line[::-1])
    
    print(f"First: {first}    Last: {last}    Total: {10 * first + last}")
    return 10 * first + last

def get_first_num(line):
    ll = len(line)
    if ll == 0:
        return 0

    s = line[0]
    t = line[0:3] if ll > 2 else line
    u = line[0:4] if ll > 3 else line
    v = line[0:5] if ll > 4 else line

    if s == "1":
        return 1
    elif s == "2":
        return 2
    elif s == "3":
        return 3
    elif s == "4":
        return 4
    elif s == "5":
        return 5
    elif s == "6":
        return 6
    elif s == "7":
        return 7
    elif s == "8":
        return 8
    elif s == "9":
        return 9

    if t == "one":
        return 1
    elif t == "two":
        return 2
    elif t == "six":
        return 6

    if u == "four":
        return 4
    elif u == "five":
        return 5
    elif u == "nine":
        return 9

    if v == "three":
        return 3
    elif v == "seven":
        return 7
    elif v == "eight":
        return 8

    return get_first_num(line[1:])

def get_last_num(line):
    ll = len(line)
    if ll == 0:
        return 0

    s = line[0]
    t = line[0:3] if ll > 2 else line
    u = line[0:4] if ll > 3 else line
    v = line[0:5] if ll > 4 else line

    if s == "1":
        return 1
    elif s == "2":
        return 2
    elif s == "3":
        return 3
    elif s == "4":
        return 4
    elif s == "5":
        return 5
    elif s == "6":
        return 6
    elif s == "7":
        return 7
    elif s == "8":
        return 8
    elif s == "9":
        return 9

    if t == "eno":
        return 1
    elif t == "owt":
        return 2
    elif t == "xis":
        return 6

    if u == "ruof":
        return 4
    elif u == "evif":
        return 5
    elif u == "enin":
        return 9

    if v == "eerht":
        return 3
    elif v == "neves":
        return 7
    elif v == "thgie":
        return 8

    return get_last_num(line[1:])

if __name__ == '__main__':
    main()
