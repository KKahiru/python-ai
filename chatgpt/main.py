import argparse
import os

import openai

HISTORY_PATH = 'history.log'
TOKEN_PATH = 'token.txt'

parser = argparse.ArgumentParser()
parser.add_argument('-r', '--reset', action='store_true', help='会話履歴(history.log)を初期化して実行する')
args = parser.parse_args()

history = ''
# トークンの読み込み
openai.api_key = open(TOKEN_PATH, 'r').read()
# リセットフラグが立っていない&ファイルが存在する場合履歴を読み込む
if os.path.isfile(HISTORY_PATH) and not args.reset:
    with open(HISTORY_PATH, 'r') as f:
        history = f.read()

# 会話として推論するため、会話ログを付け足してリクエストする
prompt = history
for i in range(0, 2):
    prompt += input('> ')
    response = openai.Completion.create(
        model='text-davinci-003',
        prompt=prompt,
        temperature=0,  # ランダム性の制御[0-1]
        max_tokens=1000,  # 返ってくるレスポンストークンの最大数
        top_p=1.0,  # 多様性の制御[0-1]
        frequency_penalty=1.0,  # 周波数制御[0-2]：高いと同じ話題を繰り返さなくなる
        presence_penalty=0.0  # 新規トピック制御[0-2]：高いと新規のトピックが出現しやすくなる
    )
    texts = ''.join([choice['text'] for choice in response.choices])
    print(texts)
    prompt += "\n" + texts + "\n\n"

# 会話履歴の保存
with open(HISTORY_PATH, 'w') as f:
    f.write(prompt)