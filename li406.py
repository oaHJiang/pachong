#excel文件的编辑
import xlrd
import xlwt
rwb=xlrd.open_workbook('成绩表.xlsx')
rsheet=rwb.sheet_by_index(0)

rsheet.put_cell(0,4,xlrd.XL_CELL_TEXT,'总分',None)
for row in range(1,13):
    grades=rsheet.row_values(row,1,4)
    total=sum(grades)
    rsheet.put_cell(row,4,xlrd.XL_CELL_NUMBER,total,None)

for col in range(1,5):
    grades=rsheet.col_values(col,1,13)
    avg=sum(grades)/len(grades)
    rsheet.put_cell(13,col,xlrd.XL_CELL_NUMBER,avg,None)

wwb=xlwt.Workbook()
wsheet=wwb.add_sheet('sheet1')
for row in range(0,14):
    for col in range(0,5):
        wsheet.write(row,col,rsheet.cell_value(row,col))

wwb.save('abc.xls')

