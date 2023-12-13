from collections import defaultdict

def dfs_iterative(graph, start):
    visited = set()
    stack = [start]
    while stack:
        node = stack.pop()
        if not node in visited:
            print(node)
            visited.add(node)
            for neighbour in graph[node]:
                stack.append(neighbour)



def main():
    graph = {
        0: [1, 3, 2, 5],
        1: [8, 5],
        2: [6, 7, 0, 4, 9, 1, 3],
        3: [5],
        4: [9],
        5: [8, 4, 0, 9],
        6: [4, 5, 2, 0],
        7: [0, 1, 8, 9, 4],
        8: [4],
        9: [5, 8, 7, 2, 0, 3, 6]
    }

    dfs_iterative(graph, 0)


if __name__ == '__main__':
    main()