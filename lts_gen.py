from itertools import combinations
from sage.all import Hypergraph


def is_linear_with(triangles, new_triangle):
    for t in triangles:
        if len(set(t) & set(new_triangle)) > 1:
            return False
    return True


def canonical_string(triangle_system):
    h = Hypergraph([list(t) for t in triangle_system])
    return h.incidence_graph().canonical_label().graph6_string()


def build_linear_triangle_systems(vertices):
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
