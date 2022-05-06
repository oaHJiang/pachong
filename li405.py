# 写入Excel文件

# 1.导入xlwt模块
import xlwt
import random

# 2.创建一个Worlbook对象
workbook = xlwt.Workbook()

# 3.创建一个Sheet对象
sheet = workbook.add_sheet('sheet1')

# 4.使用sheet.write方法把数据写入到Sheet下指定行和列中。想在原有workbook对象上添加新的cell，那么需要调用put_cell来添加
headers = ['姓名', '语文', '数学', '英语']
for index, header in enumerate(headers):
    sheet.write(0, index, header)

names = ['张三', '李四', '王五']
for index, name in enumerate(names):
    sheet.write(index + 1, 0, name)

for row in range(1, 4):
    for col in range(1, 4):
        sheet.write(row, col, random.randint(1, 100))

# 5.保存成excel文件
workbook.save('成绩表1.xls')
