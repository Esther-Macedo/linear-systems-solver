# linear-systems-solver
Solves square linear systems trough gauss elimination (no or partial pivoting) and performs L U decomposition of the  coeficient matrix. 

## commands
[x] a: coeficient matrix input -> recieves an integer 'n' (sistem size) and n lines of the coeficient matrix. No output should be expected.
[x] c: constant vector input -> expects n one number lines. No output should be expected.
[x] p: prints system current state, both a and c commands must be ran first.
[x] s: solves system via gauss elimination with no pivoting and prints solution vector.
[x] r: solves system via gauss elimination with partial pivoting and prints solution vector.
[x] l: prints L U decomposition of the coeficient matrix (constant vector doesn't need to be inputed).
[x] e: terminates command sequence