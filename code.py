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
    return [m, b]


def make_graph(data, final_m, final_b, inital_MAE, final_MAE):
    # set data and initialize scatterplot
    x = list(data[:, 0])
    y = list(data[:, 1])
    plt.scatter(x, y)

    # plot best fit line
    slope = final_m
    intercept = final_b
    fit_line_values = [slope * i + intercept for i in x]  # create a list of values that represent the best fit line
    plt.plot(x, fit_line_values, 'r')  # plot the best fit line over the actual scatter ('r'= make line red)

    # add features to graph
    plt.axis([0, 100, 0, 150])  # set axis lengths [Xstart,Xend,Ystart,Yend]
    plt.xlabel('Distance Biked (m)')
    plt.ylabel('Calories Burned (kcal)')
    plt.title('Best Fit Line with GD')
    plt.text(70, 20, r'Initial MAE={}'.format("%.2f" % inital_MAE))  # display initial MAE, rounded to 2 decimal places
    plt.text(70, 10, r'Final MAE={}'.format("%.2f" % final_MAE))  # display final MAE, rounded to 2 decimal places
    plt.text(75, 110, r"y={}x+{}".format("%.2f" % final_m, "%.2f" % final_b))  # display final best fit equation, rounded to 2 decimal places
    plt.show()  # display the created graph in a popup window
    # plt.savefig('Output_Figure.png')  # optional: save figure as a png file in current working directory


if __name__ == '__main__':
    # import data and calculate initial MAE
    data = np.genfromtxt("data.csv", delimiter=",", skip_header=1)  # import data as np array without the header row

    initial_m = 0.00000001
    initial_b = 0.00000001
    inital_MAE = compute_MAE_for_given_line(initial_m, initial_b, data)
    print("Initial MAE: {}".format(inital_MAE))

    # define hyperparameters and run GD
    print("Performing Stochastic Gradient Descent...")
    epochs = 1000
    constant_learning_rate = 0.0000003
    final_m, final_b = gradient_descent(initial_m, initial_b, data, epochs, constant_learning_rate)

    # recalculate MAE
    final_MAE = compute_MAE_for_given_line(final_m, final_b, data)
    print("Final MAE: {}".format(final_MAE))
    print("\nFinal Equation: y={}x+{}".format("%.2f" % final_m, "%.2f" % final_b))

    # create graph
    make_graph(data, final_m, final_b, inital_MAE, final_MAE)
