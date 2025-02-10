#!/bin/bash

LOCALFILE="$1"
NEWFILE="$2"

# tr remove spaces
cat "$LOCALFILE" | tr -s '\n' > "$NEWFILE"

