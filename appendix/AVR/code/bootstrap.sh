#!/usr/bin/env bash
if [ ! -f /usr/bin/ansible ]; then
    sudo apt-add-repository ppa:ansible/ansible
    sudo apt-get update
    sudo apt-get install ansible
fi


