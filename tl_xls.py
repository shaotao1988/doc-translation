#!/usr/bin/env python

import xlrd,xlwt,xlutils,sys
from xlutils.filter import process,XLRDReader,XLWTWriter
import os, shutil
from translate3 import Translator

def copy2(wb):
    w = XLWTWriter()
    process(
        XLRDReader(wb,'unknown.xls'),
        w
        )
    return w.output[0][1], w.style_list


#http://stackoverflow.com/questions/3723793/preserving-styles-using-pythons-xlrd-xlwt-and-xlutils-copy
def put_value():
        filename = '/Users/ruby/Documents/doc-translation/test.xls'
        path = os.path.dirname(filename)
        new_filename = os.path.join(path, 'English.xls')
        shutil.copyfile(filename, new_filename)
        origin_workbook = xlrd.open_workbook(filename, formatting_info = True)
        #sheet = origin_workbook.sheet_by_name("sheet1")
        origin_sheet = origin_workbook.sheets()[0]
        nrows = origin_sheet.nrows
        ncols = origin_sheet.ncols
        print("rows:%d, cols:%d"%(nrows, ncols))
        work_book, style_list = copy2(origin_workbook)
        work_sheet = work_book.get_sheet(0)

        translator = Translator()
        
        for rownum in range(0, nrows):
            for colnum in range(0, ncols):
                cell = origin_sheet.cell(rownum, colnum)
                value = cell.value
                if len(value) > 0:
                        xf_index = origin_sheet.cell_xf_index(rownum, colnum)
                        print(value)
                        value = translator.translate(value)
                        work_sheet.write(rownum, colnum, value, style_list[xf_index])
        work_book.save(new_filename)

def main():
        put_value()

if __name__=="__main__":
        main()
