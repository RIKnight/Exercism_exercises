/* Name:
 *   hamming.cpp
 * Purpose:
 *   Exercism, cpp track, Hamming distance
 * Modification History:
 *   Written byZ Knight, 2019.10.04
 */
#include "hamming.h"
#include <iostream>

using namespace std;

namespace hamming {

int compute(string string1, string string2) {
  int distance = 0;
  
  if (string1.length() != string2.length()) {
    cout << "lengths not equal!\n";
    throw domain_error("Lengths not equal!");
  }
  for (unsigned i=0; i<string1.length(); ++i) {
    //cout << string1.at(i) << string2.at(i) << "\n";
    if (string1.at(i) != string2.at(i)) {
      distance++;
    }
  }
  return distance;

}  // int compute

}  // namespace hamming
