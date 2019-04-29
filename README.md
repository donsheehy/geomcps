# Trajectory
Welcome to the trajectory package. This is to help visualize complex data structures and time warping.

## Config File
To use this package, you will need to add a .config file to the folder where your data reside. Create the config file by running config.py. The structure of the config file is as follows.

### Sample config
If running config.py doesn't work, or you want the dirty details, here's what goes into the config file:
```
.csv
64
64
```
The first line represents the extension of the data files. These extensions are currently supported: csv, tsv. The second and third lines represent how much metadata you'd like to save for each file - the idea is to name your data as you go so that you can find it again if you choose to extend this package.

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
