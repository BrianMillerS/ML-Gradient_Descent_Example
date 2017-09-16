# ML-Gradient_Descent_Example

Stochrastic Gradient Descent(GD) for Linaer Regression:
This post is inspired by Matt Nedrich's [blog post](https://spin.atomicobject.com/2014/06/24/gradient-descent-linear-regression/). This is a great introduction to GD, but I want to delve into the math a little more, and use a different loss function. I highly recommend reading Matt's blog post and also watching Siraj Raval's [youtube video](https://www.youtube.com/watch?v=xRJCOz3AfYY) on this topic.

Let's begin with a refresher of [the gradient](https://en.wikipedia.org/wiki/Gradient), the collection of all the partial derivatives for a given multivariable function.

Let's look at a simple example:

![alt text](https://raw.githubusercontent.com/BrianSMiller/ML-Gradient_Descent_Example/master/Math2.png)

Furthermore, "the gradient points in the direction of the greatest rate of increase of the function, and its magnitude is the slope of the graph in that direction"([wikipedia](https://en.wikipedia.org/wiki/Gradient)). This is critical, for in this example the gradient is used to minimize our loss function. As our goal is linear regression, we can visualize our loss surface as such...

![alt text](https://raw.githubusercontent.com/BrianSMiller/ML-Gradient_Descent_Example/master/GD_Visualization2.png)

The red arrow indicates what we want, the global minimum, but since the gradient "points in the direction of the greatest rate of increase" this is in the total oposite direction (with an arrow pointing up) 
Lets use the Mean Absolute Error as our loss function:
#![alt text](https://raw.githubusercontent.com/BrianSMiller/ML-Gradient_Descent_Example/master/Math5.png)
But since this is an example of [Stochrastic GD and not Batch GD](https://stats.stackexchange.com/questions/49528/batch-gradient-descent-versus-stochastic-gradient-descent), thus for each datapoint along the way we can calculate the Absolute Error (same thing as MAE but just not averaged).
#![alt text](https://raw.githubusercontent.com/BrianSMiller/ML-Gradient_Descent_Example/master/Math3.png)



#![alt text](https://raw.githubusercontent.com/BrianSMiller/ML-Gradient_Descent_Example/master/Math4.png)

#![alt text](https://raw.githubusercontent.com/BrianSMiller/ML-Gradient_Descent_Example/master/Math6.png)

#![alt text](https://raw.githubusercontent.com/BrianSMiller/ML-Gradient_Descent_Example/master/Output_Figure.png)








