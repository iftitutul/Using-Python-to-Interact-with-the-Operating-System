#!/usr/bin/env python3.6

log = "JULY 31 07:51:48 mycomputer bad_process[12345]: ERROR Performing package upgrade"

index = log.index("[")

print(log[index+1:index+6])
