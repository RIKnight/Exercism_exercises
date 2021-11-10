/* Name:
 *   nucleotide_count.cpp
 * Purpose:
 *   Exercism, cpp track, nucleotide_count
 * Modification History:
 *   Wirtten by Z Knight, 2021.11.10
 */
#include "nucleotide_count.h"
#include <string>
#include <map>
#include <stdexcept>      // std::invalid_argument

namespace nucleotide_count {

counter::counter (std::string in_string)
{
    dna_sequence = in_string;
    num_nucleotides = dna_sequence.length();
    for (int i = 0; i < num_nucleotides; i++) {
        if (!_is_valid(dna_sequence[i])) {
            throw std::invalid_argument("All nucleotides must be A, T, C, or G.");
        }
    }
}

bool counter::_is_valid(char to_check) const
{
    if (to_check != 'A' && to_check != 'T' && to_check != 'C' && to_check != 'G') {
        return false;
    }
    return true;
}

int counter::count(char to_count) const
{
    if (!_is_valid(to_count)) {
        throw std::invalid_argument("Nucleotide to count must be A, T, C, or G.");
    }
    int num_found = 0;
    for (int i = 0; i < num_nucleotides; i++) {
        if (dna_sequence[i] == to_count) {
            num_found++;
        }
    }
    return num_found;
}

std::map<char, int> counter::nucleotide_counts() const
{
    int num_A = count('A');
    int num_T = count('T');
    int num_C = count('C');
    int num_G = count('G');
    return std::map<char, int> { {'A', num_A}, {'T', num_T}, {'C', num_C}, {'G', num_G} };
}


}  // namespace nucleotide_count
