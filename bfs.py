BFS(graph, startVert):
# start w a graph and vertex we will start on
# first thing we do is go through each vert and make them color white // at the outset all verts are unvisited
    for v of graph.vertexes:
        v.color = white

# next, mark starting vert as gray / because we are exploring the SV's neighbors
# also enqueue the SV which means it will be first vert we look at once we enter loop
    startVert.color = gray
    queue.enqueue(startVert)

# condition we check at outset is if the queue is not empty 
# if its not empty, we look at first item in queue by storing it in variable
    while !queue.isEmpty():
        u = queue[0]  
        # Peek at head of the queue, but do not dequeue!

        # then loop through each of that verts neighbors and:
            # check if unvisited / if it is, mark as gray and enqueue the vert
        for v of u.neighbors:
            if v.color == white:
                v.color = gray
                queue.enqueue(v)
        
        # next dequeue the current vert weve been exploring and mark it as black
        # continue on this process until all verts have been explored
        queue.dequeue()
        u.color = black

