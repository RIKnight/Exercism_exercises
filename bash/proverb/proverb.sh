#!/usr/bin/env bash

# Name: proverb.sh
# Purpose: exercism, bash track, proverb:
#   For want of a horseshoe nail, a kingdom was lost, or so the saying goes.
#   Given a list of inputs, generate the relevant proverb. For example, given the list 
#   `["nail", "shoe", "horse", "rider", "message", "battle", "kingdom"]`, 
#   you will output the full text of this proverbial rhyme
# Written by Z Knight, 2020.06.14

forwant() {
    # needs two inputs
    echo "For want of a "$1" the "$2" was lost."
}

main () {
    args=("$@")
    for (( word_counter=0; word_counter<$#-1; word_counter++ )); do
        forwant "${args[$word_counter]}" "${args[$word_counter+1]}"
    done
    if [[ $# > 0 ]]; then
        echo "And all for the want of a "$1"."
    fi
}

main "$@"
