#!/bin/bash

width=0;
height=0;

if [ $height != `tput lines` ]
then
 echo "456"
fi
	

while(true)
do
if [ $height != `tput lines` -o $width != `tput cols` ]
then
	height=`tput lines`
	width=`tput cols`
	echo "$width,$height"
fi
done

