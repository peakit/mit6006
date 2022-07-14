"""
Perform a Depth First Search for the given graph and starting vertex.
"""

def dfs_visit(vertex, adj_matrix, visited, output):
    """
    Called from dfs search to recursively traverse the graph in DFS 
    approach
    """
    visited[vertex] = 1
    output.append(vertex)

    connections = adj_matrix[vertex]
    
    if connections is None:
        return

    for conn in connections:
        if visited.get(conn) is None:
            dfs_visit(conn, adj_matrix, visited, output)


def dfs_search(adj_matrix, start_vertex):
    """
    Keep chasing a node and then its connected node
    and further its connected nodes. Inherently recursive
    behavior is emulated as a recursion of dfs_visit()
    """
    visited = dict()
    output = list()

    dfs_visit(start_vertex, adj_matrix, visited, output)
    return output


def capture_inputs():
    print("Enter the number of vertices=", end="")
    vertices = int(input())
    adj_matrix = dict()
    for v in range(1, vertices+1):
        print("Vertex#" + str(v) + " is connected to=", end="")
        connections = input()
        if connections != '':
            connections = [int(c) for c in connections.split(",")]
        adj_matrix[v] = connections
    print("Enter the starting vertex=", end="")
    start_vertex = int(input())
    return adj_matrix, start_vertex


def main():
    adj_matrix, start_vertex = capture_inputs()
    output = dfs_search(adj_matrix, start_vertex)
    print("=>Depth First traversal of graph is=", output)


if __name__ == "__main__":
    main()
