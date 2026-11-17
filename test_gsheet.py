from google.oauth2.service_account import Credentials
import gspread

# --- Cấu hình ---
SERVICE_ACCOUNT_FILE = "service_account.json"
SPREADSHEET_ID = "YOUR_SHEET_ID_HERE"  # Thay bằng ID thật từ link Google Sheet

# --- Kết nối ---
SCOPES = [
    "https://www.googleapis.com/auth/spreadsheets",
    "https://www.googleapis.com/auth/drive.readonly"
]
creds = Credentials.from_service_account_file(SERVICE_ACCOUNT_FILE, scopes=SCOPES)
gc = gspread.authorize(creds)

sheet = gc.open_by_key(SPREADSHEET_ID).sheet1
print("✅ Kết nối Google Sheet thành công!")

# --- Test đọc dữ liệu ---
print("Dòng 1:", sheet.row_values(1))
