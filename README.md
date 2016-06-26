# About
An implementation of differential evolution based on Wikipedia (https://en.wikipedia.org/wiki/Differential_evolution).

Given a function **f**, the code will try to find the arguments which *maximises* the value of **f**.

There are 2 terminating conditions:
* When the maximum number of iterations has been reached
* When the best value of f (within a generation) improves less than a minimum threshold

**Testing**

The default test tries to maximise the function `f(x,y) = -((x+5)^2 + 3 * \sqrt{|y+2| + 7})`.

To optimise your own numerical function:
* Replace `def f(args): ...` with your own function
* Update `argn`
* [Optional] Modify tuning parameters such as `N`, `DW`, `CR`, `max_iter` and `min_eps`

# Blog post
To learn more, read the blog post here: http://davinchoo.com/2016/06/26/differential-evolution/
