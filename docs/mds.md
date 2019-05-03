# Multidimensional scaling

This is used to scale down high dimensional data in order for it to be visualized in low dimensions.
The function works by taking as input a list of any objects which can have a distance metric applied to them.
For example a list of points, trajectories, etc. The metric must be the squared distance.
The algorithm works in a similar way to Pricipal Component Analysis (PCA).
This method reduces the dimensionality by first computing the square pairwise distance matrix between all pairs of objects.
To get a matrix like the one used in PCA we applt double centering. Then the normal PCA algorithm is followed.
The resulting matrix is decomposed into eigenvalues and eigenvectors.
We sort these in order of decreaseing eigenvalue since the largest eigenvalues correlate to the directions of most variance.
Our solution is then the eigenvector matrix multiplied by the squareroot of the eigenvalue matrix.
To plot in a reduced m dimensions, take the first m eigenvectors treating each as a coordinate.
The implementation in this package returns a list of points in the requested dimension.

For a more in depth explanation of the mathematics [check this presentation](https://www.stat.pitt.edu/sungkyu/course/2221Fall13/lec8_mds_combined.pdf)