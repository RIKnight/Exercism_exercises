#if !defined(NUCLEOTIDE_COUNT_H)
#define NUCLEOTIDE_COUNT_H

#include <string>
#include <map>

namespace nucleotide_count {

class counter
{
private:
    
    std::string dna_sequence;
    int num_nucleotides;

    bool _is_valid(char) const;

public:

    // constructor
    counter (std::string);

    int count(char) const;

    std::map<char, int> nucleotide_counts() const;

};

}  // namespace nucleotide_count

#endif // NUCLEOTIDE_COUNT_H