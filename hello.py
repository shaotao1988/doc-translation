#!/usr/bin/env python

import xlrd,xlwt,xlutils,sys
from xlutils.filter import process,XLRDReader,XLWTWriter
import translate3

def copy2(wb):
    w = XLWTWriter()
    process(
        XLRDReader(wb,'unknown.xls'),
        w
        )
    return w.output[0][1], w.style_list


#http://stackoverflow.com/questions/3723793/preserving-styles-using-pythons-xlrd-xlwt-and-xlutils-copy
def put_value():
        origin_work_book = xlrd.open_workbook('test.xls', formatting_info = True)
        #sheet = origin_work_book.sheet_by_name("sheet1")
        origin_sheet = origin_work_book.sheets()[0]
        nrows = origin_sheet.nrows
        ncols = origin_sheet.ncols
        print("rows:%d, cols:%d"%(nrows, ncols))
        work_book, style_list = copy2(origin_work_book)
        work_sheet = work_book.get_sheet(0)

        translate_col = 0
        #0 empty, 1 string, 2 number, 3 date, 4 boolean, 5 error
        ctype = 1

        js = translate3.Py4Js()
        
        for rownum in range(0,nrows):
                cell = origin_sheet.cell(rownum, translate_col)
                value = cell.value
                if len(value) > 0:
                        xf_index = origin_sheet.cell_xf_index(rownum, translate_col)
                        print(value)
                        tk = js.getTk(value)
                        value = translate3.translate(value, tk)
                        work_sheet.write(rownum, translate_col, value, style_list[xf_index])
        work_book.save('English.xls')

def main():
        put_value()

if __name__=="__main__":
        main()
