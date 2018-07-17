
'''
#作业1
num1, num2 = eval(input('输入身高和体重：'))
bmi = num2/num1**2
if bmi < 18.5:
	print('体重过轻')
elif bmi > 32:
	print('非常肥胖')
elif 18.5<=bmi<=23.9:
	print('正常')
elif 24<=bmi<=27:
	print('过重')
else:
	print('肥胖')



#作业2
s = int(input('输入一个整形数：'))
i = 0
y = 0
for i in range(s+1):
	y = y + i
print(y)


#作业3

num = int(input('价格:'))
i = 0.1
s = 0.2
if 50 <= num<= 100:
	print("{:.0f}%{: >10.2f}".format(i*100, num*(1-i)))
elif num > 100:
	print("{:.0f}%{: >10.2f}".format(s*100, num*(1-s)))

'''

s = 'python'
y = 'p'
j = 'n'
if y in s:
	print(y)
if j in s:
	print(j)































