# Name: hamming.R
# Purpose: exercism, R track, hamming: 
#    Calculate the Hamming difference between two DNA strands.
# Written by Z Knight, 2020.04.10
#   Modified to use strsplit and multiple n_acid variables; ZK, 2020.06.14
#   Fixed list of vector indexing problem; ZK, 2020.06.15
#
hamming <- function(strand1, strand2) {
    distance <- 0
    n_acids1 = nchar(strand1)
    n_acids2 = nchar(strand2)
    if (n_acids1 != n_acids2) {
        stop("strands of unequal length!")
    }
    
    acids1 = strsplit(strand1, "")
    acids2 = strsplit(strand2, "")
    comparison <- acids1[[1]] == acids2[[1]]
    num_matches = sum(comparison)
    
    return(n_acids1-num_matches)
}
