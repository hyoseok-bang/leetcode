# https://leetcode.com/problems/climbing-stairs/

class Solution(object):
    
    tb = collections.defaultdict(int)
    
    def climbStairs(self, n):
        """
        :type n: int
        :rtype: int
        """

        if n <= 2:
            return n
        if self.tb[n]:
            return self.tb[n]
        self.tb[n] = self.climbStairs(n-1) + self.climbStairs(n-2)
        
        return self.tb[n]