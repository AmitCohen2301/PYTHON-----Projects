def reachableDFS(graph, node):
    reachableList = [] # Nodes we can reach to
    stackOfNodeToEndle = [] # Nodes that we need to check where we can get to from them
    discoveredNodes = [] # Nodes that we already checked
    stackOfNodeToEndle.append(node)
    while len(stackOfNodeToEndle) != 0: # Move on all nodes we need to endle
        nodeToEndle = stackOfNodeToEndle.pop() # Take the head of stack
        if nodeToEndle not in discoveredNodes: # Node we didn't see yet
            reachableList.append(nodeToEndle) # Add to reachable list
            discoveredNodes.append(nodeToEndle) # Add to discoverd nodes
            for newNodeToHandle in graph[nodeToEndle]: # Move on every posible edge from node to handle
                stackOfNodeToEndle.append(newNodeToHandle) # Add nodes that we can reach to and need to handle
    return reachableList