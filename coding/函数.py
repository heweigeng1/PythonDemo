# 定义函数与使用函数

def sayhello(name):
    print(name,", welcome")

sayhello("lili")

# 修改参数的值

def xgmsg(msg):
    msg="ok"

msg="no"

xgmsg(msg)

print(msg)
# msg依然为no,因为参数里修改的只是副本
nums=[10,1,2]
def xglist(nums):
    nums[0]=3
    nums.append(12)
xglist(nums)
print(nums)
# 关键字参数

def gjzfun(name, age):
    print("name:",name)
    print("age:",age)
# 可以看出参数的顺序是可以不一致的.
gjzfun(age=10,name="tom")

gjzfun(10,"tom")
# 如果是这样的话,则输出的顺序就错误了

# 缺省参数
def qxfun(name, age=10):
    print("name:",name)
    print("age:",age)
# 如果不输入此参数 则输出默认值
qxfun("tom")
qxfun("lili",40)

# 不定长参数

def bdcfun(name, *parame):
    print("输出:")
    print("name:",name)
    for par in parame:
        print(par,end=' ')

bdcfun("tom",10,"girl","home",22)

# 匿名函数
print("\n匿名函数")
sum=lambda val1,val2:val1+val2

num= sum(10,11)
print(num)

# 返回值
def getsum(val1, val2):
    return val1+val2

sum1=getsum(10,20)

print(sum1)