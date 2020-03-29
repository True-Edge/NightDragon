#!/bin/bash
clear
if [ -f .env ]
then
  export $(cat .env | sed 's/#.*//g' | xargs)
fi
while :
do
git fetch; git pull
bash -c "exec -a pybot python3 bot.py"
bash stop.sh
done