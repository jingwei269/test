#!/bin/bash 

server_lst=`cat server_list`

for hostname in $server_lst; do 
    echo $hostname
    ssh yhuangjw@$hostname id
done

