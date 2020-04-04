/*
 * Name: collatz-conjecture.js
 * Purpose: exercism, javascript track, collatz-conjecture
 * by Z Knight, 2020.04.04
 */

export const steps = (toCheck) => {
  if (toCheck <= 0) {
    throw new Error('Only positive numbers are allowed');
  }
  if (toCheck == 1) {
    return 0;
  }
  else if (toCheck%2 == 0) {
    return steps(toCheck/2) +1;
  }
  else {
    return steps(3*toCheck+1) +1;
  }
};

