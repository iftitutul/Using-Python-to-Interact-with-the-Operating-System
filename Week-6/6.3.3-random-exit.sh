#!/bin/bash

n=1
command=$1
while ! $command && [ $n -le 5 ]; do
   sleep $n
   ((n+=1))
   echo "Retry #$n"
done;

### ./6.3.3-random-exit.sh ./6.3.2-random-exit.py 