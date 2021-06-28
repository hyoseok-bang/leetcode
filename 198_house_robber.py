# https://leetcode.com/problems/house-robber/
import collections

def rob(nums):
    # Save result here; the ith element is the max amount that can steal when we were to visit ith house
    # dp[i]: maximum amount of money you can rob when you were to only rob 1 ~ ith house
    dp = [0] * len(nums)  
    
    if len(nums) <= 2:
        return max(nums)
    else:
        dp[0], dp[1] = nums[0], max(nums[0], nums[1])
        for i in range(2, len(nums)):
            # Compare the two results:
            # maximum amount when we consider (i-1)th house and the amount when we visit ith house
            # Save the bigger one
            dp[i] = max(dp[i-1], dp[i-2] + nums[i])
    print(dp)
    return max(dp)
