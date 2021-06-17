# https://leetcode.com/problems/cheapest-flights-within-k-stops/
# Timeout error

def findCheapestPrice(self, n, flights, src, dst, k):
    """
    :type n: int
    :type flights: List[List[int]]
    :type src: int
    :type dst: int
    :type k: int
    :rtype: int
    """
    graph = collections.defaultdict(list)
    for _from, _to, _price in flights:
        graph[_from].append((_to, _price))


    queue = [(0, src, k)]

    while queue:
        price, node, k = heapq.heappop(queue)
        if node == dst:  # If arrive at dst within k stops
            return price
        if k >= 0:  # if the number of stops from the start to node is less than k
            for _to, _price in graph[node]:
                next_price = price + _price
                heapq.heappush(queue, (next_price, _to, k-1))

    return -1
