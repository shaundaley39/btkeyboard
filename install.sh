#! /bin/bash

sudo rm -R /usr/local/src/btkeyboard
sudo cp -R ../btkeyboard /usr/local/src/btkeyboard
sudo sh -c "echo 'sudo /usr/local/src/btkeyboard/blues.sh' >> /etc/profile"
