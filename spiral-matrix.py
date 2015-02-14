class Solution:
    # @param matrix, a list of lists of integers
    # @return a list of integers
    def spiralOrder(self, matrix):
        if len(matrix) == 0 or len(matrix[0]) == 0:
            return []

        elif len(matrix) == 1:
            # 1 row
            return matrix[0]

        elif len(matrix[0]) == 1:
            # 1 column
            return [row[0] for row in matrix]

        else:
            # Top row
            shell = matrix[0]
    
            # Right column, exclude top & bottom
            middleRows = matrix[1:-1]
            shell += [row[-1] for row in middleRows]
    
            # Bottom row
            bottomRow = matrix[-1]
            bottomRow.reverse()
            shell += bottomRow
            
            # Left column, exclude top & bottom
            middleRows.reverse()
            shell += [row[0] for row in middleRows]

            return shell + self.spiralOrder( [ middleRow[1:-1] for middleRow in matrix[1:-1] ] )
