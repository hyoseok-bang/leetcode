def max_subarray(nums):
    for i in range(1, len(nums)):
        nums[i] += nums[i-1] if nums[i-1] > 0 else 0
    return max(nums)


# Kadane's Algorithm
def maxSubArray(nums):
    best_sum = -sys.maxsize
    current_sum = 0
    for num in nums:
        current_sum = max(sum, current_sum + sum)
        best_sum = max(best_sum, current_sum)
    
    return best_sum