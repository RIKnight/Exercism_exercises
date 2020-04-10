# Name: acronym.R
# Purpose: exercism, R track, acronym: 
#    Convert a phrase to its acronym.
# Written by Z Knight, 2020.04.09
#
acronym <- function(input) {
    words <- unlist(strsplit(input, "[-_ ]+"))
    letters <- ""
    for (word in words) {
        letters <- paste0(letters, substring(word, 1, 1))
    }
    acronym <- toupper(letters)
}
