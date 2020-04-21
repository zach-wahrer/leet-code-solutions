class Solution:
    def leftMostColumnWithOne(self, binaryMatrix: 'BinaryMatrix') -> int:
        rows, cols = binaryMatrix.dimensions()
        row_index = 0
        col_index = cols - 1
        last_seen = -1
        while row_index < rows and col_index >= 0:
            value = binaryMatrix.get(row_index, col_index)
            if value == 1:
                last_seen = col_index
                col_index -= 1

            else:
                row_index += 1

        return last_seen
