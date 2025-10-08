def add_node(v):
    if v in graph:
        print(v," already exists")
    else:
        graph[v]= []

def add_edge(v1, v2, cost=1):
    if v1 not in graph:
        print(v1," doesn't exist")
    elif v2 not in graph:
        print(v2," doesn't exist")
    else:
        # list1= [v2, cost]
        # list2= [v1, cost]
        graph[v1].append(v2)
        graph[v2].append(v1)

def delete_node(v):
    if v not in graph:
        print(v," doesn't exist")
    else:
        list1= graph[v]
        del graph[v]
        for i in list1:
            graph[i].remove(v)

def delete_edge(v1, v2):
    if v1 not in graph:
        print(v1, "doesn't exist")
    elif v2 not in graph:
        print(v2, "doesn't exist")
    else:
        graph[v1].remove(v2)
        graph[v2].remove(v1)


graph= {}

if __name__ == "main":
    add_node('A')
    add_node('B')
    add_node('C')
    add_edge('A', 'C')
    # delete_node('B')
    delete_edge('A', 'C')
    print(graph)
