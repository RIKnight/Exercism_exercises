#include <stdbool.h> 
// #include <stdio.h>
#include "armstrong_numbers.h"

/* Name: armstrong_numbers.c
 * Purpose: exercism, c track, armstrong numbers
 * Written by Z Knight, 2019.09.11
 *   Modified by ZK for smaller memory requirement, 2019.10.01
 */

int intPow(int base, int exponent)
// works recursively
// exponent must be >= 1
{
  if(exponent == 1) {
    return base;
  }
  return base*intPow(base, exponent-1);
}

bool isArmstrongNumber(int input_number)
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
    partial_sum += intPow(my_digit, num_digits);
  }
  if(partial_sum == input_number) {
    return true;
  }
  return false;
}
