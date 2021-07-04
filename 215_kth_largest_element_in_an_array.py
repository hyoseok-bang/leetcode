class Solution(object):
    def findklargest_push(self, nums, k):
        # Use heappush
        heap = []

        for n in nums:
            heapq.heappush(heap, -n)
        
        for _ in range(1,k):
            heapq.heappop(heap)
        
        return -heapq.heappop(heap)
    
    def findklargest_heapify(self, nums, k):
        # Use heapify
        heapq.heapify(nums)

        for _ in range(len(nums) - k):  # Since heapq module is min-heap, pop n-kth element form the heap
            heapq.heappop(nums)
        
        return heapq.heappop(nums)
    
    def findklargest_nlargest(self, nums, k):  # Return 1 ~ k largest values from the array nums
        return heapq.nlargest(k, nums)[-1]

    def findklargest_sort(self, nums, k):
        return sorted(nums, reverse=True)[k-1]
