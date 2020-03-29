#include <stdbool.h> 
#include <math.h>
// #include <stdio.h>
#include "armstrong_numbers.h"

/* Name: armstrong_numbers.c
 * Purpose: exercism, c track, armstrong numbers
 * Written by Z Knight, 2019.09.11
 *   Modified for smaller memory requirement; ZK, 2019.10.01
 *   Modified so function names use underscores; ZK, 2019.10.07
 *   Modified to use math.pow; ZK, 2019.10.24
 *   Modified to use only one return statement; ZK, 2020.03.29
 */

bool is_armstrong_number(int input_number)
{
  int my_digit;
  int reduced_number = input_number;
  int partial_sum = 0;
  int num_digits = 0;
  
  // count the digits
  // printf("Input number: %d\n", input_number);
  while(reduced_number >= 1) {
    reduced_number /= 10;
    num_digits += 1;
  }
  // printf("num digits: %d\n", num_digits);

  // separate input into digits and raise to power
  reduced_number = input_number;
  while(reduced_number >= 1) {
    my_digit = reduced_number % 10;
    reduced_number /= 10;
    partial_sum += pow(my_digit, num_digits);
  }
  return partial_sum == input_number;
}
