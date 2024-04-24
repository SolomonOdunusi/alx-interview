# 0x07. Rotate 2D Matrix
`Algorithm`
`Python`


To rotate a 2D matrix 90 degrees clockwise in-place, you can follow these steps:

Transpose the matrix (swap elements across the diagonal).
Reverse each row of the transposed matrix.

Time Complexity: O(N^2), since each element in the matrix is touched once.
Space Complexity: O(1), as the space used does not scale with the size of the input matrix but remains constant (only one temporary variable used).

