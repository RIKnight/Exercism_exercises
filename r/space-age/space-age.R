# Name: space-age.R
# Purpose: exercism, R track, space-age
# Written by Z Knight, 2019.10.14
#
library(dict)

earth_years_per_yr <- dict()
earth_years_per_yr[["mercury"]] <- 0.2408467
earth_years_per_yr[["venus"]] <- 0.61519726
earth_years_per_yr[["earth"]] <- 1.0
earth_years_per_yr[["mars"]] <- 1.8808158
earth_years_per_yr[["jupiter"]] <- 11.862615
earth_years_per_yr[["saturn"]] <- 29.447498
earth_years_per_yr[["uranus"]] <- 84.016846
earth_years_per_yr[["neptune"]] <- 164.79132

sec_per_earth_yr <- 31557600

space_age <- function(seconds, planet) {
  earth_years <- seconds/sec_per_earth_yr/earth_years_per_yr[[planet]]
  round(earth_years, 2)
}
