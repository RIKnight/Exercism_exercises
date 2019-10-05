# Name: leap.R
# Purpose: exercism, R track, Leap
# Written by Z Knight, 2019.10.05
#
leap <- function(year) {
  if (year %% 4 == 0) {
    if (year %% 100 == 0) {
      if ( year %% 400 == 0) {
        return(TRUE)
      }
      return(FALSE)
    }
    return(TRUE)
  }
  return(FALSE)
}
