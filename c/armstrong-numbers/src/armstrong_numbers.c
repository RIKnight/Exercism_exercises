#include <stdbool.h> 
#include "armstrong_numbers.h"

/* Name: armstrong_numbers.c
 * Purpose: exercism, c track, armstrong numbers
 * Written by Z Knight, 2019.09.11
 */

#define MAXDIGITS 10

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
  int digits[MAXDIGITS];
  int my_digit;
  int reduced_number = input_number;
  int partial_sum = 0;
  int num_digits = 1;
  // separate input into digits
  for(int digit_num = 0; digit_num < MAXDIGITS; digit_num++) {
    my_digit = reduced_number % 10;
    reduced_number /= 10;
    digits[digit_num] = my_digit;
    if(my_digit != 0) {
      num_digits = digit_num+1;
    }
  }
  
  if(num_digits == 1) {
    return true;
  }

  for(int digit_num=0; digit_num < num_digits; digit_num++)  {
    partial_sum += intPow(digits[digit_num], num_digits);
  }
  if(partial_sum == input_number) {
    return true;
  }
  return false;
}
