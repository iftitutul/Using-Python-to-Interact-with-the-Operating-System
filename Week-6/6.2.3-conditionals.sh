#!/bin/bash

if grep "127.0.0.1" /etc/hosts;then
   echo "everything ok"
else
   echo "ERROR! 127.0.0.1 is not in /etc/hosts"
fi


### one line in conditional
if test -n "$PATH"; then echo "Your path is not empty"; fi

## or, use [] instead of test
if [ -n "$PATH" ]; then echo "Your path is not empty"; fi