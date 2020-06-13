#!/usr/bin/env bash

# Name: matching_brackets.sh
# Purpose: exercism, bash track, matching_brackets:
#    Given a string containing brackets [], braces {}, parentheses (), or any combination thereof, 
#    verify that any and all pairs are matched and nested correctly.
# Written by Z Knight, 2020.06.12

# these must be the same length
OPENS=("(" "[" "{")
CLOSES=(")" "]" "}")

main () {
    input=$1
    char_stack=""

    for (( i=0; i<${#input}; i++ )); do
        char="${input:$i:1}"
        for j in ${!OPENS[@]}; do
            # Check for opening bracket
            if [[ $char == ${OPENS[$j]} ]]; then
                char_stack+=$char
                break
            else
                # check for closing bracket
                if [[ $char == ${CLOSES[$j]} ]]; then
                    previous="${char_stack:${#char_stack}-1:1}"
                    # check for matching pair
                    if [[ $previous == ${OPENS[$j]} ]]; then
                        char_stack="${char_stack:0:${#char_stack}-1}"
                        break
                    else
                        # closing bracket without opening
                        char_stack="bad"
                        break 2
                    fi
                fi
            fi
        done
    done
    
    result="true"
    if [[ ${#char_stack} != 0 ]]; then
        result="false"
    fi
    echo "$result"
    
}

main "$@"

