# Name: perfect-numbers.R
# Purpose: exercism, R track, perfect-numbers; Determine whether a number is "perfect"
# Written by Z Knight, 2019.10.14
#
is_factor <- function(to_check, maybe_factor){
  to_check %% maybe_factor == 0
}

number_type <- function(to_check){
  if (to_check == 1){
    return("deficient")
  }
  sum <- 0
  for (maybe_factor in 1:(to_check-1)){
    if (is_factor(to_check, maybe_factor)){
      sum <- sum + maybe_factor
    }
  }
  if (sum > to_check){
    return("abundant")
  }
  if (sum == to_check){
    return("perfect")
  }
  return("deficient")
}

