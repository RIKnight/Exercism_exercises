# Name: collatz-conjecture.R
# Purpose: exercism, R track, collatz conjecture: 
#   given a number n, find the number of steps required to reach 1
# Written by Z Knight, 2019.10.16
#
collatz_step_counter <- function(num) {
  if (num < 1) stop("num < 1")
  counter <- 0
  while (num > 1) {
    if (num %% 2 == 0) {
      num <- num / 2
    } else {
      num <- num *3 +1
    }
    counter <- counter +1
  }
  return(counter)
}

collatz_step_counter <- Vectorize(collatz_step_counter)

