/*
 * Name: mixed-juices.js
 * Purpose: exercism, javascript track, mixed-juices
 * by Z Knight, 2021.11.07
 */

/**
 * Determines how long it takes to prepare a certain juice.
 *
 * @param {string} name
 * @returns {number} time in minutes
 */
export function timeToMixJuice(name) {
  switch (name) {
    case 'Pure Strawberry Joy':
      return 0.5;
    case 'Energizer':
    case 'Green Garden':
      return 1.5;
    case 'Tropical Island':
      return 3;
    case 'All or Nothing':
      return 5;
    default:
      return 2.5;
  }
}

/**
 * Calculates the number of limes that need to be cut
 * to reach a certain supply.
 *
 * @param {number} wedgesNeeded
 * @param {string[]} limes
 * @returns {number} number of limes cut
 */
export function limesToCut(wedgesNeeded, limes) {
  let numLimes = 0
  let limeSize = ""
  while (wedgesNeeded > 0 && limes.length > 0) {
    limeSize = limes.shift()
    numLimes++
    switch (limeSize) {
      case 'small':
        wedgesNeeded -= 6
        break;
      case 'medium':
        wedgesNeeded -= 8
        break;
      case 'large':
        wedgesNeeded -= 10
        break;
    }
  }
  return numLimes;
}

/**
 * Determines which juices still need to be prepared after the end of the shift.
 *
 * @param {number} timeLeft
 * @param {string[]} orders
 * @returns {string[]} remaining orders after the time is up
 */
export function remainingOrders(timeLeft, orders) {
  let nextOrder = ""
  while (timeLeft > 0 && orders.length > 0) {
    nextOrder = orders.shift()
    timeLeft -= timeToMixJuice(nextOrder)
  }
  return orders
}
