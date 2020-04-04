/*
 * Name: resistor-color.js
 * Purpose: exercism, javascript track, resistor-color
 * by Z Knight, 2019.10.07
 */

export const colorCode = (colorToFind) => {
  var found_index = -1;
  COLORS.forEach(function (item, index) {
    if (item == colorToFind) {
      console.log(item);
      found_index = index;
    }
  });
  return found_index;
};

export const COLORS = ["black","brown","red","orange","yellow","green","blue","violet","grey","white"];

