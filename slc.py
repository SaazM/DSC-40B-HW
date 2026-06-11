"""Single linkage clustering via Kruskal's algorithm."""


class DisjointSetForest:

    def __init__(self, elements):
        self._core = _DisjointSetForestCore()

        self.element_to_id = {}
        self.id_to_element = {}

        for element in elements:
            eid = self._core.make_set()
            self.element_to_id[element] = eid
            self.id_to_element[eid] = element

    def find_set(self, element):
        return self.id_to_element[
            self._core.find_set(
                self.element_to_id[element]
            )
        ]

    def union(self, x, y):
        x_id = self.element_to_id[x]
        y_id = self.element_to_id[y]
        self._core.union(x_id, y_id)

    def in_same_set(self, x, y):
        return self.find_set(x) == self.find_set(y)


class _DisjointSetForestCore:

    def __init__(self):
        self._parent = []
        self._rank = []
        self._size_of_set = []

    def make_set(self):
        x = len(self._parent)
        self._parent.append(None)
        self._rank.append(0)
        self._size_of_set.append(1)
        return x

    def find_set(self, x):
        try:
            parent = self._parent[x]
        except IndexError:
            raise ValueError(f'{x} is not in the collection.')

        if self._parent[x] is None:
            return x
        else:
            root = self.find_set(self._parent[x])
            self._parent[x] = root
            return root

    def union(self, x, y):
        x_rep = self.find_set(x)
        y_rep = self.find_set(y)

        if x_rep == y_rep:
            return

        if self._rank[x_rep] > self._rank[y_rep]:
            self._parent[y_rep] = x_rep
            self._size_of_set[x_rep] += self._size_of_set[y_rep]
        else:
            self._parent[x_rep] = y_rep
            self._size_of_set[y_rep] += self._size_of_set[x_rep]
            if self._rank[x_rep] == self._rank[y_rep]:
                self._rank[y_rep] += 1


def slc(graph, d, k):
    """Single linkage clustering: return k clusters as a frozenset of frozensets."""
    nodes = list(graph.nodes)
    n = len(nodes)

    if k < 1 or k > n:
        raise ValueError('k must be between 1 and the number of nodes, inclusive.')

    if k == n:
        return frozenset(frozenset({node}) for node in nodes)

    dsf = DisjointSetForest(nodes)

    weighted_edges = []
    for u, v in graph.edges:
        edge = tuple(sorted((u, v)))
        weighted_edges.append((d(edge), u, v))
    weighted_edges.sort()

    components = n
    for _, u, v in weighted_edges:
        if components == k:
            break
        if not dsf.in_same_set(u, v):
            dsf.union(u, v)
            components -= 1

    clusters = {}
    for node in nodes:
        rep = dsf.find_set(node)
        clusters.setdefault(rep, set()).add(node)

    return frozenset(frozenset(cluster) for cluster in clusters.values())
