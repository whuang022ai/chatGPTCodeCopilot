from pyChatGPT import ChatGPT
from pathlib import Path
import re
import json
import argparse
import pathlib
import time
from sys import exit
__version__ = '0.0.1'
__author__ = u'whuang022'


session_token = 'your token'  # `__Secure-next-auth.session-token` cookie from https://chat.openai.com/chat
interval = 3
max_keep_asking_times = 10
api = ChatGPT(session_token)


stop_key_words = ['如果你想要更多信息', '歡迎隨時咨詢', '如果你有任何其他疑問',
                  '如果您還有其他疑問', '如果你有更多問題', '有任何疑問', '歡迎隨時與我們聯繫', '請隨時告訴我', '已經講完了', '已經說完了', '已經解釋完了', '可以咨詢其他資源', '如果你有任何疑問', '我會盡力為您解答', '如果您需要更詳細的說明', '我會盡力為你解答', '需要知道的具體信息', '我不太明白您想要我說什麼', '希望這些信息能幫助您', '希望這些信息能夠幫助您', '希望這些信息能幫到您', '希望這些資訊能幫助您', '希望這些資訊能夠幫助您', '希望這些資訊能幫到您', '希望這些信息對您有所幫助', '希望這些資訊對您有所幫助', '希望您會喜歡這些功能', '建議您可以自行研究', '我會盡力幫助你']


def get_lan_extension(language, suggest_extension=".txt"):
    json_f = "Programming_Languages_Extensions.json"
    with open(json_f, 'rt') as file:
        lines = ''.join(line.lower() for line in file)
        lan_lst = json.loads(lines)
        lan = language.lower()
        lan_info = next((s for s in lan_lst if s['name'] == lan), None)
        if lan_info:
            suggest_extension = lan_info["extensions"][0]

    return suggest_extension


def msg_extract_code(msg, task, id, path='.', target_lan_ext='.txt', code_block_re=r"```(.*?)\n(.*?)```"):
    code_blocks = re.findall(code_block_re, msg, re.DOTALL)
    for code in code_blocks:
        with open(f'{path}/{task}_code_block_{id}{target_lan_ext}', 'w') as f:
            print(code[1], file=f)
        id += 1


def translate_cmd(from_lan, target_lan, input_fname):
    prompt_1 = f"請幫我把以下{from_lan}程式碼翻譯成{target_lan}"
    input_code = Path(input_fname).read_text()
    cmd = f"{prompt_1}:\n{input_code}"
    return cmd


def simplify_cmd(target_lan, input_fname):
    prompt_1 = f"簡化以下{target_lan}的程式碼"
    input_code = Path(input_fname).read_text()
    cmd = f"{prompt_1}:\n{input_code}"
    return cmd


def example_cmd(target_lan, input=""):
    prompt_1 = f"請示範在{target_lan}程式語言中，怎麼使用\'{input}\'，請舉一個完整的例子?"
    cmd = f"{prompt_1}"
    return cmd


def whatis_cmd(input=""):
    prompt_1 = f"請詳細說明什麼是：\'{input}\'，給出一個常見的定義，再舉一些例子，如果有關於它的歷史或是未來發展更好"
    cmd = f"{prompt_1}"
    return cmd


def compare_cmd(input=""):
    input = input.replace(",", "和")
    prompt_1 = f"請詳細比較：\'{input}\'的差異？如果有優劣之分，可以比較各自的優缺點，並說明具體的例子。如果有表格也可以用表格搭配文字說明？"
    cmd = f"{prompt_1}"
    return cmd


def mistake_cmd(input=""):
    prompt_1 = f"請條列式的列舉一些新手在用\'{input}\'常犯錯的例子？"
    cmd = f"{prompt_1}"
    return cmd


def scratch_cmd(target_lan, input):
    prompt_1 = f"請給我一個在不使用程式庫的情況下用\'{target_lan}\'實做一個\'{input}\'，並詳細解說它的運作原理"
    cmd = f"{prompt_1}"
    return cmd


def keep_output_cmd():
    prompt_1 = "說下去"
    return prompt_1


