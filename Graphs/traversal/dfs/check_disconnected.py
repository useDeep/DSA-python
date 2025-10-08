from .dfs_recursive import visited, dfs
from ...graph_ad_list import graph, add_edge, add_node

add_node("A")
add_node("B")
add_node("C")
add_node("D")
add_node("E")
add_node("F")
add_node("G")

add_edge("A", "B")
add_edge("A", "C")
add_edge("B", "C")
add_edge("C", "D")
add_edge("E", "F")

dfs("A", visited, graph)

for i in list(graph):
    if i not in visited:
        print("Given graph is disconnected graph")
        break
else:
    print("Graph is a connected graph")

# to visit the disconnected nodes

for i in list(graph):
    if i not in visited:
        dfs(i, visited, graph)