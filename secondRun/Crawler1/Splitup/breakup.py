import urllib.request
import xlrd
from urllib.error import *
from requests.exceptions import *
loc = ("./1FilteredUpdated.xlsx")

file = open("403Forbidden.txt","w")
file.write("List of urls that gave 403 forbiden errors:\n")
file.close()

file2 = open("otherErrors.txt","w")
file2.write("List of urls with other errors:\n")
file2.close()

m=1

def download_file(download_url, filename):
    try:
        download_url_main = str(download_url.replace(" ",""))
        response = urllib.request.urlopen(download_url_main)
        print(download_url)
        file = open(filename + ".pdf", 'wb')
        file.write(response.read())
        file.close()
        global m
        m+=1
    except HTTPError as e:
        if e.code == 403:
            file1 = open("403Forbidden.txt","a")
            file1.write(download_url+"\n")
            file1.close()
        else:
            file3 = open("otherErrors.txt","a")
            file3.write(download_url+"\n")
            file3.close()
    except (URLError,ConnectionError, ProxyError, SSLError, TooManyRedirects, InvalidURL):
        file2 = open("otherErrors.txt","a")
        file2.write(download_url+"\n")
        file2.close()



wb = xlrd.open_workbook(loc)
sheet = wb.sheet_by_index(0)
sheet.cell_value(0, 0)

n=1
print("Starting now")

for i in range(sheet.nrows):
    pdf_path = sheet.cell_value(i,0)
    #print(type(pdf_path))
    if type(pdf_path) == str:
    	#print("True")
    	download_file(pdf_path,str(m))
    elif type(pdf_path) == unicode:
    	#print("False")
    	file2 = open("otherErrors.txt","a")
    	pdf_path1 = pdf_path.encode("utf-8")
    	file2.write(pdf_path1,"\n")
    	file2.close()
    else:
    	pass
    """
    print(sheet.cell_value(i, 0))
    download_file(pdf_path,str(n))
    n+=1"""
