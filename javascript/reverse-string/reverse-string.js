/*
 * Name: reverse-string.js
 * Purpose: exercism, javascript track, reverse-string
 * by Z Knight, 2019.10.12
 */

export const reverseString = (inString) => {
  var result = "";
  var counter;
  for (counter = 0; counter < inString.length; counter++) {
    result = inString.charAt(counter).concat(result);
  }
  return result;
};

