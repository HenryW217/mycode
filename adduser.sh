#!/bin/bash

# Take input as the username
    echo "Please enter username: "
    sleep 1

# define the username
    read username
# add user
    sudo adduser $username

    echo "Please enter groupname: "
    sleep 1
# define group
    read groupname
# add to group
    sudo usermod -aG $groupname $username



