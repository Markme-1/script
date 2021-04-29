#!/usr/bin/bash
#wios is a wifi dos automated tool

if [[ $UID -eq 0 ]]; then

                                                
                       
	echo "wios is a wifi dos automated tool"
	sleep 2
	iwconfig
	sleep 2
	echo -n "please enter wifi interface name: "
	read wifi
	airmon-ng start $wifi
	airodump-ng $wifi
	 
else echo "run the script as root"
 exit
fi
