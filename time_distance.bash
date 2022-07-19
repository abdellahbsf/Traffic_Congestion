#!/bin/bash
for i in {1..168} # (24 hours during one week)
do
    start=$(date +%s)
    python time_distance.py
	end=$(date +%s)
	runtime=$(( $end - $start ))
	sleep_sec=$(( 3600 - $runtime ))
    sleep $sleep_sec

done
