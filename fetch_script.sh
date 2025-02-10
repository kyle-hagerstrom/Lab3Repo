#!/bin/bash

URL="$1"

# Fetching the remote bundle via passing a URL
curl -O $URL

# Decompressing the archive using tar
tar -xzf *.tar.gz

# Coverting from tab seperated value (tsv) file format to csv format
tr '\t' ',' < lab3_data.tsv > new_lab3_data.csv
