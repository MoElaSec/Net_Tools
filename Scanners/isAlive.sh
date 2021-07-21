#!/usr/bin/env bash

for protocol in 'http://' 'https://'; do
	while read line;
	do
		code=$(timeout 5 curl -L -s --write-out "%{http_code}" --insecure $protocol$line -o /dev/null)
		if [ $code = "000" ]; then
			echo "$protocol$line: not responding."
		else
			echo "$protocol$line: HTTP $code"	
			echo "$protocol$line: $code" >> alive.txt 
		fi
	done < domains.txt
done
