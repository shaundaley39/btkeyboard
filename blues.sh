#! /bin/bash
BD_ADDRESS=$(sudo hciconfig hcio | awk '/BD/ {print $3}')
REVISION=$(cat /proc/cpuinfo | awk '/Revision/ {print $3}')

if [ "$REVISION" == "a02082" ] || [ "$REVISION" == "a22082" ] ; then
 MODEL="three"
fi
if [ "$REVISION" == "900092" ] || [ "$REVISION" == "900093" ] ; then
 MODEL="zero"
fi

sudo /etc/init.d/bluetooth stop
sudo /usr/sbin/bluetoothd -p time &
sudo hciconfig hcio up
# here: set bluetooth address hard
sudo python server/btk_server.py > results.txt 2>errors.log &

# next, we need an agent and pairing
./agent.sh
# then we run some client:
sudo python keyboard/kb_client.py
# we will want our client to check whethe it's in a zero or a three, for pin purposes
