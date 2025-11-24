# test_triangle_systems.py
from lts_gen import build_linear_triangle_systems
from complexutils import facets_to_inclusion_poset
from dimension import sat_dimension
from functools import reduce
from sage.all import Poset


def linext_to_relation(linext):
    # Return all pairs (x < y) based on total order
    return set(
        (linext[i], linext[j])
        for i in range(len(linext))
        for j in range(i + 1, len(linext))
    )


def log(msg, f):
    print(msg)
    f.write(msg + "\n")


output_path = "triangle_system_results.txt"

with open(output_path, "w") as log_file:
    for n in range(11, 12):  # vertex sets from 3 to 7 inclusive
        log(f"\n===== Triangle Systems on {n} Vertices =====", log_file)
        vertices = list(range(1, n + 1))
        systems = build_linear_triangle_systems(vertices)

        log(f"Total systems: {len(systems)}\n", log_file)

        all_verifications_passed = True
        high_dimension_systems = []

        for idx, system in enumerate(systems, 1):
            log(f"System {idx}:", log_file)

            sorted_triangles = sorted([tuple(sorted(t)) for t in system])
            log(f"  Triangles: {sorted_triangles}", log_file)

            try:
                P = facets_to_inclusion_poset(system)
                dim, realizer = sat_dimension(P, certificate=True)
                log(f"  Dimension: {dim}", log_file)
                log("  Realizer:", log_file)
                for linext in realizer:
                    readable = [sorted(list(e)) for e in linext]
                    log(f"    {readable}", log_file)

                if dim > 4:
                    high_dimension_systems.append(idx)

                # -- Verification Step --
                relations = [linext_to_relation(le) for le in realizer]
                intersection_relation = reduce(set.intersection, relations)

                reconstructed_poset = Poset(
                    (list(P), intersection_relation), cover_relations=False
                )

                # Compare with original poset
                if reconstructed_poset == P:
                    log("Verification passed!", log_file)
                else:
                    log("Verification failed!", log_file)
                    all_verifications_passed = False

                log("", log_file)  # blank line above
                log("-" * 50, log_file)
                log("", log_file)  # blank line below

            except Exception as e:
                log(f"ERROR: {e}", log_file)

        if all_verifications_passed:
            log("All Verifications passed!", log_file)
        else:
            log("Some Verification failed!", log_file)

        log("High Dimension Systems (dimension > 4):", log_file)
        for high_dim_idx in high_dimension_systems:
            log(f"  System {high_dim_idx}", log_file)
