
def generate_graph():
    al = [[1, 2], [2], [3], [4], [5]]
    return al


def path_exists(al, source, destination):
    neighbours = al[source]
    try:
        if neighbours.index(destination) > -1:
            return True
    except ValueError as e:
        return False


adjacency_list = generate_graph()
print(path_exists(adjacency_list, 0, 6))


