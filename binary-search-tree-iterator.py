# Definition for a  binary tree node
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class BSTIterator:
    # @param root, a binary search tree's root node
    def __init__(self, root):
        self._nodeStack = []
        self._traverseLeft(root)

    # @return a boolean, whether we have a next smallest number
    def hasNext(self):
        return len(self._nodeStack) > 0

    # @return an integer, the next smallest number
    def next(self):
        currentNode = self._nodeStack.pop()
        self._traverseLeft(currentNode.right)
        
        return currentNode.val
    
    def _traverseLeft(self, root):
        currentNode = root
        while currentNode:
            self._nodeStack.append(currentNode)
            currentNode = currentNode.left
        

# Your BSTIterator will be called like this:
# i, v = BSTIterator(root), []
# while i.hasNext(): v.append(i.next())