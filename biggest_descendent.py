"""Compute biggest descendent values in a directed tree."""


def _children(graph, node):
    """Return the outgoing neighbors of node as a list."""
    return list(graph.neighbors(node))


def biggest_descendent(graph, root, value):
    """
    Return a dictionary mapping each node to its biggest descendent value.

    A node is considered a descendent of itself.
    """

    biggest = {}

    def dfs(node):
        best = value[node]
        for child in _children(graph, node):
            child_best = dfs(child)
            if child_best > best:
                best = child_best
        biggest[node] = best
        return best

    dfs(root)
    return biggest
