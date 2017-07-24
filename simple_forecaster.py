from pandas import read_csv
from pandas import datetime
from matplotlib import pyplot
from statsmodels.tsa.arima_model import ARIMA
from statsmodels.tsa.arima_model import ARIMAResults
from sklearn.metrics import mean_squared_error

verbose = 1 # boolean 1 or 0 indicating if you would like verbose output for results, i.e. print values or not
N = 2000 # number of data points to use. keep in mind the runtime when selecting this
fraction = 0.95  # fraction of data to use as training and test, e.g. 0.95 will yeild 95% training and 5% test data

Location = 'household_power_consumption\household_power_consumption_small.csv' # location of dataset

df =  read_csv(Location, sep=';', header=0) # read in data. remember to change sep character if necessary
X = list(map(float, df.Voltage.as_matrix()))[:N] # turn each element of the necessary column to float and into a list, take N data elements

# paritition data into test and training subsets using fraction parameter above
size = int(len(X) * fraction)
train, test = X[0:size], X[size:len(X)]

# copying over the training data into a 'history' array
history = [x for x in train]

# list to store predictions
predictions = list()

if verbose:
    print('One-Step Prediction\tExpected')
for t in range(len(test)):
    model = ARIMA(history, order=(5,1,0))
    model_fit = model.fit(disp=0)
    output = model_fit.forecast()
    yhat = output[0]
    predictions.append(yhat)
    obs = test[t]
    history.append(obs)
    if verbose:
        print('%f\t%f' % (yhat, obs))

if verbose:
    print(model_fit.summary()) # print a little model summary of statistics. kinda boring

error = mean_squared_error(test, predictions) # calculate RMSE error over all predictions and test datapoints

if verbose:
    print()
    print('Test MSE: %.3f' % error)

# write data to file. will rewrite this using dataframes and pandas to condense coding required for new datasets
f = open('predictions.csv','w')
f.write('Data,Prediction\n')
for i in range(len(predictions)):
    f.write(str(test[i])+','+str(predictions[i][0])+'\n')
f.close()

# plot values for visuals
pyplot.plot(test, label='Ground truth data')
pyplot.plot(predictions, color='r', label='Predicted data')
# plot info, remember to change depending on dataset
pyplot.legend()
pyplot.xlabel('Point number [arb. units]')
pyplot.ylabel('Voltage [V]') # change this depending on data set

pyplot.show()

