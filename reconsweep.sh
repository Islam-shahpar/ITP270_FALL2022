#!/bin/bash

echo "Enter the first name and press enter: "
read first_name
echo "Enter the last name and press enter: "
read last_name

echo $first_name $last_name

echo "searching for" $first_name $last_name

firefox "https://www.411.com/name/$first_name-$last_name?"


