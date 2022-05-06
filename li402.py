import csv

# 读取CSV
'''
with open('movie.csv','r',encoding='utf-8') as fp:
    reader=csv.reader(fp)
    for x in reader:
        print(x[0]) 
'''

""" with open('000717.csv','r',encoding='gbk') as fp:
    reader=csv.DictReader(fp)
    for x in reader:
        print(x['收盘价'])  """

# 写入CSV

# 1.writerow：写入一行；writerows：写入多行
headers = ('name', 'age', 'height')
students = [
    ('张三', 18, 180),
    ('李四', 19, 190),
    ('王五', 20, 170)
]
with open('student.csv', 'w', encoding='utf-8', newline='') as fp:
    writer = csv.writer(fp)
    writer.writerow(headers)
    writer.writerows(students)
    # for data in students:
    # writer.writerow(data)

# 2.使用DictWriter
headers = ('name', 'age', 'height')
students = [
    {'name': '张三', 'age': 18, 'height': 180},
    {'name': '李四', 'age': 19, 'height': 190},
    {'name': '王五', 'age': 20, 'height': 170}
]
with open('student.csv', 'w', encoding='utf-8', newline='') as fp:
    writer = csv.DictWriter(fp, headers)
    writer.writeheader()  # 必须
    writer.writerows(students)
    # for data in students:
    # writer.writerow(data)
