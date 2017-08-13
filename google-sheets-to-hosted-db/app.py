# The gspread library
import gspread
# OAuth2 Client Lib
from oauth2client.service_account import ServiceAccountCredentials
# Optional , for pretty printing
import pprint

scope = ['https://spreadsheets.google.com/feeds']
creds = ServiceAccountCredentials.from_json_keyfile_name('file/path/of/your/client.secret.json', scope)
# Authorize your web server to access spreadsheet
client = gspread.authorize(creds)


sheets = client.open("your-spreadsheet-name").sheet1

# To get all records
sheets.get_all_records()

# Get a particular row value
sheets.row_values(<int>)

# Get a column's values
sheets.col_values()

# Update a cell
sheets.update_cell(<int>,<int>,<value>)

# Get a particular cell values
sheets.cell(<int>,<int>).value

# Insert a row
sheets.insert_row(<Enter values>)

# Delete a row 
sheets.delete_row(<int>)

# Row count 
sheets.row_count

# Column Count
sheets.col_count

# Update a particular cell
sheets.update_cell(1,1, 'Love is life')