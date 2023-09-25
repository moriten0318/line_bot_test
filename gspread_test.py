from google.oauth2.service_account import Credentials
import gspread

scopes = [
    'https://www.googleapis.com/auth/spreadsheets',
    'https://www.googleapis.com/auth/drive'
]

credentials = Credentials.from_service_account_file(    
    "C:\\Users\\moris\\Downloads\\gspread-400109-00716d87edde.json",
    scopes=scopes
)
#認証用のJSONファイルのパスを貼る(\は2個に変えること！)

gc = gspread.authorize(credentials)


spreadsheet_url = "https://docs.google.com/spreadsheets/d/1g4g0UNh74WJmemhGR3ftCQUWyt2_GbmYonw6CHo0XHo/edit#gid=0"

spreadsheet = gc.open_by_url(spreadsheet_url)
print(spreadsheet.sheet1.get_all_values())