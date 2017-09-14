# 循环

# 普通循环
nums=[10,1,22,31,12,33]

for num in nums:
    print(num)

# 使用索引器

text=["apple","mi","huawei"]
for index in range(len(text)):
    print('phone:'+text[index])

# 嵌套if else
for num in nums:
    if num>20:
        print("我数组很大哟")
else:
    print("哎哟,怎么这样啊!")

# 冒泡排序
i=0
for index in range(len(nums)):
    for index2 in range(index+1,len(nums)):
        if nums[index] < nums[index2]:
            temp=nums[index]
            nums[index]=nums[index2]
            nums[index2]=temp
        i=i+1
        print (index,index2)
print(i)
print(nums)

# while循环
nums2=[]
nums3=[]
while len(nums)>0:
    num=nums.pop()
    if num>10:
        nums2.append(num)
    else :
        nums3.append(num)

print(nums2,nums3)

while len(nums2)>0 or len(nums3)>0:
    if len(nums2)>0:
        nums.append(nums2.pop())
    if len(nums3)>0:
        nums.append(nums3.pop())
else:
    print("is end")

print(nums)

# break
i=0
while True:
    if nums[i]>10:
        print(nums[i])
        i=i+1
        break
    
print('执行了:',i,'次')

# continue
i=0
_bool=True
while _bool:
    if len(nums)>i:
        print(nums[i])
        i=i+1
        continue
    else :
        _bool=False
print('执行了',i,'次')