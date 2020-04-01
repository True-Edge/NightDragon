#!/bin/bash
clear
if [ -f .env ]
then
  export $(cat .env | sed 's/#.*//g' | xargs)
fi
while :
do
bash -c "exec -a pybot python3 bot.py"
bash stop.sh
git fetch; git pull
done