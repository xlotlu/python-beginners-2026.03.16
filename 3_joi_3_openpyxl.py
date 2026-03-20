from openpyxl import load_workbook

wb = load_workbook("data/books.xlsx")
sheet = wb.worksheets[0]

# iterăm row cu row
for row in sheet.rows:
    for cell in row:
        print(cell.value)

# iterăm prin celulele unei coloane
for cell in sheet["C":"C"]:
    print(cell)
    break

# iterăm printr-un slice de coloane
for column in sheet["A":"C"]:
    x = 0
    for cell in column:
        print(cell.value)

        x += 1
        if x > 5: break
