# https://leetcode.com/problems/network-delay-time/

def networkDelayTime(self, times: List[List[int]], n: int, k: int) -> int:
    # Convert the input list into a graph
    graph = collections.defaultdict(list)
    for source, target, time in times:
        graph[source].append((target, time))

    arrived = collections.defaultdict(int)  # Initialize a dict to store the arrival time from the start node
    queue = [(0,k)]  # Use priority queue to find shortest next node
    
    # Start finding the arrival time to each node from the start node
    while queue:
        time, node = heapq.heappop(queue) # Pop the shortest(smallest) node using heapq
        if node not in arrived:  # Record as arrived if it is not
            arrived[node] = time
            for _target, _time in graph[node]:  # Search for the nodes to move next
                delay = time + _time  # Compute the arrival time to that node from the start node
                heapq.heappush(queue, (delay, _target))  # Save (time, target) to the queue

    if len(arrived) == n:  # If it's possible to visit all nodes from the start
        return max(arrived.values())  # Return the arrival time of the longest node
    else:  # If it's not available to visit all nodes from the start
        return -1  # Return -1
