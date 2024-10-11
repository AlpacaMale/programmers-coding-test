#!/usr/bin/zsh

if [ $# -eq 1 ]; then
    title=$(echo "$1" | sed 's/ /_/g')
    mkdir ${title}
    touch ${title}/${title}.py
    echo "# [$1][1]" > ${title}/${title}.md
    echo "" >> ${title}/${title}.md
    echo "## 문제 설명" >> ${title}/${title}.md
    echo "" >> ${title}/${title}.md
    echo "" >> ${title}/${title}.md
    echo "" >> ${title}/${title}.md
    echo "## 제한사항" >> ${title}/${title}.md
    echo "" >> ${title}/${title}.md
    echo "" >> ${title}/${title}.md
    echo "" >> ${title}/${title}.md
    echo "## 입출력 예" >> ${title}/${title}.md
    echo "" >> ${title}/${title}.md
    echo "" >> ${title}/${title}.md
    echo "" >> ${title}/${title}.md
    echo "## 풀이" >> ${title}/${title}.md
    echo "" >> ${title}/${title}.md
    echo "" >> ${title}/${title}.md
    echo "" >> ${title}/${title}.md
    echo "[1]: " >> ${title}/${title}.md
else
    echo "Usage: $0 foldername"
    exit 1
fi