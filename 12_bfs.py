"""
Perform a Breadth First Search over the given graph and a starting vertex
"""


def capture_inputs():
    print("Enter number of vertices=", end="")
    vert = int(input())

    adj_matrix = dict()
    for v in range(1, vert + 1):
        print("Vertex#", v, "connects to which other vertices=", end="")
        connections = input()
        adj_matrix[v] = [int(con) for con in connections.split(",")]

    print("Enter vertex from where to start the BFS=", end="")
    start_vert = int(input())

    return adj_matrix, start_vert


def bfs_search(adj_matrix, start_vert):
    """
    
    """
    frontiers = [start_vert]
    level = {}

    frontier_iter = iter(frontiers)
    i = 0

    traversal_result = []
    while True:
        try:
            frontier = next(frontier_iter)

            if level.get(frontier) is None:
                traversal_result.append(frontier)
                
                connected_vert = adj_matrix[frontier]
                frontiers.extend(connected_vert)
                level[frontier] = i     # mark as visited
                i = i + 1
        except StopIteration:
            break
    return traversal_result

def main():
    adj_matrix, start_vert = capture_inputs()
    traversal_result = bfs_search(adj_matrix, start_vert)
    print("=>Traversal result=", traversal_result)

if __name__ == "__main__":
    main()
