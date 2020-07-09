#!/bin/bash
clear
while :
do
if [ -f .env ]
then
  export $(cat .env)
fi

git fetch codeberg master; git pull codeberg master
clear
bash -c "exec -a pybot python3 d.py"
bash stop.sh
done