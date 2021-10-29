#!/bin/bash
DEL='./del.list'
len=$(cat ${DEL} | wc -l)
for ((i=1;i<=${len};i++))
do
    del_path=$(head -n ${i} ${DEL} | tail -n 1)
    rm -rf $del_path
done
