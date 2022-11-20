from __future__ import print_function
from matplotlib import pyplot as plt
import numpy as np
from scipy.optimize import curve_fit

dataX = []
dataY = []

datafile = open('data.txt', "r")
line_list = datafile.readlines()

datafile.close()



for line in line_list:
    dataSplit = line.split(" ")
    x = float(dataSplit[0])
    y = float(dataSplit[1])

    dataX.append(x)
    dataY.append(y)

#Convert into numpy arrays 
dataX = np.asarray(dataX)
dataY = np.asarray(dataY)


# Define the Gaussian function
def Gauss(x, A, B):
    y = A*np.exp(-1*B*x**2)
    return y
parameters, covariance = curve_fit(Gauss, dataX, dataY)

fit_A = parameters[0]
fit_B = parameters[1]

fit_y = Gauss(dataX, fit_A, fit_B)
plt.plot(dataX, dataY, 'o', label='Data')
plt.plot(dataX, fit_y, '-', label='fit')
plt.legend()
plt.show()