import xlrd

workbook = xlrd.open_workbook('成绩表.xlsx')

# 获取所有sheet名字
# print(workbook.sheet_names())

# 根据索引获取指定的sheet对象
# sheet=workbook.sheet_by_index(0)
# print(sheet.name)

# 根据名称获取指定的sheet对象
# sheet=workbook.sheet_by_name('1班')
# print(sheet.name)

# 获取所有sheet对象
# sheets=workbook.sheets()
# for sheet in sheets:
#     print(sheet.name)

# 获取指定sheet的行数和列数
sheet = workbook.sheet_by_index(0)
print({'rows': sheet.nrows, 'cols': sheet.ncols})
