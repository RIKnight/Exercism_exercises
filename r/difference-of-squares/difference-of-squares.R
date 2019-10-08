# Name: difference-of-squares.R
# Purpose: exercism, R track, difference-of-squares
#     this function takes a natural_number
#     and returns the difference-of-squares (\Sigma_1^n x)^2 - \Sigma_1^n x^2
# Written by Z Knight, 2019.10.07
#
difference_of_squares <- function(natural_number) {
  sum_squared <- (natural_number*(natural_number+1)/2)^2
  sum_of_squares <- sum(c(0:natural_number)^2)
  difference_of_squares <- sum_squared - sum_of_squares 
}

