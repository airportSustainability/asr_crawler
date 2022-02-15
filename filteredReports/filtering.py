import urllib.request
import xlrd
loc = ("./test.xlsx")

def download_file(download_url, filename):
    response = urllib.request.urlopen(download_url)
    file = open(filename + ".pdf", 'wb')
    file.write(response.read())
    file.close()

wb = xlrd.open_workbook(loc)
sheet = wb.sheet_by_index(0)
sheet.cell_value(0, 0)

n=1

for i in range(sheet.nrows):
    pdf_path = sheet.cell_value(i,0)
    print(sheet.cell_value(i, 0))
    download_file(pdf_path,str(n))
    n+=1

#pdf_path = "https://www.munich-airport.com/_b/0000000000000011206503bb60ae4589/winterbericht-20-21-en.pdf"


#download_file(pdf_path, "Test")
