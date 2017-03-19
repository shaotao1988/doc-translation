import openpyxl
import os, shutil
import translate3

filename = '/Users/ruby/Documents/doc-translation/test.xlsx'
path = os.path.dirname(filename)
new_filename = os.path.join(path, 'English.xlsx')
shutil.copyfile(filename, new_filename)

wb = openpyxl.load_workbook(new_filename)
ws = wb.active

js = translate3.Py4Js()

for row in ws.rows:
    for cell in row:
        tk = js.getTk(cell.value)
        cell.value = translate3.translate(cell.value, tk)

wb.save(new_filename)
