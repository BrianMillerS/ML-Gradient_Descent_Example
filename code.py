#!/usr/bin/env python

import numpy as np
import matplotlib.pyplot as plt


def compute_MAE_for_given_line(m, b, data):
    sum_of_errors = 0
    for i in range(len(data)):  # for each data point in the data set
        x = data[i, 0]  # get x value from row i and column 1
        y = data[i, 1]  # get y value from row i and column 0
        sum_of_errors += abs(y - (m * x + b))  # adds the difference between a known and predicted y values
    return sum_of_errors / len(data)  # returns MAE


def gradient_descent(initial_m, initial_b, data, epochs, learning_rate):
    m = initial_m
    b = initial_b
    for number in range(epochs):  # iterate through whole dataset for a set number of times
        for i in range(len(data)):  # for each data point in the data set
            x = data[i, 0]

            gradient_m = -x * (m * x + b) / abs(m * x + b)  # compute gradient of m
            gradient_b = -(m * x + b) / abs(m * x + b)  # compute gradient of b
            m -= (gradient_m * learning_rate)  # update m
            b -= (gradient_b * learning_rate)  # update b
    return m, b


def run_GD_best_fit(data):
    # set m and b to 0 and calculate MAE
    initial_m = 0.00000001
    initial_b = 0.00000001
    inital_MAE = compute_MAE_for_given_line(initial_m, initial_b, data)
    print("\tInitial MAE: {}".format(inital_MAE))

    # define hyper-parameters and run GD
    print("\tPerforming Stochastic Gradient Descent...")
    epochs = 1000
    constant_learning_rate = 0.0000003
    final_m, final_b = gradient_descent(initial_m, initial_b, data, epochs, constant_learning_rate)

    # recalculate MAE and print
    final_MAE = compute_MAE_for_given_line(final_m, final_b, data)
    print("\tFinal MAE: {}".format(final_MAE))
    print("\tFinal Equation: y={}x+{}\n".format("%.2f" % final_m, "%.2f" % final_b))  # m and b rounded to 2 decimal places

    return final_m, final_b, final_MAE


def run_LSM_best_fit(data):
    x_values = data[:, 0]
    y_values = data[:, 1]
    x_mean = np.mean(x_values)
    y_mean = np.mean(y_values)

    # calculate numerator for m
    m_numerator = 0
    for i in range(len(data)):  # for every x,y pair
        m_numerator += (x_values[i] - x_mean) * (y_values[i] - y_mean)

    # calculate denominator for m
    m_denominator = 0
    for x in x_values:
        m_denominator += (x - x_mean)**2

    # calculate m and b
    m = m_numerator / m_denominator
    b = y_mean - (m * x_mean)

    # calculate MAE and
    LSM_MAE = compute_MAE_for_given_line(m, b, data)
    print("\tMAE: {}".format(LSM_MAE))
    print("\tFinal Equation: y={}x+{}".format("%.2f" % m, "%.2f" % b))

    return m, b, LSM_MAE


def make_graph(data, m_GD, b_GD, MAE_GD, m_LSM, b_LSM, MAE_LSM):
    # set data and initialize scatter-plot
    x = list(data[:, 0])
    y = list(data[:, 1])
    plt.scatter(x, y, c='g')  # initialize the scatter-plot ('g'= make points green)

    # plot best fit line for GD
    fit_line_values_GD = [m_GD * i + b_GD for i in x]  # create a list of values that represent the best fit line for GD
    plt.plot(x, fit_line_values_GD, 'r')  # plot the best fit line over the actual scatter ('r'= make line red)

    # plot best fit line for LSM
    fit_line_values_LSM = [m_LSM * i + b_LSM for i in x]  # create a list of values that represent the best fit line for LSM
    plt.plot(x, fit_line_values_LSM, 'b')  # plot the best fit line over the actual scatter ('b'= make line blue)

    # add features to graph
    plt.axis([20, 80, 20, 125])  # set axis lengths [Xstart,Xend,Ystart,Yend]
    plt.xlabel('Distance Biked (m)')
    plt.ylabel('Calories Burned (kcal)')
    plt.title('Line of Best Fit with GD and LSM')
    plt.text(65, 45, r'GD MAE={}'.format("%.2f" % MAE_GD), color='r')
    plt.text(25, 110, r'LSM MAE={}'.format("%.2f" % MAE_LSM), color='b')
    plt.text(65, 40, r"y={}x+{}".format("%.2f" % m_GD, "%.2f" % b_GD), color='r')
    plt.text(25, 105, r"y={}x+{}".format("%.2f" % m_LSM, "%.2f" % b_LSM), color='b')

    plt.show()  # display the created graph in a popup window
    # plt.savefig('Output_Figure.png')  # optional: save figure as a png file in current working directory


if __name__ == '__main__':
    # import data
    data = np.genfromtxt("data.csv", delimiter=",", skip_header=1)  # import data as np array without the header row

    # Model best fit with GD
    print("Calculating line of best fit using Gradient Descent:")
    m_GD, b_GD, MAE_GD = run_GD_best_fit(data)

    # Model best fit with LSM
    print("Calculating line of best fit using Least Squares Method:")
    m_LSM, b_LSM, MAE_LSM = run_LSM_best_fit(data)

    # graph results
    make_graph(data, m_GD, b_GD, MAE_GD, m_LSM, b_LSM, MAE_LSM)
