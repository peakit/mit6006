"""
Topological sort is like outputing DFS results in reverse. The graph needs
to be DAG (Directed Acyclic Graph) that is it must not have in cycles.

Top sort ensures the whole graph is traversed by keep moving the starting
vertex to another random vertex which is not-visited

This is used in Job scheduling, meeting pre-requisites for courses etc.
"""
import random


def topological_sort(adj_matrix, start_vertex, output, visited):
    connections = adj_matrix.get(start_vertex)
    if connections is not None:
        for conn in connections:
            if visited.get(conn) is None:
                topological_sort(adj_matrix, conn, output, visited)

    visited[start_vertex] = 1
    output.append(start_vertex)


def capture_inputs():
    print("Enter the number of vertices=", end="")
    vertices = int(input())
    adj_matrix = dict()
    for v in range(1, vertices+1):
        print("Vertex#" + str(v) + " is connected to=", end="")
        connections = input()
        if connections != '':
            connections = [int(c) for c in connections.split(",")]
        else:
            connections = None
        adj_matrix[v] = connections
    print("Enter the starting vertex=", end="")
    start_vertex = int(input())
    return adj_matrix, start_vertex


def main():
    adj_matrix, start_vertex = capture_inputs()
    output = list()
    visited = dict()
    topological_sort(adj_matrix, start_vertex, output, visited)

    while len(output) < len(adj_matrix.keys()):
        # if the entire graph has not been visited with the
        # earlier starting vertex, choose another non-visited
        # node as the starting vertex
        new_start_vertex = random.choice(
            list(
                adj_matrix.keys() - set(output)
            )
        )
        topological_sort(adj_matrix, new_start_vertex, output, visited)

    # reverse the output and print the results
    print("=>Topological sort order=", output[::-1])


if __name__ == "__main__":
    main()
