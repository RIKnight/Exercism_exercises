# Name: sieve.R
# Purpose: exercism, R track, sieve; Implement the sieve of Eratosthenes
# Written by Z Knight, 2019.10.16
#
sieve <- function(limit) {
  if (limit == 1) {
    return(c())
  }
  range <- c(1:limit)
  # print(range)
  keep_mask <- rep(TRUE, limit)
  keep_mask[[1]] <- FALSE
  for (to_check in range) {
    if (keep_mask[[to_check]]) {
      base <- to_check
      # print(base)
      product <- base
      while (product < limit) {
        product <- product + base
        if (product %in% range) {
          keep_mask[[product]] <- FALSE
          # print(product)
        }
      }
    }
  }
  return(range[keep_mask])
}
