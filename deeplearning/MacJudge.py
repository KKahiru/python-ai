from keras.models import load_model
import PySimpleGUI as sg

sg.theme('Default1')   # デザインテーマの設定

# ウィンドウに配置するコンポーネント
layout = [  [sg.Text('ここは1行目')],
            [sg.Text('ここは2行目：適当に文字を入力してください'), sg.InputText()],
            [sg.Button('Choose'), sg.Button('キャンセル')] ]

# ウィンドウの生成
window = sg.Window('サンプルプログラム', layout)

# イベントループ
while True:
    event, values = window.read()
    if event == sg.WIN_CLOSED or event == 'キャンセル':
        break
    elif event == 'Choose':
        result = sg.popup_get_file("ファイルを選択してください",
        file_types = ("JPEG files", [".jpg", ".jpeg"]),
        no_window = True)

window.close()