def permute(self, nums):
    """
    :type nums: List[int]
    :rtype: List[List[int]]
    """
    results = []
    prev_elements = []

    def dfs(elements):
        if len(elements) == 0:
            results.append(prev_elements[:])  # copy object

        for e in elements:
            next_elements = elements[:]
            next_elements.remove(e)
            prev_elements.append(e)
            dfs(next_elements)
            prev_elements.pop()  # initialize prev_elements before the next loop

    dfs(nums)
    return results
