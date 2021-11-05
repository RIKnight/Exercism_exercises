/*
 * Name: vehicle-purhcase.js
 * Purpose: exercism, javascript track, vehicle-purhcase
 * by Z Knight, 2021.11.05
 */

/**
 * Determines whether or not you need a licence to operate a certain kind of vehicle.
 *
 * @param {string} kind
 * @returns {boolean} whether a license is required
 */
export function needsLicense(kind) {
  return (kind === "car" || kind === "truck")
}

/**
 * Helps choosing between two options by recommending the one that
 * comes first in dictionary order.
 *
 * @param {string} option1
 * @param {string} option2
 * @returns {string} a sentence of advice which option to choose
 */
export function chooseVehicle(option1, option2) {
  const rest = ' is clearly the better choice.'
  if (option1 < option2) {return option1+rest}
  else {return option2+rest}
}

/**
 * Calculates an estimate for the price of a used vehicle in the dealership
 * based on the original price and the age of the vehicle.
 *
 * @param {number} originalPrice
 * @param {number} age
 * @returns expected resell price in the dealership
 */
export function calculateResellPrice(originalPrice, age) {
  if (age<3){return originalPrice*0.8}
  else if (age<=10){return originalPrice*0.7}
  else {return originalPrice*0.5}
}
