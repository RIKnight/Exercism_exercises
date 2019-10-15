# Name: grains.R
# Purpose: exercism, R track, grains
#     The function square takes an integer 1-64, for squares on the chess board
#       and returns the power 2^(n-1).
#     The function total tells how many grains it takes to fill the board.
# Written by Z Knight, 2019.10.14
#
square <- function(n) {
  if (n < 1 || n > 64) {
    stop("Input outside of chessboard range 1-64. Exiting.")
  } else if (n == 1) {
    return(1)
  } else {
    return(2*square(n-1))
  }
}

total <- function() {
  square(64)*2-1
}

