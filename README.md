# Trajectories
The `trajectories` Python package provides tools for geometric analysis of time series data.   


## Making Pretty Pictures

## Internal Data structures

**Samples** Object: a dictionary of samples, paired with their names
```
{sample_a:[run1, run2], sample_b:[run1, run2]...}
```
**Sample** Object: a dictionary with runs assigned to the data
```
sample._instances = {samplea_run1: <instance holding points>, samplea_run2: <instance holding points>}
```

**Instance** Object: a list of points.
```
instance = [[t0, xCoord, yCoord],[t1, xCoord, yCoord],[t2, xCoord, yCoord]]
```

**Trajectory** Object: a list of point objects.
**Point** Object: the value of each dimension at some time.
