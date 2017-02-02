#!/bin/env bash

for i in *.res; do
    file $i | grep text > /dev/null
    #echo $?
    if [[ "$?" == "0" ]]; then
        echo "======================= $i ===================="
        cat $i
    fi
done

