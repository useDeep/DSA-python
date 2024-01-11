def add_node(v):
    global node_count
    if v in nodes:
        print("the node is already exists")
    else:
        node_count+=1
        nodes.append(v)
        for i in graph:
            i.append(0)
        graph.append([0] * node_count)

def add_edge(v1, v2, cost=1):
    if v1 not in nodes:
        print(v1," is not present in graph")
    elif v2 not in nodes:
        print(v2, " is not present")
    else:
        v1_index= nodes.index(v1)
        v2_index= nodes.index(v2)
        graph[v1_index][v2_index]= cost
        graph[v2_index][v1_index]= cost

def delete_node(v):
    global node_count
    if v not in nodes:
        print(v," doesn't exist")
    else:
        node_count-=1
        v_index= nodes.index(v)
        nodes.remove(v)
        for i in graph:
            i.pop(v_index)
        graph.pop(v_index)

def delete_edge(v1, v2):
    if v1 not in nodes:
        print(v1," is not present in graph")
    elif v2 not in nodes:
        print(v2, " is not present")
    else:
        v1_index= nodes.index(v1)
        v2_index= nodes.index(v2)
        graph[v1_index][v2_index]= 0
        graph[v2_index][v1_index]= 0

def print_graph():
    for i in graph:
        for j in i:
            print(format(j, "<3"), end=" ")
        print()

nodes= []
graph= []
node_count= 0
add_node('A')
add_node('B')
add_node('C')
add_edge('B', 'C', 500)
# delete_node('A')
delete_edge('B', 'C')
print_graph()