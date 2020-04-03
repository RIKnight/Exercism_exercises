/*
 * Name: triangle.js
 * Purpose: exercism, javascript track, triangle
 * by Z Knight, 2020.04.01
 * Updated to conform with new version of triangle.spec.js; ZK, 2020.04.03
 */

export class Triangle {
  constructor(side_A, side_B, side_C) {
    this.side_A = side_A;
    this.side_B = side_B;
    this.side_C = side_C;

    // count the number of pairs of equal sides
    this.num_equal_pairs = 0;
    this._side_check(side_A, side_B)
    this._side_check(side_B, side_C)
    this._side_check(side_C, side_A)
  }

  _side_check(side_A, side_B) {
    if ( side_A == side_B ) {
      this.num_equal_pairs += 1;
    }
  }

  kind() {
    // check for illegal values
    if (this.side_A <= 0 || this.side_B <= 0 || this.side_C <= 0) {
      throw new Error("Side is not > 0");
    }
    var sum_1 = this.side_A + this.side_B;
    var sum_2 = this.side_B + this.side_C;
    var sum_3 = this.side_C + this.side_A;
    if ( sum_1 < this.side_C || sum_2 < this.side_A || sum_3 < this.side_B ) {
      throw new Error("Violates triangle inequality!");
    }

    if (this.num_equal_pairs >= 2) {
      return 'equilateral';
    }
    else if (this.num_equal_pairs == 1) {
      return 'isosceles';
    }
    else {
      return 'scalene';
    }
  }

  isEquilateral() {
    try {
      return ( this.kind() == 'equilateral')
    }
    catch {
      return false
    }
  }

  isIsosceles() {
    try {
      return ( this.kind() == 'isosceles' || this.kind() == 'equilateral')
    }
    catch {
      return false
    }
  }

  isScalene() {
    try {
      return ( this.kind() == 'scalene')
    }
    catch {
      return false
    }
  }
}
