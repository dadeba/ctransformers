#!/bin/bash

rm -rf build

./scripts/build.sh
mkdir ctransformers/lib/local/

cp build/lib/libctransformers.so ctransformers/lib/local/


