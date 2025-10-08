# dfs using iterative approach (stack is used externally)

from ...graph_ad_list import graph, add_edge, add_node


def dfs(node, graph):
    visited= set()
    stack= []
    if node not in graph:
        print("node is not present in the graph")
        return
    stack.append(node)
    while stack:
        current= stack.pop()
        if current not in visited:
            print(current)
            visited.add(current)
            for i in graph[current]:
                stack.append(i)
        





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

    dfs("B", graph)
