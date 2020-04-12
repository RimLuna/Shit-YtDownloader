#!/bin/bash


if ! [[ "$(python3 -V)" =~  ^(.*)(3.*)$ ]]; then
    echo "Need Python 3"
    echo "Installing dependencies.."
    sudo apt-get install python3 && sudo apt install python3-pip
    pip3 install youtube_dl;
fi

pip3 install youtube_dl
