def main():
    with open('input.txt', 'r') as f:
        words = f.readlines()

    sum = 0
    for word in words:
        sum += 10 * get_first_digit(word) + get_last_digit(word)
    print(sum)
    exit(0)

def get_first_digit(word):
    for char in word:
        if char in '1234567890':
            return int(char)
    return 0

def get_last_digit(word):
    for char in word[::-1]:
        if char in '1234567890':
            return int(char)
    return 0

if __name__ == '__main__':
    main()
