def main():
    MAX_CUBES = {
        'red': 12,
        'green': 13,
        'blue': 14
    }

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

    score = 0
    for i in range(len(games)):
        game_is_possible = True
        for bag in games[i]:
            for color in MAX_CUBES:
                if color in bag and bag[color] > MAX_CUBES[color]:
                    game_is_possible = False
                    break
            if not game_is_possible:
                break
        if game_is_possible:
            score += i+1

    print(score)

if __name__ == "__main__":
    main()
