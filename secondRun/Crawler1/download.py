import urllib.request
import xlrd
from urllib.error import *

loc = ("./3Filtered.xlsx")

file = open("403Forbidden.txt","w")
file.write("List of urls that gave 403 forbiden errors:\n")
file.close()

file2 = open("otherErrors.txt","w")
file2.write("List of urls with other errors:\n")
file2.close()

def download_file(download_url, filename):
    try:
        response = urllib.request.urlopen(download_url)
        file = open(filename + ".pdf", 'wb')
        file.write(response.read())
        file.close()
    except HTTPError as e:
        if e.code == 403:
            file1 = open("403Forbidden.txt","a")
            file1.write(download_url+"\n")
            file1.close()
    except (URLError,InvalidURL,ConnectionError,ProxyError,SSLError,TooManyRedirects):
        file2 = open("otherErrors.txt","a")
        file2.write(download_url+"\n")
        file2.close()



wb = xlrd.open_workbook(loc)
sheet = wb.sheet_by_index(0)
sheet.cell_value(0, 0)

n=1

for i in range(sheet.nrows):
    pdf_path = sheet.cell_value(i,0)
    print(sheet.cell_value(i, 0))
    download_file(pdf_path,str(n))
    n+=1
