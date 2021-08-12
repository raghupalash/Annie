from openpyxl import load_workbook

workbook = load_workbook(filename="database.xlsx")
sheet = workbook.active

sheet.Name = 'Watched'

workbook.save(filename="database.xlsx")