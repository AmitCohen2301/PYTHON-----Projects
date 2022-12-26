def reachableBFS(graph, node):
    reachableList = []  # Nodes we can reach to
    queueOfNodeToEndle = []  # Nodes that we need to check where we can get to from them
    discoveredNodes = []  # Nodes that we already checked
    queueOfNodeToEndle.append(node)
    while len(queueOfNodeToEndle) != 0: # Move on all nodes we need to endle
        nodeToEndle = queueOfNodeToEndle.pop(0) # Take first in queue
        if nodeToEndle not in discoveredNodes: # Node we didn't see yet
            reachableList.append(nodeToEndle) # Add to reachable list
            discoveredNodes.append(nodeToEndle) # Add to discoverd nodes
            for newNodeToHandle in graph[nodeToEndle]: # Move on every posible edge from node to handle
                queueOfNodeToEndle.append(newNodeToHandle) # Add nodes that we can reach to and need to handle
    return reachableList