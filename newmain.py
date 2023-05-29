import itertools


def generate_combinations(length):
    letters_and_digits = 'abcdefghijklmnopqrstuvwxyz0123456789'
    for combo in itertools.product(letters_and_digits, repeat=length):
        yield ''.join(combo)


if __name__ == '__main__':
    with open('combinations.txt', 'w') as f:
        for combo in generate_combinations(3):
            f.write('www.' + combo + '.zip:80;\n')
            f.write('www.' + combo + '.mov:25565;\n')
