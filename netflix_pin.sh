#!/bin/bash

greenColour="\e[0;32m\033[1m"
endColour="\033[0m\e[0m"
redColour="\e[0;31m\033[1m"
blueColour="\e[0;34m\033[1m"
yellowColour="\e[0;33m\033[1m"
purpleColour="\e[0;35m\033[1m"
turquoiseColour="\e[0;36m\033[1m"
grayColour="\e[0;37m\033[1m"

python3 index.py -s $1 -e $2 &
PID=$(echo $!)

function Ctrl_c {
    echo "[!]Saliendo..."
    kill -9 $PID
    exit 1
}

trap 'Ctrl_c' INT 

while true; do
    sound=$(pacmd list-sink-inputs  | grep -w state | grep  "RUNNING" | awk 'NF{print $NF}') 
    if [[ $sound = "RUNNING" ]];then
     
        if pgrep -f index.py >/dev/null; then   
        
            kill -9 $PID &>/dev/null 
           
            echo -e "${turquoiseColour}\nEl pin esta entre el rango de numeros: $(expr $(cat files.txt) - 11) "-" $(expr $(cat files.txt) - 2)${endColour}" 
            echo -e "${greenColour}\nProbablemnte sea el PIN: $(expr $(cat files.txt) - 3) :)${endColour}"
            echo -e "${redColour}\n[!] Si no ve ningun numero es porque\nla tarjeta de sonido esta activa...${endColour}"
            kill -9 $(pgrep -f text.txt) &>/dev/null 
            rm files.txt
            exit 1
        
        else

            echo "[!]Espere..."
            exit 1
        
        fi
    fi
done 2>/dev/null
