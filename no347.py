# https://leetcode.com/problems/top-k-frequent-elements/

def topKFrequent(self, nums, k):
    """
    :type nums: List[int]
    :type k: int
    :rtype: List[int]
    """
    freqs = collections.Counter(nums)
    freqs_heap = []
    for f in freqs:
        heapq.heappush(freqs_heap, (-freqs[f], f))
    topk = []
    for _ in range(k):
        topk.append(heapq.heappop(freqs_heap)[1])

    return topk

# More concise way:
def topKFrequent(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: List[int]
        """
        return list(zip(*collections.Counter(nums).most_common(k))[0])
