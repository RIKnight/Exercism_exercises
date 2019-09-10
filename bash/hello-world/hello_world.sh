#!/usr/bin/env bash
# exercism, bash track, exercise 1
# by Z Knight, 2019.09.07

function hello {
  local  __resultvar=$1
  local  myresult='Hello, World!'
  eval $__resultvar="'$myresult'"
}

main () {
  hello result
  echo $result
  exit
}

main
