#!/bin/bash
# set -x # uncomment to debug
if [[ $# < 3 ]]; then
    echo 'missing argument, usage is: ploop.sh <prefix> <start> <end>'
    exit 1
fi

printf "\n"
for ((o=$2;o<=$3;o++)); do
    ping -c 1 ${1}.${o} | grep "bytes from" | cut -d" " -f4 | cut -d":" -f1 &
done
wait # w/o this, the script doesn't seem to stop
