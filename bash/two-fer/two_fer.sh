#!/usr/bin/env bash

# Name: two_fer.sh
# Purpose: exercism, bash track, two-fer
# Written by Z Knight, 2019.09.10
#   refactored for simplicity; ZK, 2019.09.15

main () {
  if [ -z "$1" ]
    then
      my_input='you'
    else my_input="$1"
  fi
  start_string='One for '
  end_string=', one for me.'

  result="$start_string$my_input$end_string"
  echo $result
}

main "$1"
