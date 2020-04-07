/*
 * Name: resistor-color.js
 * Purpose: exercism, javascript track, resistor-color
 * by Z Knight, 2019.10.07
 *   Modified to use .indexOf method; ZK, 2020.04.07
 */

export const colorCode = (colorToFind) => {
  return COLORS.indexOf(colorToFind)
};

export const COLORS = ["black","brown","red","orange","yellow","green","blue","violet","grey","white"];

