#!/usr/bin/env bash

curl -sL https://deb.nodesource.com/setup_16.x | bash -
apt-get install -y nodejs
npm i -g npm
pip3 install -r requirements.txt
