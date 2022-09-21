#!/bin/bash
sed -i.bak "s/content_size = .*/content_size = $1/g" exploit.py
python3 exploit.py 
../server-code/stack-L1 < badfile
