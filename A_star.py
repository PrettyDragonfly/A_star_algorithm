import math


def dist(vertices, src, tgt):
    return math.sqrt((pow(vertices[tgt]["x"]-vertices[src]["x"], 2)
                      + pow(vertices[tgt]["y"]-vertices[src]["y"], 2)
                      + pow(vertices[tgt]["z"]-vertices[src]["z"], 2)))


def find_path(parent, vertex):
    path = [vertex]
    while parent[vertex] is not None:
        vertex = parent[vertex]
        path.append(vertex)
    return reversed(path)


# graph : edges
# vertices : coordinates
def A_star(graph, vertices, departure, arrival):
    open = list()
    parent = dict()
    close = list()

    # Heuristic
    for vertex in graph:
        vertices[vertex]['h'] = dist(vertices, vertex, arrival)
        # initially, their total cost is equal to their heuristic
        vertices[vertex]['costtot'] = vertices[vertex]['h']
        vertices[vertex]['cost'] = 0

    # Addition of the departure vertex in the priority queue
    open.append(departure)
    parent[departure] = None

    ite = 1
    print("Iteration n° {}".format(ite))
    print("Open: {}".format(open))
    print("Close: (ø)")
    print('')

    # As long as we haven't met the arrival vertex
    while arrival not in open:
        current_vertex = min(open, key=lambda c: vertices[c]['costtot'])
        open.remove(current_vertex)
        close.append(current_vertex)

        for vertex in graph[current_vertex]:
            # We have already met this vertex
            if vertex in open:
                # if its cost it lower by this path, we update his parent
                if vertices[vertex]['costtot'] > dist(vertices, current_vertex, vertex) \
                        + vertices[current_vertex]['cost'] + vertices[vertex]['h']:
                    vertices[vertex]['costtot'] = dist(vertices, current_vertex, vertex) \
                            + vertices[current_vertex]['cost'] + vertices[vertex]['h']
                    parent[vertex] = current_vertex

            elif vertex not in close:
                # we update their cost (parent's cost + distance from the parent)
                vertices[vertex]['cost'] = vertices[current_vertex]['cost'] + dist(vertices, current_vertex, vertex)
                # update the total cost
                vertices[vertex]['costtot'] += vertices[vertex]['cost']

                parent[vertex] = current_vertex

                open.append(vertex)

        ite += 1
        print("Itération n° {}".format(ite))
        print("Open: {}".format(open))
        print("Close: {}".format(close))
        print('')

    res = find_path(parent, arrival)

    print("Path : ")
    for x in res:
        if x is not None:
            print(x)