def get_parser():
    parser = argparse.ArgumentParser('chatGPT Code Copilot')
    version = '%(prog)s ' + __version__
    parser.add_argument('--version', '-v', action='version', version=version)
    parser.add_argument('--output_path', '-o',
                        dest='output_path', action='store', default='./output')
    parser.add_argument('--translate', '-t', dest='translate', action='store',
                        help='useage -t [input.py] translate source code [input.py] from input language [-a] to target programming language [-b] ', )
    parser.add_argument('--example', '-e', dest='example', action='store',
                        help='useage : -e [what you want for gen example] to target programming language [-b] ')
    parser.add_argument('--whatis', '-w', dest='whatis', action='store',
                        help='useage : -w [the thing you want to ask ] ')
    parser.add_argument('--compare', '-c', dest='compare', action='store',
                        help='things to compare , useage : -c [things1,things2,things3 ... ] ')

    parser.add_argument('--mistake', '-m', dest='mistake', action='store',
                        help='useage : -m [the thing you want to ask about the basic mistakes ] ')
    parser.add_argument('--scratch', '-s', dest='scratch', action='store',
                        help='useage : -s [the thing you want make from scratch] ')

    parser.add_argument('--simplify', '-S', dest='simplify', action='store',
                        help='useage : -S [the sorce code fille name you want to simplify] ')

    parser.add_argument('--input_lan', '-a', dest='input_lan',
                        action='store', default='python')
    parser.add_argument('--output_lan', '-b',
                        dest='output_lan', action='store', default='python')

    parser.add_argument('--waiting_keep_ask', '-k',
                        dest='waiting_keep_ask', action='store_true')
    return parser


if __name__ == '__main__':
    parser = get_parser()
    args = parser.parse_args()
    lan_ext = get_lan_extension(args.output_lan)
    command_msgs = []
    tasks = []
    if args.translate:
        command_msg = translate_cmd(
            args.input_lan, args.output_lan, args.translate)
        command_msgs.append(command_msg)
        tasks.append(f"translate_{args.translate}")

    for option in ("example", "scratch", "simplify"):
        if getattr(args, option):
            command_msg = locals()[f"{option}_cmd"](
                args.output_lan, (getattr(args, option)))
            command_msgs.append(command_msg)
            tasks.append(f"{option}_{getattr(args, option)}")

    for option in ('whatis', 'compare', 'mistake'):
        if getattr(args, option):
            print(getattr(args, option))
            command_msg = locals()[f"{option}_cmd"](getattr(args, option))
            command_msgs.append(command_msg)
            tasks.append(f"{option}_{getattr(args, option)}")
    if command_msgs:
        id = 0
        pathlib.Path(args.output_path).mkdir(parents=True, exist_ok=True)
        for task, command_msg in zip(tasks, command_msgs):

            print(f"Me:{command_msg}")
            msg = ""
            first_msg = ""
            try:
                first_result = api.send_message(command_msg)
                first_msg = first_result['message']
            except Exception:
                print(Exception)
                exit()

            print("chatGPT:")
            print(first_msg)
            msg += first_msg
            for _ in range(0, max_keep_asking_times):
                time.sleep(interval)
                print(f"Me:{keep_output_cmd()}")
                other_msg = ""

                try:
                    other_result = api.send_message(keep_output_cmd())
                    other_msg = other_result['message']
                except Exception:
                    print(Exception)
                    break
                print("chatGPT:")
                print(other_msg)
                msg += other_msg
                if any(stop_key_word in other_msg for stop_key_word in stop_key_words):
                    print("End \n --------------")
                    break

                if args.waiting_keep_ask:
                    x = input(
                        "Press [y] to keep asking , press [n] to stop ask loop:\n")
                    if x == 'y' or x == 'Y':
                        continue
                    elif x == 'n' or x == 'N':
                        print("End\n --------------")
                        break

            with open(f'{args.output_path}/{task}.md', 'w') as f:
                print(msg, file=f)

            msg_extract_code(
                msg, task, id, path=args.output_path, target_lan_ext=lan_ext)
