# Name: leap.R
# Purpose: exercism, R track, Leap
# Written by Z Knight, 2019.10.05
#  Modified to and and or instead of nested loops; ZK, 2019.10.05
#  Modified to use a single line instead of an if block; ZK, 2019.10.05
#
leap <- function(year) {
  year %% 4 == 0 & (year %% 100 != 0 | year %% 400 == 0)
}
