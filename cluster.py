"""Compute similarity-based clusters in a weighted undirected graph."""


def _all_nodes(graph):
    """Return an iterable over nodes for common graph interfaces."""
    if hasattr(graph, "nodes"):
        nodes_attr = graph.nodes
        return nodes_attr() if callable(nodes_attr) else nodes_attr
    return graph


def cluster(graph, weights, level):
    """
    Return clusters at the given similarity level.

    Two nodes are connected in the thresholded graph iff the edge between
    them has weight >= level.
    """

    visited = set()
    clusters = set()

    for start in _all_nodes(graph):
        if start in visited:
            continue

        component = set()
        stack = [start]
        visited.add(start)

        while stack:
            node = stack.pop()
            component.add(node)
            for neighbor in graph.neighbors(node):
                if neighbor in visited:
                    continue
                if weights(node, neighbor) < level:
                    continue
                visited.add(neighbor)
                stack.append(neighbor)

        clusters.add(frozenset(component))

    return frozenset(clusters)
