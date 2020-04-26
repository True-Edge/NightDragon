#!/bin/bash
clear
if [ -f .env ]
then
  export $(cat .env | sed 's/#.*//g' | xargs)
fi
while :
do
git fetch codeberg master; git pull codeberg master
clear
bash -c "exec -a pybot python3 d.py" & bash -c "exec -a hata-bot python3 h.py"
bash stop.sh
done