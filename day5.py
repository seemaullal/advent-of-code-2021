from collections import Counter

coordinates = []
with open("inputs/day5.txt") as file:
    for line in file.readlines():
        start, end = line.strip().split(" -> ")
        coordinates.append([list(map(int, start.split(","))), list(map(int, end.split(",")))])


def count_passed_multiple_times(include_diagonals: bool):
    seen = Counter()
    passed_more_than_once = 0
    for start, end in coordinates:
        difference_x = end[0] -start[0]
        difference_y = end[1] -start[1]
        current_x = start[0]
        current_y = start[1]
        increase_x = 0 if difference_x == 0 else (1 if difference_x > 0 else -1)
        increase_y = 0 if difference_y == 0 else (1 if difference_y > 0 else -1)
        if difference_x != 0 and difference_y != 0 and not include_diagonals:
            continue
        while current_x != end[0] + increase_x or current_y != end[1] + increase_y:
            seen[(current_x, current_y)] += 1
            if seen[(current_x, current_y)] == 2:
                passed_more_than_once += 1
            current_x += (0 if difference_x == 0 else (1 if difference_x > 0 else -1))
            current_y += (0 if difference_y == 0 else (1 if difference_y > 0 else -1))
    return passed_more_than_once

def part_1():
    return count_passed_multiple_times(False)

def part_2():
    return count_passed_multiple_times(True)


print(f"Part 1: {part_1()}")
print(f"Part 2: {part_2()}")
