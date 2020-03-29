#!/bin/bash
clear
if [ -f .env ]
then
  export $(cat .env | sed 's/#.*//g' | xargs)
fi
while :
do
clear
git fetch; git pull
bash -c "exec -a pybot python3 bot.py" $ bash -c "exec -a jsbot node main.js"
bash stop.shz
done