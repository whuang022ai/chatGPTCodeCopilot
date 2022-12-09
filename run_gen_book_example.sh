#!/bin/bash

# 簡介人工智慧
array=('人工智慧' '機器學習' '深度學習')

for i in "${array[@]}" ; do
    python chatGPTCodeCopilot.py -w "$i" -o "$i" -k
done
# 概念比較
python chatGPTCodeCopilot.py -c "人工智慧,機器學習,深度學習" -o "概念比較" -k
# 簡介線性回歸
array=('線性回歸')

for i in "${array[@]}" ; do
    python chatGPTCodeCopilot.py -w "$i" -o "$i" -k
done
# 實作線性回歸
python chatGPTCodeCopilot.py -e "${array[0]}" -b python -k -o "${array[0]}"
