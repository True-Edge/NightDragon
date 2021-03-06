#!/bin/bash
clear
if [ -f .env ]
then
  export $(cat .env | sed 's/#.*//g' | xargs)
fi

while :
do
  git fetch; git pull
  clear
  bash -c "exec -a pybot python3 d.py"
  bash stop.sh
done