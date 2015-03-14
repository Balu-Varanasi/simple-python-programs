"""
    A robot is located in the upper-left corner of a 4×4 grid.
    The robot can move either up, down, left, or right, but
    cannot go to the same location twice. The robot is trying
    to reach the lower-right corner of the grid. Your task is
    to find out the number of unique ways to reach the destination.

    INPUT SAMPLE:
        There is no input for this program.

    OUTPUT SAMPLE:
        Print out the number of unique ways for the robot to
        reach its destination. The number should be printed out
        as an integer ≥0.
"""


def count_paths(grid, current_x, current_y, end_x, end_y):

    if current_x < 0 or current_x > 3 or current_y < 0 or current_y > 3:
        return 0

    if grid[current_x][current_y]:
        return 0

    if current_x == end_x and current_y == end_y:
        return 1

    grid[current_x][current_y] = True

    result = 0

    result += count_paths(grid, current_x+1, current_y,   end_x, end_y)
    result += count_paths(grid, current_x,   current_y+1, end_x, end_y)
    result += count_paths(grid, current_x-1, current_y,   end_x, end_y)
    result += count_paths(grid, current_x,   current_y-1, end_x, end_y)

    grid[current_x][current_y] = False

    return result


def main():
    four_by_four_grid = [
        [False, False, False, False],
        [False, False, False, False],
        [False, False, False, False],
        [False, False, False, False]
    ]

    print count_paths(four_by_four_grid, 0, 0, 3, 3)

if __name__ == '__main__':
    main()
