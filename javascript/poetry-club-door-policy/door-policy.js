/*
 * Name: door-policy.js
 * Purpose: exercism, javascript track, door-policy
 * by Z Knight, 2021.10.19
 */

/**
 * Respond with the correct character, given the line of the
 * poem, if this were said at the front door.
 *
 * @param {string} line
 * @returns {string} the first letter of the line
 */
export function frontDoorResponse(line) {
  return line[0]
}

/**
 * Format the password for the front-door, given the response
 * letters.
 *
 * @param {string} word the letters you responded with before
 * @returns {string} the front door password
 */
export function frontDoorPassword(word) {
  return word[0].toUpperCase()+word.slice(1,word.length).toLowerCase()
}

/**
 * Respond with the correct character, given the line of the
 * poem, if this were said at the back door.
 *
 * @param {string} line
 * @returns {string} The last letter of the line before trailing
 */
export function backDoorResponse(line) {
  var trimmed = line.trim()
  return trimmed[trimmed.length-1]
}

/**
 * Format the password for the back door, given the response
 *
 * @param {string} word the letters you responded with before
 * @returns {string} the back door password
 */
export function backDoorPassword(word) {
  return word[0].toUpperCase()+word.slice(1,word.length).toLowerCase()+", please"
}
