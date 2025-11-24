from sage.all import Poset
from itertools import combinations

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
