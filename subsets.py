class Solution:
    # @param S, a list of integer
    # @return a list of lists of integer
    def subsets(self, S):
        S.sort()
        self.S = S
        self.size = len(S)

        self.answerSets = []
        self._dfs(0, [])
        return self.answerSets
    
    def _dfs(self, i, subset):
        if i == self.size:
            self.answerSets.append(list(subset))
        else:
            self._dfs(i+1, subset)
            subset.append(self.S[i])
            self._dfs(i+1, subset)
            subset.pop()
