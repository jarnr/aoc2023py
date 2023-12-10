from functools import reduce
import operator

def main():
    colors = ['red', 'green', 'blue']

    with open('input.txt', 'r') as f:
        lines = [line[line.find(':')+2:].strip() for line in f.readlines()]

    games = []
    for line in lines: 
        game = []
        for group in line.split(';'):
            bag = {}
            for pair in group.split(','):
                s = pair.strip().split(' ')
                k,v = s[1], int(s[0])
                bag[k] = v
            game.append(bag)
        games.append(game)

    # Original way
    #score = 0
    #for game in games:
    #    maxes = [max(bag.get(color, 1) for bag in game) for color in colors]
    #    power = reduce(operator.mul, maxes, 1)
    #    score += power

    # Stupid golfy way
    score = sum([reduce(operator.mul, [max(bag.get(color, 1) for bag in game) for color in colors], 1) for game in games])

    print(score)

if __name__ == "__main__":
    main()
