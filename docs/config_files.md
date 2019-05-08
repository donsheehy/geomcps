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
