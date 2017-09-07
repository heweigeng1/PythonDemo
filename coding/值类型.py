# 字符串===================

text="hello wolrd"

#从下标0开始,取3位的值
str1=text[0:3]

print (str1)

#从下标0开始取至结束
str2=text[0:]

print(str2)

#拼接字符串
str1='hello '

str2='world!!'

print(str1+str2)

# List(列表)===================
list1=[10,20,30]

list2=[20,30]

print(list1[0:1])

print(list1[0:])

print(list1*2)

print(list1+list2)

# 元组===========================
tuple1=("abc",10,"tom",31)

tuple2=(1,30,"lili",18)

print(tuple1[0:1])

print(tuple2[0:])

print(tuple1+tuple2)

# 字典
dict1={"name":"tom","age":20}

dict1={"name":"lili","age":21}

print(dict1["name"])

print(dict1)

print(dict1.keys())

print(dict1.values())

dict1["age"]=30

print(dict1)

# 类型转换
dictstr=str(dict1)

print(dictstr)

print(dictstr[0:6])

# 查看数据类型

print(type(dict1))