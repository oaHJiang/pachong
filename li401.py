#json字符串格式介绍
#字符串必须双引号
#对象(字典) 花括号
#列表(数组) 方括号
#多个数据间用逗号隔开，句末无逗号
import json
books=[
    {'title':'钢铁是怎样炼成的','price':9.8},{'title':'红楼梦','price':9.9}
]

#python对象转换成json字符串

#1.dumps函数
json_str=json.dumps(books,ensure_ascii=False)
print(json_str)

#2.dump函数
fp=open('book.json','w',encoding='utf-8')
json.dump(books,fp,ensure_ascii=False)
fp.close()

#json字符串load成Python对象

#1.loads函数
json_str='[{"title": "钢铁是怎样炼成的", "price": 9.8}, {"title": "红楼梦", "price": 9.9}]'
result=json.loads(json_str)
print(result)

#2.load函数
with open('book.json','r',encoding='utf-8') as fp:
    result=json.load(fp)
    print(result)
