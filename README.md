
Stochastic Gradient Descent(GD) for Linear Regression:

This post is inspired by Matt Nedrich's [blog post](https://spin.atomicobject.com/2014/06/24/gradient-descent-linear-regression/). This is a great introduction to GD, but I want to delve into the math a little more, and use a different loss function. I highly recommend reading Matt's blog post and also watching Siraj Raval's [youtube video](https://www.youtube.com/watch?v=xRJCOz3AfYY) on this topic. Just to be clear there are faster and less computationally expensive ways to perform linear regression, but we are just using it as a way to show how gradient descent works.

Let's begin with a refresher of the linear regression setup. The goal is to generate the line that is closest to as many data points as possible. Hence we can define our error (or loss) function to be representative of the mean distance between all data points and a given line. Let’s use the Mean Absolute Error as our loss function:

LOSS FUNCTION

But since this is an example of [Stochrastic GD and not Batch GD](https://stats.stackexchange.com/questions/49528/batch-gradient-descent-versus-stochastic-gradient-descent), thus for each x,y data point pair along the way we can calculate the Absolute Error (same thing as MAE but just not averaged).

J DEFINITION

At this point, we need to find the line out of all possible lines that minimizes our loss function. Let's visualize this by graphing all possible m and b values along with their corresponding error.

GD VISUALIZATION

You can see that the arrow indicates our goal, but how do we get there? First we will initialize our m and b values to 0, then we will iteratively use gradient descent to change our m and b values in the direction that minimizes our loss. [The gradient](https://en.wikipedia.org/wiki/Gradient) is the collection of all the partial derivatives for a given multivariable function. 
Here is a basic usage example:

BASIC EXAMPLE

But what do these numbers truly represent? "The gradient points in the direction of the greatest rate of increase of the function, and its magnitude is the slope of the graph in that direction"([wikipedia](https://en.wikipedia.org/wiki/Gradient)). This is critical, for in our case if we take the gradient of our loss function then we can tell how the error changes as one of our variables changes. 

Let's visualize this with another example. Consider that we want to know how the error changes as b changes. The picture below is the same error surface as before, but this time let's take the partial derivative of J with regard to b (this means that m is held constant).

PARTIAL DERIVATIVE 1

PARTIAL DERIVATIVE 2

Images derived from [Wikipedia](https://en.wikipedia.org/wiki/Partial_derivative).

The arrow is up because the "points in the direction of the greatest rate of increase", yet we want to change b in the opposite direction. Thus we can redefine b to move in the opposite direction as the gradient.

REDEFINEM AND B

Note the learning rate is just a hyper-parameter that influences how quickly these changes to m and b occur.

Now we can expand out our partial derivatives:

EXPAND DERIVATIVES

Here is the piece of code that encapsulates the whole gradient descent step

GD_CODE

After running the code for 1000 epochs and with a learning rate of 0.0000003 we see that the we have converged to our answer. Let's also include a well known algebraic linear regression technique called the [Least Squares Method](https://www.youtube.com/watch?v=JvS2triCgOY&t=435s)(LSM) to benchmark our results.

TERMINAL OUTPUT

Finally, we can visualize our results!














