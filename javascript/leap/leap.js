/*
 * Name: leap.js
 * Purpose: exercism, javascript track, leap
 * by Z Knight, 2019.10.11
 */

export const isLeap = (year) => {
  var result = false;
  if (year %4 == 0 && ( year %100 != 0 || year %400 == 0 )) {
    return true;
  }
  return result;
};

