# https://leetcode.com/problems/product-of-array-except-self/

class Solution(object):
    def productExceptSelf(self, nums: List[int]) -> List[int]:
      out = []
      
      n = 1  # 
      # Append the product of leftmost values from the index i
      for i in range(len(nums)):
        out.append(n)
        n *= nums[i]
      # In the list out = [ identity, product from the left when index=1, product from the left when index=2, ... ]
      
      # Multiplicate rightmost elements when index=i
      n = 1
      for i in range(len(nums) - 1, -1, -1):
        out[i] = out[i] * n  # At start, multiplicate the identity to the last element in out
        n *= nums[i]
      
      return out
        
