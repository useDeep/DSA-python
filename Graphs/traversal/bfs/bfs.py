from ...graph_ad_list import graph, add_edge, add_node

def bfs(node, graph, visited):
    if node not in graph:
        print(node, " not present in the graph")
        return 
    queue= []
    queue.append(node)
    visited.add(node)
    while queue:
        current= queue.pop()
        print(current)
        for i in graph[current]:
            if i not in visited:
                queue.append(i)
                visited.add(i)



visited= set()


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

bfs("B", graph, visited)