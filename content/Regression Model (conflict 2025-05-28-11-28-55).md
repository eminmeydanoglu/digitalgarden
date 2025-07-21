---
publish: 1
---
#rw
Regression: A type of supervised learning algorithm used to predict new values based on the "true" data. After we give it 50 house size and price value, our function can make a price prediction (y-hat) of a house size of x. (the feature)
![[Regression Model-20240506171158332.webp|325]]

# Representing the function f mathematically.
One can represent this function linearly (linear regresison), which seems the most primitive method! Linear regression is univariate, meaning consists of only one variable. We only take our guess by the size of the house, but not for example where it is located and more.
A linear regression function is something like wx + b. w and b are parameters of the regression model, adjusted as the model learns from the data. They’re also referred to as “coefficients” or “weights”

## Cost Function
When we produce this function from the "true" data, say that one of them is  (2, 10). Well, the prediction for 2 is not going to be 20, indeed. Here is a squared error cost function. 
![[Regression Model-20240506173646577.webp]]
Goal of linear regression is to minimize cost function J. We should have the most appropriate w and b so that J is minimum. For a data that fits perfectly to y =3x, we choose the linear regression function as w = 3 and b = 0 and the error is 0. ! y hat and y is equal. 
![[Regression Model-20240506175300787.webp|537]]

## Model with more than 1 feature:
![[Regression Model-20240609105530336.webp|524]]
Is now a dot product.
