# Linear Triangle Systems

This project generates all **maximal linear triangle systems** over a given vertex set, computes their **inclusion posets**, and determines their **order dimensions** using a SAT-based method.

## 📂 Contents

- `lts_gen.py`: Generates all **maximal linear triangle systems** over a given vertex set.
- `complexutils.py`: Provides a function to generate the **inclusion poset** of a simplicial complex from its facets.
- `small_systems_test.py`: Computes the **order dimension** and **realizers** of all maximal linear triangle systems for a specified number of vertices. Also verifies the correctness of the realizer.
- `lts_dimensions_9_vert.txt` Output from `small_systems_test.py` for 9 vertices

## Dependencies

- **Python 3.10+**
- **[SageMath](https://www.sagemath.org/)** (for poset and hypergraph utilities)
- **`dimension.py`** from the [productdim repository](https://github.com/maxitw/productdim)  
  This provides the `sat_dimension` function used to compute poset dimensions via SAT solving.
- **[Kissat SAT Solver](https://github.com/arminbiere/kissat)**  
  This is required by `dimension.py`. Make sure `kissat` is available in your system’s PATH.

