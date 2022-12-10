from zipfile import *

with ZipFile('/Users/zackamiton/Desktop/Book1.xlsx', 'r') as xlsx:

    with xlsx.open('xl/sharedStrings.xml') as xf, xlsx.open('xl/worksheets/sheet1.xml') as lf:
        print([cell.decode('utf-8') for cell in xf.readlines()])
        print(lf.readlines())

    # print(xlsx.filelist)
        # print(xf.readlines())

#
# with open("/Users/zackamiton/Desktop/test.csv") as cf, zipfile.ZipFile("/Users/zackamiton/Desktop/Book1.xlsx", 'rb') as ef:
#     print(cf.readlines())
#     print(ef.readlines())