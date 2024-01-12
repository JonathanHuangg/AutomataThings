import collections as col

def createGraph(graph) -> dict:
    # Well, well, well, doesn't this look like advent of code all of a sudden

    newGraph = col.defaultdict(list)

    # each semicolon is a vertex
    vertices = graph.split(";")

    for vertex in vertices:
        sections = vertex.split(",")
        
        for i in range(len(sections)):
            if i == 0:
                start = sections[i]
            else:
                newGraph[start].append(sections[i])
    
    return newGraph
            

def passesNFA(graph, start):
    print("1")
def main():

    print()
    print("________________________")
    print()

    print("Enter the graph in this form -> vertex1, (edge1, alphabet associated1, alphabet associated 2...), edge2(...)... with every semicolon separating every vertex")
    graph = input("Example -> 0, (0, a, b), (1, a); 1, (2, a); 2, (3, a); 3, (4, a); 4, (5, a) \n")
    
    print()
    print("Enter the start state")
    start = input("Example -> a \n")
    print()

    print()
    print("Enter the string to test")
    string = input("Example -> aaaa \n")
    print()

    exampleGraph = {0 : [("a", "b", 0), ("a", 1)], 1 : [("a", 2)], 2 : [("a", 3)], 3 : [("a", 4)], 4 : [("a", 5)]}
if __name__ == "__main__":
    main()
