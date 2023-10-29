#!/bin/bash
friend1=$1
echo "what is your name ?"
friend="shubha"
read name
echo "hey how are you $name"
sleep 3
echo "AWESOME "
sleep 3
echo "I gotta go good to see you again Bye $name"
echo "you are the $friend 's friend"
echo "he is another $friend1"
sleep 4
user=$(whoami)
date=$(date)
whereami=$(pwd)
echo "you are $user on location $whereami on date-$(date)"
echo $((765+5656))