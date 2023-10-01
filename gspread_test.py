from google.oauth2.service_account import Credentials
import gspread
import socket
import time

scopes = [
    'https://www.googleapis.com/auth/spreadsheets',
    'https://www.googleapis.com/auth/drive'
]

credentials = Credentials.from_service_account_file(    
    "C:\\Users\\moris\\Downloads\\gspread-400109-00716d87edde.json",
    scopes=scopes
)
#認証用のJSONファイルのパスを貼る(\は2個に変えること！)

gc = gspread.authorize(credentials)#GoogleAPIにログイン
spreadsheet_url = "https://docs.google.com/spreadsheets/d/1g4g0UNh74WJmemhGR3ftCQUWyt2_GbmYonw6CHo0XHo/edit#gid=0"

HOST = '127.0.0.1'
PORT = 50007
client = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

lastnum = 0
null = ""
current_list = []

#スプレッドシートを取得するための関数
def get_sheet():        
    spreadsheet = gc.open_by_url(spreadsheet_url).sheet1
    import_value = spreadsheet.col_values(2)#B行の要素を取得
    print(import_value)
    return import_value
    #spreadsheet.acell('B'+cell_number).value


#UDP通信周りの関数
def UDP(content):
    client.sendto(content.encode('utf-8'),(HOST,PORT))



while True:
    new_list = get_sheet()    
    if new_list==current_list:
        print("更新はありません")
        time.sleep(5.0)
        continue
    else:
    #スプレッドシートに更新があったときの処理
        for i in range(lastnum,len(new_list)):
            print(new_list[i])
            UDP(new_list[i])
        current_list = new_list
        lastnum = len(current_list)
        time.sleep(5.0)

