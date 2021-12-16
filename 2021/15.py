import sys
from heapq import heappush, heappop

input_file = sys.argv[1] if len(sys.argv) > 1 else "inputs/15.txt"
with open(input_file) as file:
    risk_levels = [list(map(int, list(line.strip()))) for line in file.readlines()]

ROW_NUM = len(risk_levels)
COL_NUM = len(risk_levels[0])


def part_1():
    distances = {(row, col): float("inf") for row in range(ROW_NUM) for col in range(COL_NUM)}
    to_visit_priority_queue = []
    heappush(to_visit_priority_queue, (0, (0, 0)))
    while True:
        current_distance, current_coordinates = heappop(to_visit_priority_queue)
        current_row, current_col = current_coordinates
        neighbors = []
        if current_row == ROW_NUM - 1 and current_col == COL_NUM - 1:
            return current_distance
        if current_row != ROW_NUM - 1:
            neighbors.append((current_row + 1, current_col))
        if current_col != COL_NUM - 1:
            neighbors.append((current_row, current_col + 1))
        for neighbor_row, neighbor_col in neighbors:
            tentative_risk_level = current_distance + risk_levels[neighbor_row][neighbor_col]
            if tentative_risk_level < distances[(neighbor_row, neighbor_col)]:
                distances[(neighbor_row, neighbor_col)] = tentative_risk_level
                heappush(to_visit_priority_queue, (tentative_risk_level, (neighbor_row, neighbor_col)))


def part_2():
    pass


print(f"Part 1: {part_1()}")
print(f"Part 2: {part_2()}")