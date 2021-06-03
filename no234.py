# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def isPalindrome_list(self, head):
        """
        :type head: ListNode
        :rtype: bool
        """
        
        l = []
        
        # If the LinkedList is empty, return False directly
        if not head:
            return False
        
        # Append elements in LinkedList to a new list object
        while head is not None:
            l.append(head.val)
            head = head.next
        
        # Examine whether it is a palindrome
        while len(l) > 1:
            if l.pop(-1) != l.pop(0):
                return False
        
        return True
      
    def isPalindrome_deque(self, head: ListNode) -> bool:
        # Using deque, pop() method from either side can be done in O(1)
        
        # Initialize deque
        q: Deque = collections.deque()
        
        # If the LinkedList is empty, return False directly
        if not head:
            return False
        
        # Append elements in LinkedList to a new list object
        while head is not None:
            q.append(head.val)
            head = head.next
        
        # Examine whether it is a palindrome
        while len(q) > 1:
            if q.popleft() != l.pop():
                return False
        
        return True
    
    def isPalindrome_runner(self, head):
        rev = None
        fast = slow = head
        
        while fast and fast.next:  # Finish while loop if either value is None
            fast = fast.next.next
            slow, rev, rev.next = slow.next, slow, rev
            # rev, rev.next, slow = slow, rev, slow.next
        if fast:  # Case when the length of LinkedList is odd
            slow = slow.next
        
        # Examine palinfrome
        while rev and rev.val == slow.val:
            rev, slow = rev.next, slow.next
        
        return not rev
