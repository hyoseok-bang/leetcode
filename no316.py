# https://leetcode.com/problems/remove-duplicate-letters/

import collections

def removeDuplicateLetters(s):
    """
    :type s: str
    :rtype: str
    """
    counter, seen, stack = collections.Counter(s), set(), list()
    
    for c in s:
        counter[c] -= 1
        
        # Pass if c is already processed
        if c in seen:
            continue
        
        # 1) If stack is empty -> pass
        # 2) If c is greater than the last item in the stack (in alphabetical order) -> pass
        # 3) If the last item in the stack does not appear anymore -> pass
        while stack and c < stack[-1] and counter[stack[-1]] > 0:
            seen.remove(stack.pop())
        
        stack.append(c)
        seen.add(c)
    
    return ''.join(stack)
