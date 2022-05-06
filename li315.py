from dataclasses import replace
from posixpath import split
import re

# 分组：
# text='apple price is $99,orange price is $88'
# res=re.search('.+(\$\d+).+(\$\d+)',text) #search寻找符合条件的第一个
# print(res.group(0)) 
# 0匹配整个分组
# 1匹配第一个分组
# groups()获取所有分组
# text='apple price is $99,orange price is $88'
# res=re.search('.+(\$\d+).+(\$\d+)',text) #search寻找符合条件的第一个
# print(res.group(0))

# findall:查找所有满足条件的,输出列表
# text='apple price is $99,orange price is $88'
# res=re.findall('\$\d+',text) #search寻找符合条件的第一个
# print(res)

# sub:根据规则替换其他字符串
# text='nihao zhongguo,hello world'
# res=text.replace(' ','\n') #replace函数
# res=re.sub(r' |,','\n',text)
# print(res)
'''
html="""
<div class="job-detail">Python开发工程师 
  <br>岗位职责： 
  <br>1、设计和开发扩展性良好的Python应用，进行算法模型部署和产品开发； 
  <br>2、调试和维护部门开发的Python应用，处理用户的反馈问题； 
  <br>3、相关技术说明和过程文档的撰写和归纳整理。 
  <br> 
  <br>岗位要求： 
  <br>1、熟练掌握Python编程语言，3年及以上解决实际问题的代码编写经验，熟悉编码规范，具备良好的文档编写能力； 
  <br>2、熟练掌握Flask、Django等Web框架，具有实际的项目经验； 
  <br>3、熟悉SQL语法，熟练掌握PostgreSQL/MySQL/Oracle/MongoDb等任一数据库； 
  <br>4、熟悉云服务开发，熟悉RabbitMQ/Kafka/Redis等常用组件； 
  <br>5、熟悉Hadoop/Hbase/Flink的使用，有项目经验的优先； 
  <br>6、熟悉Vue等框架的优先； 
  <br>7、有Devops开发经验的优先。 
  <br> 
  <br> 【公司福利】 
  <br>五险一金、绩效工资、年终奖金、员工激励计划、午餐补贴、加班晚餐补贴、加班打车费报销、每月团建读书会、国内旅游、年终海外游、生日礼金、定期体检、公司免费茶点、员工定制西装、年会超级大奖 
  <br>
</div>
"""
new_html=re.sub('<.+?>','',html)
print(new_html)
'''

# split:根据规则分割字符串
# text='nihao zhongguo,hello world'
# res=re.split(r' |,',text)
# print(res)

# compile:编译正则表达式
text = 'apple price is $34.56'
r = re.compile(r"""
\d+ # 整数部分
\.? # 小数点
\d+ # 小数部分
""", re.VERBOSE)  # 注释在search也可用
res = re.search(r, text)
print(res.group())
