class Solution:
    # @return a boolean
    OPEN_PARENTHESES = ('{', '[', '(')
    CLOSE_TO_OPEN = {
        '}': '{',
        ']': '[',
        ')': '('
    }

    def isValid(self, s):
        parenthesesStack = []

        for char in s:
            if char in self.OPEN_PARENTHESES:
                parenthesesStack.append(char)
            else: # char is a closing parentheses

                if len(parenthesesStack) <= 0:
                    # No opening parentheses in stack, incorrect.
                    return False

                latestOpening = parenthesesStack.pop()
                if self.CLOSE_TO_OPEN[char] != latestOpening:
                    # Not matching the latest opening parentheses, incorrect.
                    return False

        if len(parenthesesStack) > 0:
            # Dangling opening parentheses, incorrect.
            return False

        return True
