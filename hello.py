#!/usr/bin/env python

import xlrd,xlwt,sys
import codecs

#http://stackoverflow.com/questions/3723793/preserving-styles-using-pythons-xlrd-xlwt-and-xlutils-copy
def put_value():
        data = xlrd.open_workbook('test1.xlsx')
        #table = data.sheet_by_name("sheet1")
        table = data.sheets()[0]
        nrows = table.nrows
        ncols = table.ncols
        print(nrows)
        print(ncols)
        work_book = xlwt.Workbook()
        work_sheet = work_book.add_sheet('test')

        translate_col = 1
        #0 empty, 1 string, 2 number, 3 date, 4 boolean, 5 error
        ctype = 1
        
        for rownum in range(0,nrows):
                #value = table.row(rownum)[translate_col].value.encode('utf8')
                cell = table.row(rownum)[translate_col]
                value = cell.value
                if value:
                        print(value)
                        fmt = None
                        if cell.xf_index != None:
                                fmt = data.xf_list[cell.xf_index]
                                work_sheet.write(rownum, 0, value, fmt)
                        else:
                                work_sheet.write(rownum, 0, value)
                #work_sheet.write(rownum, ncols+1, value)
                #work_sheet.write(rownum, 0, value)
        work_book.save('t1.xls')

def main():
        put_value()

if __name__=="__main__":
        main()
