#!/bin/bash
clear
if [ -f .env ]
then
  export $(cat .env | sed 's/#.*//g' | xargs)
fi
while :
do
clear
git fetch; git pull codeberg master
bash -c "exec -a pybot python3 bot.py"
bash stop.sh
done