from itertools import combinations
from sage.all import Hypergraph
from sage.all import Poset


def generate_faces(facets):
    """Generate all non-empty subsets of all facets."""
    face_set = set()
    for facet in facets:
        facet = list(facet)
        for k in range(1, len(facet) + 1):
            for subface in combinations(facet, k):
                face_set.add(frozenset(subface))
    return face_set


def facets_to_inclusion_poset(facets):
    """Build inclusion poset from raw facet list."""
    faces = generate_faces(facets)
    return Poset((faces, lambda x, y: x.issubset(y)))


def is_linear_with(triangles, new_triangle):
    for t in triangles:
        if len(set(t) & set(new_triangle)) > 1:
            return False
    return True


def canonical_string(triangle_system):
    h = Hypergraph([list(t) for t in triangle_system])
    return h.incidence_graph().canonical_label().graph6_string()


def edges_of_system(triangles):
    edges = set()
    for t in triangles:
        for e in combinations(t, 2):
            edges.add(frozenset(e))
    return edges


def edge_is_addable(edge, edges, vertices):
    u, v = tuple(edge)
    for w in vertices:
        if w != u and w != v:
            if frozenset({u, w}) in edges and frozenset({v, w}) in edges:
                return False  # would complete a triangle
    return True


def is_edge_maximal(triangles, vertices):
    edges = edges_of_system(triangles)
    all_edges = {frozenset(e) for e in combinations(vertices, 2)}

    for e in all_edges - edges:
        if edge_is_addable(e, edges, vertices):
            return False  # still extendable
    return True


def build_triangle_maximal_complexes(vertices):
    all_triangles = sorted(combinations(vertices, 3))
    seen = set()
    results = []

    def backtrack(system, start_idx):
        canon = canonical_string(system)
        if canon in seen:
            return
        seen.add(canon)

        extended = False
        for i in range(start_idx, len(all_triangles)):
            t = all_triangles[i]
            if is_linear_with(system, t):
                extended = True
                system.append(t)
                backtrack(system, i + 1)
                system.pop()

        # Only add if no further triangle could be added
        if not extended:
            results.append(list(system))

    backtrack([], 0)
    return results

def complete_to_edge_maximal(triangle_systems, vertices):
    all_edges = set(frozenset(e) for e in combinations(vertices, 2))
    completed_systems = []

    for triangles in triangle_systems:
        triangle_edges = set()
        for tri in triangles:
            for e in combinations(tri, 2):
                triangle_edges.add(frozenset(e))

        bare_edges = list(all_edges - triangle_edges)
        completed_systems.append((triangles, bare_edges))

    return completed_systems
