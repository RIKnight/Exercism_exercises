/*
 * Name: freelancer-rates.js
 * Purpose: exercism, javascript track, freelancer-rates
 * by Z Knight, 2021.10.14
 */

const DAILY_RATE_FACTOR = 8;
const BILLABLE_DAYS_PER_MONTH = 22;

/**
 * The day rate, given a rate per hour
 *
 * @param {number} ratePerHour
 * @returns {number} the rate per day
 */
export function dayRate(ratePerHour) {
  return ratePerHour * DAILY_RATE_FACTOR;
}

/**
 * Calculates the rate per month
 *
 * @param {number} ratePerHour
 * @param {number} discount for example 20% written as 0.2
 * @returns {number} the rounded up monthly rate
 */
export function monthRate(ratePerHour, discount) {
  return Math.ceil(dayRate(ratePerHour) * BILLABLE_DAYS_PER_MONTH * (1-discount));
}

/**
 * Calculates the number of days in a budget, rounded down
 *
 * @param {number} budget the total budget
 * @param {number} ratePerHour the rate per hour
 * @param {number} discount to apply, example 20% written as 0.2
 * @returns {number} the number of days
 */
export function daysInBudget(budget, ratePerHour, discount) {
  return Math.floor(budget/dayRate(ratePerHour)/(1-discount));
}

