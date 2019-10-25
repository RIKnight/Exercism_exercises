#!/usr/bin/env bash

# Name: resitor_color_duo.sh
# Purpose: exercism, bash track, resistor color duo: translate two colors to numbers
# Written by Z Knight, 2019.10.24

COLORS=("black" "brown" "red" "orange" "yellow" "green" "blue" "violet" "grey" "white")

main () {
  # echo ${COLORS[@]}
  result=""
  for j in $@; do
    for i in ${!COLORS[@]}; do
      if [[ $j == ${COLORS[$i]} ]]; then
        result="$result"$( printf '%01d' $i )
      fi
    done 
  done

  if [[ $result == "" ]]; then
    echo "invalid color"
  else
    echo "$result"
  fi
}

main "$1 $2"
