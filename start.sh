#!/bin/bash
clear
if [ -f .env ]
then
  export $(cat .env | sed 's/#.*//g' | xargs)
fi
while :
do
git fetch codeberg; git pull codeberg master
clear
bash -c "exec -a pybot python3 bot.py"
bash stop.sh
done