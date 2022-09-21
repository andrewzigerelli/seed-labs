#! /usr/bin/awk -f 

#use BEGIN sepecial character to set FS built-in variable
BEGIN { FS="\t" }

#first_col=NF
{_start=3; for(i=_start; i<=NF; i++) print $i }

#{ print $3 }

#END { print NF}
