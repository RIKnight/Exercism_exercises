/*
 * Name: clock.js
 * Purpose: exercism, javascript track, clock
 * by Z Knight, 2021.10.13
 * Modified to use toString().padStart() instead of numeral; ZK, 2021.10.13
 */

// var numeral = require('numeral');

export class Clock {
  constructor(newHours, newMinutes=0) {
    // set starting point
    // note:  % in javascript is a remainder operator, not a modulo operator!
    this.minutes = 0;
    this.hours = (newHours % 24 + 24) % 24;
    // add new minutes
    this.plus(newMinutes);
  }

  toString() {
    //return numeral(this.hours).format('00')+":"+numeral(this.minutes).format('00');
    return this.hours.toString().padStart(2, '0')+":"+this.minutes.toString().padStart(2, '0');
  }

  plus(newMinutes) {
    // input:  the number of minutes to add
    // modify inputs
    var remainingMinutes = ((this.minutes + newMinutes) % 60 + 60) % 60;
    var extraHours = (this.minutes + newMinutes - remainingMinutes) / 60;
    // save results
    this.hours = ((this.hours + extraHours) % 24 + 24) % 24;
    this.minutes = remainingMinutes;

    return this;
  }

  minus(newMinutes) {
    // input:  the number of minutes to subtract
    return this.plus(-1*newMinutes);
  }

  equals(newClock) {
    // input:  a clock to compare to
    return this.minutes == newClock.minutes && this.hours == newClock.hours;
  }
}
