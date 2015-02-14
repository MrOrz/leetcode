# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    # @param head, a ListNode
    # @param k, an integer
    # @return a ListNode
    def rotateRight(self, head, k):
        
        # Find the length of the linked list,
        # and the last node of the list.
        len = 0
        currentNode = head
        oldEnd = None
        while currentNode:
            len += 1
            oldEnd = currentNode
            currentNode = currentNode.next
            
        # Determine the new starting node of the rotated list.
        cuttingK = 0 if len == 0 else (len - k) % len
        newHead = head
        newEnd = oldEnd
        while cuttingK > 0:
            cuttingK -= 1
            newEnd = newHead
            newHead = newHead.next
            
        # Connect the last node with the first node
        if oldEnd:
            oldEnd.next = head
        
        # Break the end of the rotated list
        if newEnd:
            newEnd.next = None
        
        return newHead
        
        