#!/usr/bin/env bash

# Name: grep.sh
# Purpose: exercism, bash track, grep:
#   Search a file for lines matching a regular expression pattern. 
#   Return the line number and contents of each matching line.
#   The grep command takes three arguments:
#       The pattern used to match lines in a file.
#       Zero or more flags to customize the matching behavior.
#       One or more files in which to search for matching lines.
#   This script implements the grep function, which should read the contents 
#       of the specified files, find the lines that match the specified 
#       pattern and then output those lines as a single string. 
#   Note that the lines will be output in the order in which they were found, 
#       with the first matching line in the first file being output first.
#
# Written by Z Knight, 2021.10.21
# Fixed logic error; ZK, 2021.10.26
#

main () {
    # set default arguments
    print_line_numbers=0
    print_only_file_names=0
    #match_case_insensitive=0
    invert_program=0
    only_match_entire_lines=0

    # parse command line switches
    while getopts "nlivx" option; do
    case ${option} in
        n ) # Print the line numbers of each matching line.
        print_line_numbers=1
        ;;
        l ) # Print only the names of files that contain at least one matching line.
        print_only_file_names=1
        ;;
        i ) # Match line using a case-insensitive comparison.
        #match_case_insensitive=1
        shopt -s nocasematch
        ;;
        v ) # Invert the program -- collect all lines that fail to match the pattern.
        invert_program=1
        ;;
        x ) # Only match entire lines, instead of lines that contain a match.
        only_match_entire_lines=1
        ;;
        \? )  # invalid option 
        echo "Valid options: [-n] [-l] [-i] [-v] [-x]"
        exit
        ;;
        esac
    done
    # drop the leading flags from argument list
    shift $((OPTIND - 1))
    
    # get the search string
    if [[ $only_match_entire_lines == 1 ]]; then
        to_find="^"$1"$"
    else
        to_find=$1
    fi
    
    # loop through the file
    line_counter=0
    while IFS= read -r line; do
        let line_counter=$line_counter+1
        # printf '%s\n' "$line"
        if (   [[ $line =~ $to_find ]] && [[ $invert_program == 0 ]] ) || 
           ( ! [[ $line =~ $to_find ]] && [[ $invert_program == 1 ]] ); then
            if [[ $print_only_file_names == 1 ]]; then
                echo $2
            else  # print the line, not the file name
                if [[ $print_line_numbers == 1 ]]; then
                    printf '%s:%s\n' "$line_counter" "$line"
                else
                    printf '%s\n' "$line"
                fi
            fi
        fi
    done < $2
}

main "$@"



