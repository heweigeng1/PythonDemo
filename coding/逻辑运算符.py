x=100
y=10
if x<10:
    print(True)
else :
    print(False)


# 多重判断
print("多重判断")
if x<100:
    print('x<100')
elif y>100:
    print('y>100')
else :
    print("很尴尬,都不正确")

# 多条件
print("多条件")
if x<1000 or y>100:
    print('x<1000 or y>100')
elif x<1000:
    print('x<1000')

# 短路规则
print('短路规则')
if x<1000 or 0/x>0:
    print(True)
else :
    print(False)

# 这个写法就会报错
if  0/x>0 or x<1000 
    print(True)
else :
    print(False)
