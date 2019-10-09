#!/usr/bin/env bash

# Name: leap.sh
# Purpose: exercism, bash track, leap
# Written by Z Knight, 2019.10.08

main () {
  if [[ -z $1  ||  $# -ne 1 || $1 =~ ^[0-9]+\.[0-9]*$ || $1 =~ [a-zA-Z] ]]; then
  # if ( no arg1 || not exactly 1 arg || arg1 has a decimal || arg1 has any letters )
    echo 'Usage: leap.sh <year>'
    exit 1
  fi

  result="false"
  if [[ $1%4 -eq 0 && ( $1%100 -ne 0 || $1%400 -eq 0 ) ]]; then
      result="true"
  fi

  echo "$result"
}

main "$@"
