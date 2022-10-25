#!/bin/bash
echo "Enter the Subnet:"
read Subnet

if [ "$Subnet" == "" ]
then
	echo "Enter the Subnet:"
	echo "Syntax Example = ./ping_sweep.sh 10.1.161"
else
	for IP in $(seq 1 254); do
		ping -c 1 $Subnet.$IP | grep "64 bytes" | cut -d " " -f 4 | tr -d ":" >> discoveredIPs.txt &
done
fi

cat discoveredIPs.txt | sort > discoveredIPs.txt

nmap -T4 -A -sV -iL discoveredIPs.txt -oN PortScanIPs.txt --append-output

exit
