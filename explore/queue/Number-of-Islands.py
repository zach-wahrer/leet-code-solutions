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
    count = 0

    for row_position in range(0, len(grid)):
        for col_position in range(0, len(grid[0])):
            key = _key_gen(row_position, col_position)
            if key not in memoize and grid[row_position][col_position] == "1":
                count += 1
                _assimilate(row_position, col_position)

    return count


print(num_islands(board))
