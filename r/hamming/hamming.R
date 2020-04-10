# Name: hamming.R
# Purpose: exercism, R track, hamming: 
#    Calculate the Hamming difference between two DNA strands.
# Written by Z Knight, 2020.04.10
#
hamming <- function(strand1, strand2) {
    distance <- 0
    n_acids = nchar(strand1)
    if (n_acids != nchar(strand2)) {
        stop("strands of unequal length!")
    }
    
    for (i in c(1:n_acids)) {
        acid1 = substring(strand1, i, i)
        acid2 = substring(strand2, i, i)
        # print(c(i, acid1, acid2))
        if (acid1 != acid2) {
            distance <- distance +1
        }
    }
    return(distance)
}
