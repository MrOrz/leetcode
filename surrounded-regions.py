class Solution:
    # @param board, a 2D array
    # Capture all regions by modifying the input board in-place.
    # Do not return any value.
    def solve(self, board):
        self._rowCount = len(board)
        if self._rowCount == 0:
            return

        self._columnCount = len(board[0])
        if self._columnCount == 0:
            return

        # Convert list of strings to list of lists of single-character strings.
        # By doing this each individual cell can be modified.
        #
        self._board = [ list(row) for row in board ]

        for r in xrange(0, self._rowCount):
            for c in xrange(0, self._columnCount):
                if self._board[r][c] == 'O':
                    self._fillXWhenSurrounded(r,c)

        # Convert all 'visited' slots that is not filled with 'X' back to 'O'.
        #
        for r in xrange(0, self._rowCount):
            for c in xrange(0, self._columnCount):
                if self._board[r][c] == 'V':
                    self._board[r][c] = 'O'

        # Put the lists of single-character string back to board as concatenated strings.
        for r in xrange(0, self._rowCount):
            board[r] = ''.join( self._board[r] )

    def _fillXWhenSurrounded(self, sourceR, sourceC):
        """
            Flood from (sourceR,sourceC) if (sourceR,sourceC) itself is 'O' using BFS.
            It first marks itself as visited ('V') and floods its neighbors.

            return True when the connected region is surrounded by 'X', or itself is 'X'.
        """

        bfsQueue = [(sourceR,sourceC)]
        queuePtr = 0

        # Initially assume the connected component is surrounded by 'X'
        isSurrounded = True

        while queuePtr < len(bfsQueue):
            r, c = bfsQueue[queuePtr]
            queuePtr += 1

            cell = self._getCell(r, c)

            if cell is None:
                # Open end reached!
                isSurrounded = False

            elif cell is 'O':
                self._board[r][c] = 'V'
                bfsQueue.extend([(r-1, c), (r+1, c), (r, c-1), (r, c+1)])

        if isSurrounded:
            # Fill all 'V' with 'X'
            for r, c in bfsQueue:
                if self._getCell(r, c) == 'V':
                    self._board[r][c] = 'X'


    def _getCell(self, r, c):
        """
            Returns board given (r,c) coordinate.
            If (r,c) is out of bound of the board, return None.
        """

        if r < 0 or r >= self._rowCount or c < 0 or c >= self._columnCount:
            return None

        return self._board[r][c]
