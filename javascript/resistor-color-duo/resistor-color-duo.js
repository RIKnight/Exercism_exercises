/*
 * Name: resistor-color-duo.js
 * Purpose: exercism, javascript track, resistor-color-duo: translate two colors to numbers
 * Uses: resistor-color.js
 * by Z Knight, 2020.04.04
 */

import { colorCode, COLORS } from './resistor-color'

export const decodedValue = (colorList) => {
  // throw new Error("Remove this statement and implement this function");
  var digit_0 = colorCode(colorList[0])
  var digit_1 = colorCode(colorList[1])
  return digit_0*10+digit_1;
};
