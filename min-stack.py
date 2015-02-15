class MinStack:
    def __init__(self):
        self._mins = []
        self._stack = []

    # @param x, an integer
    # @return an integer
    def push(self, x):
        self._stack.append(x)

        if len(self._mins) == 0 or \
           self._mins[-1] >= x:
           # minimum may appear multiple times.
           # '=' makes sure the min don't get popped too early.

            self._mins.append(x)

        return len(self._stack)

    # @return nothing
    def pop(self):
        popped = self._stack.pop()

        if popped == self.getMin():
            self._mins.pop()

    # @return an integer
    def top(self):
        return self._stack[-1]

    # @return an integer
    def getMin(self):
        return self._mins[-1]
