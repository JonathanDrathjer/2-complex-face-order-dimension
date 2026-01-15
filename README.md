# face order dimension of 2-complexes with edge degree at most one

This project generates all **maximal two complexes with edge degree at most one** over a given vertex set, computes their **face order** and determines its **poset dimensions** using a SAT-based method.

## 📂 Contents

- `complex_utils.py`: provides all functions required to generate all **maximal two complexes with edge degree at most one** over a given vertex set.
- `small_systems_test.py`: Computes the **face order dimension** and **realizers** of all **maximal two complexes with edge degree at most one** for a specified number of vertices. Also verifies the correctness of the realizer.
- `sample_result_9vert.txt`: Output from `small_systems_test.py` for 9 vertices

## Dependencies

- **Python 3.10+**
- **[SageMath](https://www.sagemath.org/)** (for poset and hypergraph utilities)
- **`dimension.py`** from the [productdim repository](https://github.com/maxitw/productdim)  
  This provides the `sat_dimension` function used to compute poset dimensions via SAT solving.
- **[Kissat SAT Solver](https://github.com/arminbiere/kissat)**  
  This is required by `dimension.py`. Make sure `kissat` is available in your system’s PATH.






