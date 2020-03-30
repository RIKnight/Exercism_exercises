/*
 * Name: leap.js
 * Purpose: exercism, javascript track, leap
 * by Z Knight, 2019.10.11
 *   Simplified to single line; ZK, 2020.03.29
 */

export const isLeap = (year) => {
  return (year %4 == 0 && ( year %100 != 0 || year %400 == 0 ));
};

