#! /bin/bash
BD_ADDRESS=$(sudo hciconfig hcio | awk '/BD/ {print $3}')
REVISION=$(cat /proc/cpuinfo | awk '/Revision/ {print $3}')

if [ "$REVISION" == "a02082" ] || [ "$REVISION" == "a22082" ] ; then
 MODEL="three"
fi
if [ "$REVISION" == "900092" ] || [ "$REVISION" == "900093" ] ; then
 MODEL="zero"
fi

sed -i "/MY_ADDRESS/c\    MY_ADDRESS=\"$BD_ADDRESS\"" server/btk_server.py
