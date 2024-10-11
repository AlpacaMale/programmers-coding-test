#!/usr/bin/zsh

date_dir=$(date +%Y-%m-%d)
mkdir -p "$date_dir"

if [ $# -eq 1 ]; then
    title=$(echo "$1" | sed 's/ /_/g')

    if [ -d "${date_dir}/${title}" ]; then
        echo "Error: Folder '${title}' already exists in ${date_dir}."
        exit 1
    fi

    mkdir "${date_dir}/${title}"
    touch "${date_dir}/${title}/${title}.py"

    echo "# $1" > "${date_dir}/${title}/README.md"
    echo "[코딩테스트 연습 - $1][1] 로 이동" >> "${date_dir}/${title}/README.md"
    echo "" >> "${date_dir}/${title}/README.md"

    echo "## 문제 설명" >> "${date_dir}/${title}/README.md"
    echo "" >> "${date_dir}/${title}/README.md"

    echo "## 제한사항" >> "${date_dir}/${title}/README.md"
    echo "" >> "${date_dir}/${title}/README.md"

    echo "## 입출력 예" >> "${date_dir}/${title}/README.md"
    echo "" >> "${date_dir}/${title}/README.md"

    echo "## 입출력 예 설명" >> "${date_dir}/${title}/README.md"
    echo "" >> "${date_dir}/${title}/README.md"

    echo "## 풀이" >> "${date_dir}/${title}/README.md"
    echo '```python' >> "${date_dir}/${title}/README.md"
    echo "" >> "${date_dir}/${title}/README.md"
    echo '```' >> "${date_dir}/${title}/README.md"

    echo "[1]: " >> "${date_dir}/${title}/README.md"

    echo "Folder and structure created at ${date_dir}/${title}."
else
    echo "Usage: $0 foldername"
    exit 1
fi
