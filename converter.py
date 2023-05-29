with open('new.txt', 'w') as f:
    for line in open('combinations.txt', 'r').readlines():
        f.write(f"www.{line}")
