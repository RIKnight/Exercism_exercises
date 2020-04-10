# Name: fizz-buzz.R
# Purpose: exercism, R track, fizz-buzz: 
#    Print numbers from 1 to n with the following exceptions:
#        When a number is a multiple of 3, then print "Fizz"
#        When a number is a multiple of 5, then print "Buzz"
#        When a number is both a multiple of 3 and a multiple of 5, then print "Fizz Buzz"
#        The output should be a vector of strings, such as, "1" "2" "Fizz" "4" "Buzz" ...
# Written by Z Knight, 2020.04.09
#
fizz_buzz <- function(input) {
    response = c()
    for (number in c(1:input)) {
        if (number %% 3 == 0) {
            if (number %% 5 == 0) {
                response <- append(response, "Fizz Buzz")
            }
            else {
                response <- append(response, "Fizz")
            }
        }
        else if (number %% 5 == 0) {
            response <- append(response, "Buzz")
        }
        else {
            response <- append(response, toString(number))
        }
    }
    return(response)
}
