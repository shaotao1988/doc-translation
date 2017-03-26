import openpyxl
import os, shutil
from translate3 import Translator

filename = '/Users/ruby/Documents/doc-translation/test.xlsx'
path = os.path.dirname(filename)
new_filename = os.path.join(path, 'English.xlsx')
shutil.copyfile(filename, new_filename)

wb = openpyxl.load_workbook(new_filename)
ws = wb.active

translator = Translator()

for row in ws.rows:
    for cell in row:
        cell.value = translator.translate(cell.value)

wb.save(new_filename)
