import general_functions

# Opening the workbook
book = general_functions.openGoogle()
# Doing the actual script
book.worksheet('test').update([[1, 2], [3, 4]], 'A1:B2')