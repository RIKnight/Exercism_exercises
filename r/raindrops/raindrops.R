# Name: raindrops.R
# Purpose: exercism, R track, raindrops
# Written by Z Knight, 2019.10.16
#
raindrops <- function(number) {
  result <- ""
  if (number %% 3 == 0) result <- paste0(result, "Pling")
  if (number %% 5 == 0) result <- paste0(result, "Plang")
  if (number %% 7 == 0) result <- paste0(result, "Plong")
  if (result == "") return(toString(number))
  return(result)
}
