#!/usr/bin/env bash
# exercism, bash track, two-fer
# by Z Knight, 2019.09.10

function two_fer {
  local  __inputvar="$1"
  local  __resultvar=$2
  local  start='One for '
  local  end=', one for me.'
  local  myresult="$start$__inputvar$end"
  eval $__resultvar="'$myresult'"
}

main () {
  two_fer "$1" result
  echo $result
  exit
}

if [ $# -eq 0 ]
  then
    my_input='you'
  else my_input="$1"
fi
main "$my_input"
