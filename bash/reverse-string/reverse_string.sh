#!/usr/bin/env bash

# Name: reverse_string.sh
# Purpose: exercism, bash track, reverse_string
# Written by Z Knight, 2019.10.05
#  Modified to "avoid globbing"; ZK 2019.10.05

main () {
  result=""
  for (( i=0; i<${#1}; i++ )); do
    # echo "${1:$i:1}"
    result="${1:$i:1}$result"
  done

  echo "$result"
}

main "$1"
