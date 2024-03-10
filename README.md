<h1 align="center">Understanding the math behind your model: Stochastic Gradient Descent</h1>  

<h3>Summary:</h3>  

This post is inspired by Matt Nedrich's [blog post](https://spin.atomicobject.com/2014/06/24/gradient-descent-linear-regression/) which is a great introduction to gradient descent, but I want to delve into the math a little more, and use a different loss function. We will be using a toy data set to predict the number of calories burned given how far an athlete rode his/her bike. We will use gradient descent to perform a simple linear regression, and then benchmark our results using the least squares method. To be clear, there are faster and less computationally expensive ways to perform linear regression, but we are just using it as a platform to show how gradient descent works.

Let's begin with a refresher of the linear regression setup. The goal is to generate the line that is closest to as many data points as possible. Hence we can define our error (or loss) function to be representative of the mean distance between all data points and our line. Let’s use the Mean Absolute Error as our loss function:

![alt text](https://raw.githubusercontent.com/BrianSMiller/ML-Gradient_Descent_Example/master/Math1.png)

Since this is an example of Stochrastic GD and not Batch GD, so for each x,y data point pair along the way we can calculate the Absolute Error (same thing as MAE but just not averaged).

![alt text](https://raw.githubusercontent.com/BrianSMiller/ML-Gradient_Descent_Example/master/Math2.png)

At this point, we need to find the line out of all possible lines that minimizes our loss function. Let's visualize this by graphing all possible m and b values along with their corresponding error.

![alt text](https://raw.githubusercontent.com/BrianSMiller/ML-Gradient_Descent_Example/master/GD_Visualization.png)

You can see that the arrow indicates our goal, but how do we get there? First we will initialize our m and b values to 0, then we will iteratively use gradient descent to change our m and b values in the direction that minimizes our loss function. [The gradient](https://en.wikipedia.org/wiki/Gradient) is the collection of all the partial derivatives for a given multivariable function. 
Here is a basic usage example:

![alt text](https://raw.githubusercontent.com/BrianSMiller/ML-Gradient_Descent_Example/master/Math3.png)

The gradient points in the direction of the greatest rate of increase of the function, and its magnitude is the slope of the graph in that direction. This is critical, for in our case if we take the gradient of our loss function then we can tell how the error changes as one of our variables change. 

Let's visualize this with another example. Consider that we want to know how the error changes as b changes. The picture below is the same error surface as before, but this time let's take the partial derivative of J with regard to b (this means that m is held constant).

![alt text](https://raw.githubusercontent.com/BrianSMiller/ML-Gradient_Descent_Example/master/Partial_Derivative.png)

Now plotting error vs b in two dimensional space.

![alt text](https://raw.githubusercontent.com/BrianSMiller/ML-Gradient_Descent_Example/master/Partial_Derivative2.png)

The arrow is up because the gradient points in the direction of the greatest rate of increase, yet we want to change b in the opposite direction. Thus we can redefine b to move in the opposite direction as the gradient. Note the learning rate is just a hyper-parameter that influences how quickly these changes to m and b occur.

![alt text](https://raw.githubusercontent.com/BrianSMiller/ML-Gradient_Descent_Example/master/Math4.png)

Now we can expand out our partial derivatives:

![alt text](https://raw.githubusercontent.com/BrianSMiller/ML-Gradient_Descent_Example/master/Math5.png)

Here is the piece of code that encapsulates the whole gradient descent step.

![alt text](https://raw.githubusercontent.com/BrianSMiller/ML-Gradient_Descent_Example/master/GD_Code.png)

After running the code for 1000 epochs and with a learning rate of 0.0000003, we have converged to our answer. Let's also include a well known algebraic linear regression technique called the Least Squares Method (LSM) to benchmark our results.

![alt text](https://raw.githubusercontent.com/BrianSMiller/ML-Gradient_Descent_Example/master/Terminal_Output.png)

Finally, we can visualize our results!

![alt text](https://raw.githubusercontent.com/BrianSMiller/ML-Gradient_Descent_Example/master/Output_Figure.png)












