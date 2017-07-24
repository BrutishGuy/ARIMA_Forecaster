Simple Sequence Segmenting
==========================

This repository contains Python code I wrote for forecasting 1-D time series using a simple ARIMA model. 

The code is *not* optimized for performance in any way, but it is useful for 
experimenting and data exploration.

Requirements
------------

The segmenting algorithms use [NumPy's][numpy] least squares fitting routine, so naturally it depends on [NumPy][numpy]. The script
requires [matplotlib][mpl] to display the plots. It requires [pandas] for reading and writing of csv-style data. It also requires [sklearn] for the RMSE metric used

Example
-------

You can run the code to see example output by running the simple_forecaster.py script.

The example uses shampoo sales data (included) and also the UCL ML Household Power Consumption data (must be downloaded and put into the household_power_consumption folder)


[keogh]: http://www.cs.ucr.edu/~eamonn/icdm-01.pdf "Keogh et al. An Online Algorithm for Segmenting Time Series"
[numpy]: http://numpy.scipy.org "NumPy"
[mpl]: http://matplotlib.sourceforge.net "Matplotlib"
[ecg]: http://myweb.msoe.edu/~martynsc/signals/ecg/ecg.html "ECG Data"
[pandas]: http://pandas.pydata.org/ "Pandas"
[sklearn]: http://scikit-learn.org/stable/ "Scikit-Learn"
