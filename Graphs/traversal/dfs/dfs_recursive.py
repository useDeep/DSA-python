# dfs using recursive approach

from ...graph_ad_list import graph, add_edge, add_node

def dfs(node, visited, graph):
    if node not in visited:
        print(node)
        visited.add(node)
        for i in graph[node]:
            dfs(i, visited, graph)

visited= set()

if __name__== "main":
    add_node("A")
    add_node("B")
    add_node("C")
    add_node("D")
    add_node("E")

    add_edge("A", "B")
    add_edge("B", "E")
    add_edge("A", "C")
    add_edge("A", "D")
    add_edge("B", "D")
    add_edge("C", "D")

    dfs("B", visited, graph)
