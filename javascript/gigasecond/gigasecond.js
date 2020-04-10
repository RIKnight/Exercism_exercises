/*
 * Name: gigasecond.js
 * Purpose: exercism, javascript track, gigasecond: 
 *    Given a moment, determine the moment that would be after a gigasecond has passed.
 * by Z Knight, 2020.04.09
 */

export const gigasecond = (inputDate) => {
  var input_ms = inputDate.getTime()  // milliseconds
  // console.log(input_ms)
  return new Date(input_ms+10**9*1000)
};
