import os
import PyPDF2

keywords = ['sustainability','annual report']

def checkPDF(name):
	pdfFile = open(name,'wb')
	pdfReader = PyPDF2.PdfFileReader(pdfFile)
	page = pdfReader.getPage(0)
	b = pageObj.extractText()
	c=0
	for i in keywords:
		if i in b:
			c+=1
	if c>0:
		print(name," perfected")
	else:
		print(name," deleted")
		os.remove(name)
	pdfFile.close()
	
	
	
