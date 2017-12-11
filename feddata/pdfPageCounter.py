# Run by typing 'python pdfPageCounter.py' in terminal. Returns number of pdf pages in folder.

import os
import re

folders = os.listdir()
folders.remove(".DS_Store")
folders.remove("pdfPageCounter.py")
files = []
for folder in folders:
	path_to_folder = "./" + str(folder)
	new_files = os.walk(path_to_folder)
	for file in new_files:
		for f in file[2]:
			files.append(str(file[0]) + "/" + f)

rxcountpages = re.compile(r"/Type\s*/Page([^s]|$)", re.MULTILINE|re.DOTALL)


# pf = pdffile.pdffile('../rfc1950.pdf')
# pp = pages.pages(pf)
# len(pp.pagelist) 10

# print(files)
# print(files)
# print(files)
# print("some cool art above")

def countPages(files):
        pages = 0
        for file in files:
        	data = open(file,"rb").read()
        	page = rxcountpages.findall(data.decode('latin-1'))
        	pages += len(page)
        return pages

       # pages = 0
       #  for filepath in files:
       #  	pf = pdffile.PDFDocument(filepath)
       #  	pages += pf.count_pages()

if __name__=="__main__":
    print("Number of pages in Folder:", countPages(files))
