# https://leetcode.com/problems/valid-parentheses/

class Solution(object):
    def isValid(self, s):
        """
        :type s: str
        :rtype: bool
        """
        stack = []  # Use list as a stack
        table = {
            ')':'(', 
            '}':'{', 
            ']':'['
        }
        
        for c in s:
            # Push the character if it is not one of closing parantheses
            if c not in table:
                print(c)
                stack.append(c)
            # Exception handling
            # 1) If one of closing parantheses appears first -> return False
            # 2) If closing parentheses do not match with its table values -> return False
            # Note: condition (not stack) should come first, since pop() is a inplace method
            elif not stack or table[c] != stack.pop():
                print(c)
                return False
        
        # Return True if all the opening parantheses popped out of the stack
        return len(stack) == 0
