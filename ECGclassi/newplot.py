import xlrd
import numpy as np
import matplotlib.pyplot as plt

file_location = "C:\Users\DELL\Desktop\qwert\raspberry_project\database\normal.xls"
workbook = xlrd.open_workbook(file_location)
first_sheet = workbook.sheet_by_index(0)

x = [first_sheet.cell_value(0,i) for i in range(180)]
#y = [first_sheet.cell_value(i, 1) for i in range(first_sheet.ncols)]


plt.plot(x)


plt.show()
