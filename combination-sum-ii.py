from collections import defaultdict

class Solution:
    # @param candidates, a list of integers
    # @param target, integer
    # @return a list of lists of integers
    def combinationSum2(self, candidates, target):
        candidates.sort()
        candidates = filter(lambda c: c<=target, candidates)

        # Dynamic programming
        #
        # dp[i][j]: The solution set of solving the subproblem using first i(>=0) candidates with target = j.
        #           The solution set is a list of list of integers.
        #
        # no Candidates (i < 0? 'below' the 0th candidate):
        # Solving the subproblem using 0 candidates has no solution.
        #
        # j<=0
        # Solving the subproblem with target = 0 is always solvable with an empty combination.
        # Solving the subproblem with target < 0 has no solution.
        #
        # Recursive pattern
        #                                     Smaller target used by less candidates
        #                                   __________________________________________
        #                                  /                                          \
        # dp[i][j] = dp[i-1][j] UNION (append candidate[i] to all combinations in dp[i-1][j-candidate[i]])
        #            \________/
        #           Same target
        #         already solvable
        #      using less candidates
        #

        table = {}

        def dp(i, j):
            """
            Subproblem solving using first i-th candidates (starting from 0)
            to match a (maybe smaller) target j.
            """
            
            if j == 0:
                return [ [] ]
            
            elif j < 0:
                return []
                
            if i < 0:
                return []

            elif i == 0:
                # Solve only with the 0th candidate.
                # Only when the 0th candidate == current target (j), the subproblem can be solved.
                #
                return [ [candidates[0]] ] if candidates[0] == j else []

            if not (i in table and j in table[i]):
                newCandidate = candidates[i]
                solutionSet = dp(i-1, j) + [ solution + [newCandidate] for solution in dp(i-1, j-newCandidate)]
                
                # Make sure each solution in dp(i, j) is unique.
                solutionSet = map( list, set( map(tuple, solutionSet ) ) )
                
                if i not in table:
                    table[i] = {}

                table[i][j] = solutionSet
                
            return table[i][j]

        return dp(len(candidates)-1, target)
                
