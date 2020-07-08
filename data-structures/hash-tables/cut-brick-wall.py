from collections import defaultdict

wall = [[3, 5, 1, 1],
[2, 3, 3, 2],
[5, 5],
[4, 4, 2],
[1, 3, 3, 3],
[1, 1, 6, 1, 1]]

def fewest_cuts(wall):
    cuts = defaultdict(int)

    for row in wall:
        length = 0
        for brick in row[:-1]:
            length += brick
            cuts[length] += 1
        print(length)
    return len(wall) - max(cuts.values())

print(fewest_cuts(wall))
