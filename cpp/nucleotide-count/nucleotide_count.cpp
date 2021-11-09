#include "nucleotide_count.h"
#include <string>
#include <map>

namespace nucleotide_count {

counter::counter (std::string in_string)
{
    dna_sequence = in_string;
}

int counter::count() const
{
    return 0;
}

std::map<char, int> counter::nucleotide_counts() const
{
    const std::map<char, int> expected{ {'A', 0}, {'T', 0}, {'C', 0}, {'G', 0} };
    return expected;
}


}  // namespace nucleotide_count
