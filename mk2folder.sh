#!/usr/bin/zsh

if [ $# -eq 1 ]; then
    mkdir $1
    touch $1/$1.py
    echo "# [][1]" > $1/$1.md
    echo "입니다." >> $1/$1.md
    echo "" >> $1/$1.md
    echo "## 풀이" >> $1/$1.md
    echo "" >> $1/$1.md
    echo "[1]: " >> $1/$1.md
else
    echo "Usage: $0 foldername"
    exit 1
fi