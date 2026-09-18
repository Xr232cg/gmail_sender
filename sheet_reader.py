import pathlib
import gspread
from google.oauth2 import service_account

def choose_sheet(gs):
    all_sheets = gs.list_spreadsheet_files()

    for i,sh in enumerate(all_sheets):
        print(f"{i}: {sh['name']}")

    sheet_n = int(input("開啟的試算表編號: "))

    return all_sheets[sheet_n]['name']

def sheet_reader():#hihi
    scopes = ['https://spreadsheets.google.com/feeds', 'https://www.googleapis.com/auth/drive']
    json_file=pathlib.Path(__file__).parent/"config"/"Auth_gmail-sender-app.json"

    credential = service_account.Credentials.from_service_account_file(json_file,scopes=scopes)
    gs = gspread.authorize(credential)
    all_sheets = gs.list_spreadsheet_files()
    sheet_name=choose_sheet(gs)

    data_sheet=gs.open(sheet_name)
    try:
        ensurance_data=data_sheet.worksheet("表單回覆 1")
    except Exception as e:
        print(e)
        return 1

    range_values = ensurance_data.get("E1:G50")
    print(*range_values)

    return 0

if __name__ == "__main__":
    sheet_reader()


