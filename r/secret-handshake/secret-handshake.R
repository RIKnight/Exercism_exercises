# Name: secret-hanshake.R
# Purpose: exercism, R track, secret-handshake: 
#    Given a decimal number, convert it to the appropriate sequence of events for a secret handshake.
# Written by Z Knight, 2020.04.07
#
handshake <- function(n) {
    # print(dec_to_bin_seq(n))
    if (n <=0 ) return(c())

    bin_seq <- dec_to_bin_seq(n)
    n_bits = length(bin_seq)
    events <- c()
    for (position in 1:n_bits) {
        # print(position)
        digit = bin_seq[position]
        # print(digit)
        if (digit == 1 & position <= 4 ) {
            # print(code_list[position])
            events <- append(events, code_list[position])
        }
    }

    # reverse if reverse bit set
    if (n_bits == 5) events <- rev(events)

    # print(events)
    return(events)
}

code_list <- c("wink", "double blink", "close your eyes", "jump")

dec_to_bin_seq <- function(n) {
    if (n == 1) return(c(1))
    append(n%%2, dec_to_bin_seq(n%/%2))
}
