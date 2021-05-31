# https://leetcode.com/problems/3sum/

def threeSum(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        result = []
        nums.sort()  # sort the array to simplify the solution
        
        for i in range(len(nums) - 2):
            # skip the duplicate value
            if i > 0 and nums[i] == nums[i-1]:
                continue
            
            # initialize two pointers
            left, right = i+1, len(nums) - 1
            
            # start searching for solution
            while left < right:
                sum = nums[i] + nums[left] + nums[right]
                
                if sum < 0:
                    left += 1
                elif sum > 0:
                    right -= 1
                else:
                    result.append([nums[i], nums[left], nums[right]])
                    
                    # skip the duplicates
                    while left < right and nums[left] == nums[left + 1]:
                        left += 1
                    while left < right and nums[right] == nums[right - 1]:
                        right -= 1
                    
                    left += 1
                    right -= 1
        
        return result
