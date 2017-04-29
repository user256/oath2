import gspread
from oauth2client.service_account import ServiceAccountCredentials
sitemap = "1A7tLJDZKiSTqg38pswLlCjdXNn4VRi6kok1QHhC-jZ0"

#http://gspread.readthedocs.io/en/latest/

# use creds to create a client to interact with the Google Drive API
scope = ['https://spreadsheets.google.com/feeds','https://www.googleapis.com/auth/drive']
creds = ServiceAccountCredentials.from_json_keyfile_name('/home/user256/PycharmProjects/passwords/sheets_client_secrets.json', scope)
client = gspread.authorize(creds)

#client.create("Pythons")
pythons = client.open("Pythons")
python = client.open("Pythons").sheet1
pythonid = pythons.id
pythons.share('johnwilliamfegan@gmail.com', perm_type='user', role='writer')
list = ["URL1", "URL2", "URL3", "URL4", "URL5", "URL6", "URL7"]
i=1
for x in list:
    python.update_cell(i, 1, x)
    i = i + 1

#python = client.open("Pythons").sheet1
#python.update_cell(1, 1, "Your ma is your da")
#alldata = python.get_all_records()
print (pythonid)



def tabaccess():
    sheet = client.open("CMC Sitemap Sitemap").sheet1 #opens a sheet
    list_of_hashes = sheet.get_all_records() #extract all records
    allvalues = sheet.get_all_values() #extract all of the values

def sheetaccess():
    sheets = client.open("CMC Sitemap Sitemap") #opens a file
    index = sheets.get_worksheet(0) #list tab ID
    permissions = client.list_permissions("1A7tLJDZKiSTqg38pswLlCjdXNn4VRi6kok1QHhC-jZ0") #get permissions by ID

def pythoncreate():
    #client.create("Python Sheet")
    #python1 = client.open("Python Sheet").sheet1
    #python1.update_cell(1, 1, "Your ma is your da")
    #records = python1.get_all_records() #extract all records
    print ("banana")

"""
i = 1
while i <= 5:
    sheet.update_cell(i, 1, "Your ma is your da")
    i = i + 1
"""
#pythoncreate()

