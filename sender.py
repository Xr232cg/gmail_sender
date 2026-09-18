import pathlib
import gspread
from google.oauth2 import service_account

def main():
    scopes = ['https://spreadsheets.google.com/feeds', 'https://www.googleapis.com/auth/drive']
    json_file=pathlib.Path(__file__).parent/"model"/"Auth_gmail-sender-app-509000.json"

    credential = service_account.Credentials.from_service_account_file(json_file,scopes=scopes)

    gs = gspread.authorize(credential)

    data_sheet=gs.open("2026《我這一生如履薄冰，你說我能看到AC嗎》八校電資聯合迎新 - 幹部資料 (回覆)")
    try:
        ensurance_data=data_sheet.worksheet("表單回覆 1")
    except Exception as e:
        print(e)
        return 1

    range_values = ensurance_data.get("A1:C10")

    print(*range_values)\

    return 0

if __name__ == "__main__":
    main()


