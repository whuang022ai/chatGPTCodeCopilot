# chatGPTCodeCopilot

using chatGPT to help coding and an auto book generator

用 chatGPT API 做的程式協助和教學工具的概念驗證的prototype

簡單說就是讓人工智慧自己寫基礎概念教學的書的一個概念驗證

## Installation

```
pip install pyChatGPT

git clone https://github.com/whuang022ai/chatGPTCodeCopilot.git
```

## Usage

check out how to get token from [here ](https://github.com/terry3041/pyChatGPT)

and replace your token in chatGPTCodeCopilot.py :

```
session_token = 'your token' 
```

--help, -h: help doc.

--version, -v: 顯示版本號

--output_path, -o: 設置輸出路徑，默認為 "./output"

--translate, -t: 翻譯原始碼，用法: -t [.py]，將輸入語言 [-a] 翻譯為目標語言 [-b]
```
python chatGPTCodeCopilot.py -t in.py -a python -b c++
```
--example, -e: 生成範例程式，用法: -e [what you want for gen example]，將生成範例程式輸出為目標語言 [-b]

```
python chatGPTCodeCopilot.py -e 線性回歸 -b python
```


--whatis, -w: 介紹某事情，用法: -w [the thing you want to ask]


```
python chatGPTCodeCopilot.py -w 線性回歸
```

--compare, -c: 比較多個東西，用法: -c [things1,things2,things3 ...]

```
python chatGPTCodeCopilot.py -c 人工智慧,機器學習
```

--mistake, -m: 詢問常見的新手錯誤，用法: -m [the thing you want to ask about the basic mistakes]

```
python chatGPTCodeCopilot.py -m for迴圈
```

--scratch, -s: 從頭開始創建特定東西，用法: -s [the thing you want make from scratch]

```
python chatGPTCodeCopilot.py -s 線性回歸
```

--simplify, -S: 簡化程式碼，用法: -S [the sorce code fille name you want to simplify]

```
python chatGPTCodeCopilot.py -S 要簡化的程式.py
```

--input_lan, -a: 設置輸入程式語言，默認為 "python"
--output_lan, -b: 設置輸出程式語言，默認為 "python"
--waiting_keep_ask, -k: 等待user輸入y/n決定要不要繼續問下去

## Example

生成AI基本概念解說+線性回歸的教學 :

```
./run_gen_book_example.sh
```

輸出結果都在 example_result

經過編輯後：
![a](https://user-images.githubusercontent.com/39413017/206676085-8c0f4210-53df-42d3-976d-689755d64ed0.png)
![b](https://user-images.githubusercontent.com/39413017/206676335-6c0c2bd2-3fd0-4e03-8107-8e1617c53c0a.png)

pdf在[這裡](https://drive.google.com/file/d/1QkdRuq0HjXaxgXl3IC6gDChNiebzV2WH/view?usp=sharing)

並且附上教學範例程式，也是由ChatGPT自動生成 [這](https://github.com/whuang022ai/chatGPTCodeCopilot/blob/main/example_result/%E7%B7%9A%E6%80%A7%E5%9B%9E%E6%AD%B8/example_%E7%B7%9A%E6%80%A7%E5%9B%9E%E6%AD%B8_code_block_1.py)


## Reference

pyChatGPT [ref. here](https://github.com/terry3041/pyChatGPT)
 Programming_Languages_Extensions.json [ref. here](https://gist.github.com/ppisarczyk/43962d06686722d26d176fad46879d41)

