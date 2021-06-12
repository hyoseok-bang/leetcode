# https://leetcode.com/problems/reconstruct-itinerary/

def findItinerary(self, tickets):
    """
    :type tickets: List[List[str]]
    :rtype: List[str]
    """
    graph = collections.defaultdict(list)
    for a, b in sorted(tickets):
        graph[a].append(b)
    route = []

    def dfs(a):
      # iterate until there is no connected destination
      # The items are appended from the last to first
        while graph[a]:
            dfs(graph[a].pop(0))
        route.append(a)

    dfs('JFK')
    return route[::-1]  # reverse the item 
