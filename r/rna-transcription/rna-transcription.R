# Name: rna-transcription.R
# Purpose: exercism, R track, rna-transcription: 
#    Given a DNA strand, return its RNA complement (per RNA transcription).
# Written by Z Knight, 2021.11.05
#
to_rna <- function(dna) {
    acids = unlist(strsplit(dna, ""))
    transcription = ""
    for (acid in acids) {
        if      (acid == "G") {transcription <- paste(transcription, "C", sep="")}
        else if (acid == "C") {transcription <- paste(transcription, "G", sep="")}
        else if (acid == "T") {transcription <- paste(transcription, "A", sep="")}
        else if (acid == "A") {transcription <- paste(transcription, "U", sep="")}
        else {stop("invalid input")}
    }

    transcription
}
