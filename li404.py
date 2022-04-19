import xlrd

workbook=xlrd.open_workbook('成绩表.xlsx')

# 获取cell及其属性

#1.sheet.cell(row,col):获取指定行和列的cell对象
# sheet=workbook.sheet_by_index(0)
# cell=sheet.cell(1,1)
# print(cell.value)

#2.sheet.row_slice(row,stat_col,end_col)获取指定行的某几列对象
# sheet=workbook.sheet_by_index(0)
# cells=sheet.row_slice(1,1,4)
# for cell in cells:
#     print(cell.value)

#3.sheet.col_slice(col,stat_row,end_row)获取指定列的某几行对象
# sheet=workbook.sheet_by_index(0)
# cells=sheet.col_slice(1,0,12)
# for cell in cells:
#     print(cell.value)

#4.sheet.cell_value(row,col):获取指定行和列的值
# sheet=workbook.sheet_by_index(0)
# cell_value=sheet.cell_value(0,1)
# print(cell_value)


#5.sheet.row_values(row,stat_col,end_col)获取指定行的某几列的值
# sheet=workbook.sheet_by_index(0)
# cell_values=sheet.row_values(1,1,4)
# print(cell_values)

#6.sheet.col_values(col,stat_row,end_row)获取指定列的某几行的值
# sheet=workbook.sheet_by_index(0)
# cell_values=sheet.col_values(1,0,13)
# print(cell_values)

#cell的数据类型
sheet=workbook.sheet_by_index(0)
cell=sheet.cell(0,0)
print(cell.ctype) #结果为1代表文本类型：xlrd.XL_CELL_TEXT

cell=sheet.cell(1,1)
print(cell.ctype) #结果为2代表数值类型：xlrd.XL_CELL_NUMBER

cell=sheet.cell(13,0)
print(cell.ctype) #结果为3代表时间类型：xlrd.XL_CELL_DATE

cell=sheet.cell(13,2)
print(cell.ctype) #结果为0代表布尔类型：xlrd.XL_CELL_EMPTY




