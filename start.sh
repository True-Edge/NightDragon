#!/bin/bash
clear
if [ -f .env ]
then
  export $(cat .env)
fi

while :
do
git fetch codeberg master; git pull codeberg master
clear
bash -c "exec -a pybot python3 d.py"
bash stop.sh
done