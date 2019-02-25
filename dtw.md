# Dynamic Time Warping

## What Is IT
DTW is a VERY commonly used metric to process time dependent data.
[Here](https://en.wikipedia.org/wiki/Dynamic_time_warping) is the wikipedia article explaining what basic time warping is.
It is used in a lot of electronics like smart watches or other health gadgets to process the users data.
In the one-dimensional case the point of the algorithm is search for possible shifts in the data.
For example there could be two trajectories which are the same hoever one is shifted by some units to the right/left.
This results in an excessively large value for a metric like L2-norm.
With time warping it searches for the shortest distance between points thus making the trajectories "in phase".
Heres a good image of what it does:

![alt text](https://upload.wikimedia.org/wikipedia/commons/a/ab/Dynamic_time_warping.png "Warp Example")

Most algorithms are only for one-dimensional cases however [this](http://www.cs.ucr.edu/~eamonn/Multi-Dimensional_DTW_Journal.pdf)
article seems to explain a way of extending it to multiple dimensions.
When the algorithm is extended to multiple dimensions there seem to be two ways to handle the data.
The two methods use either *dependent* or *independent* warping.
Apparently before everyone did not think there was much of a difference however the article explains why there is
and which one you should use.

## How does it work
Looking at the one dimensional case, assume we have two trajectories P and Q with lengths m and n.
This function would create and m by n table and compute every distance (based on some specified metric) between all
m X n pairs of values.
It then traverses a reverse min path through the table summing adding on the minimum of the
three previous neighbors and then moving to that spot in the table.
Now when extending to multiple dimensions there are two methods used.

### Independent DTW
This method splits the points up by dimension into N one-dimensional trajectories.
DTW is then performed N-times trajectory pairs with whatever 1-D norm.
This method results in every dimension having its own warping.

### Dependent DTW
Here the normal DTW algorithm is used once but our norm is N-dimensional.
This causes all dimensions to be warped equally.

## Some other sources
[Good Video](https://www.youtube.com/watch?v=_K1OsqCicBY) explaining the 1-D case
Something interesting came up when the path was bounded in the given table