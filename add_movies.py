from openpyxl import load_workbook

workbook = load_workbook(filename="database.xlsx")
sheet = workbook.active

movies = ["Get Out", "The Shinning", "Into the Wild", "Shutter Island"]

for i, movie in enumerate(movies):
    sheet[f"A{i + 1}"] = movie

workbook.save(filename="database.xlsx")