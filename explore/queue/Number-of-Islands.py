board = [
    ['1', '1', '0', '0', '0'],
    ['1', '1', '0', '0', '0'],
    ['0', '0', '1', '0', '0'],
    ['0', '0', '0', '1', '1']
]


def num_islands(grid: list) -> int:

    def _key_gen(row, col):
        if row in range(0, len(grid)) and col in range(0, len(grid[0])):
            return (row, col)
        return 'stop'

    def _assimilate(row, col):
        key = _key_gen(row, col)
        if key == 'stop':
            return
        if key not in memoize and grid[row][col] == "1":
            memoize[key] = True
            _assimilate(row + 1, col)
            _assimilate(row, col + 1)
            _assimilate(row - 1, col)
            _assimilate(row, col - 1)

    memoize = {}

    def _check_square(row, col, count):

        if row == len(grid):
            return count

        key = _key_gen(row, col)

        if key == 'stop':
            return _check_square(row + 1, 0, count)

        if key not in memoize and grid[row][col] == "1":
            count += 1
            _assimilate(row, col)

        return _check_square(row, col + 1, count)

    return _check_square(0, 0, 0)


print(num_islands(board))
