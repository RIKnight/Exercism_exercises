/*
 * Name: bird-watcher.js
 * Purpose: exercism, javascript track, bird-watcher
 * by Z Knight, 2021.11.06
 */

/**
 * Calculates the total bird count.
 *
 * @param {number[]} birdsPerDay
 * @returns {number} total bird count
 */
export function totalBirdCount(birdsPerDay) {
  let sum = 0;
  for (let i = 0; i < birdsPerDay.length; i++) {
    sum += birdsPerDay[i];
  }
  return sum
}

/**
 * Calculates the total number of birds seen in a specific week.
 *
 * @param {number[]} birdsPerDay
 * @param {number} week
 * @returns {number} birds counted in the given week
 */
export function birdsInWeek(birdsPerDay, week) {
  let dayStart = (week-1)*7;
  let sum = 0;
  for (let i = dayStart; i < dayStart+7; i++) {
    sum += birdsPerDay[i];
  }
  return sum
}

/**
 * Fixes the counting mistake by increasing the bird count
 * by one for every second day.
 *
 * @param {number[]} birdsPerDay
 * @returns {number[]} corrected bird count data
 */
export function fixBirdCountLog(birdsPerDay) {
  let correctedBirdsPerDay = birdsPerDay
  for (let i = 0; i < birdsPerDay.length; i++) {
    if (i % 2 === 0) {
      correctedBirdsPerDay[i]++
    }
  }
  return correctedBirdsPerDay
}
