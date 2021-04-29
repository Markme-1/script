#!/usr/bin/bash
# shutdown script
#doBASH

echo -e "\e[92mcreated by doBASH\e[0m"
echo ""
echo ""
if [[ $UID -eq 0 ]] 
then
sleep 1
echo -e "\e[31m[1]absolute shutdown\e[0m"
echo -e "\e[31m[2]relative shutdown\e[0m"
echo ""
echo -n "## "
read opt
   if [[ $opt -eq 1 ]]
	then 
             echo -n  "set a time to shutdown[hh:mm]: "
             read tim1
             shutdown $tim1 && echo -e "if you want to cancel schedule shutdown use command \e[31m shutdown -c\e[0m"
        elif [[ $opt -eq 2 ]]
          then 
             echo -n "set a time to shutdown[min]: "
             read tim2
             shutdown +$tim2 && echo -e "if you want to cancel schedule shutdown use command \e[31mshutdown -c\e[0m"
             else 
                echo "the format is incorrect"
    fi

else
  echo " run the script as root"
fi
