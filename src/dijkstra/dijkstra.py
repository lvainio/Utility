from heapq import heappush, heappop


def dijkstra(G, s):
    dist = [float('inf') if v != s else 0 for v in range(len(G))]
    prev = [None for _ in range(len(G))]

    visited = set()
    pq = [(dist[s], s)]

    while pq:
        distance, node = heappop(pq)

        # If searching for a specific node we can 
        # check node == target here and break since the 
        # shortest path to this node is already found.

        if node in visited:
            continue
        else:
            visited.add(node)

        for neighbour, edge in G[node]:
            if distance + edge < dist[neighbour]:
                dist[neighbour] = distance + edge
                prev[neighbour] = node
                heappush(pq, (dist[neighbour], neighbour))
                
                # Instead of heappush one can implement update_key for the pq.
                # This avoids duplicate nodes in the pq and the need to check if
                # node is already visited. Requires less space. In this case
                # we should populate the priority queue with all the nodes initially.

    return dist, prev


def main():
    G = {
        0: [(1, 7), (3, 9), (2, 3), (5, 9)],
        1: [(5, 4), (0, 7)],
        2: [(6, 3), (0, 3), (4, 1)],
        3: [(5, 5), (0, 9)],
        4: [(5, 13), (2, 1), (6, 10)],
        5: [(4, 13), (0, 9), (6, 4), (3, 5), (1, 4)],
        6: [(4, 10), (5, 4), (2, 3)]
    }

    dist, prev = dijkstra(G, 0)

    print(dist)
    print(prev)


if __name__ == '__main__':
    main()