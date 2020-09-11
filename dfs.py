DFS(graph):
# takes the graph as a parameter and makrs all verts as unvisited
# also sets the parent of each vert to null
    for v of graph.verts:
        v.color = white
        v.parent = null

# visits each vert in the graph and if unvisited:
    # pass that vert into second function
    for v of graph.verts:
        if v.color == white:
            DFS_visit(v)

DFS_visit(v):
# starts out by marking vert as gray (process of being explored)
    v.color = gray

# loops through all ofi ts unvisited neighbors
# sets the parent and makes recursive call to DFSvisit
    for neighbor of v.adjacent_nodes:
        if neighbor.color == white:
            neighbor.parent = v
            DFS_visit(neighbor)
# once done exploring all neighbors, nakes vert as black
    v.color = black
